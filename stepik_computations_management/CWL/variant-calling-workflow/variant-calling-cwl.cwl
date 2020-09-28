cwlVersion: v1.0
class: Workflow

requirements:
  - class: StepInputExpressionRequirement
  - class: ScatterFeatureRequirement
  - class: MultipleInputFeatureRequirement

inputs:
  input_bam: File
  reference_genome: File
outputs:
  count:
    type: File
    outputSource: count_common_variants/count

steps:

  reference_index:
    run: ./reference-index.cwl
    in: { genome: reference_genome }
    out: [ genome_with_index ]

  reference_dict:
    run: ./reference-dict.cwl
    in:
      genome: reference_index/genome_with_index
      output_filename:
        valueFrom: $(inputs.genome.nameroot).dict
    out: [ genome_with_dictionary ]

  index_bam:
    run: ./index-bam.cwl
    in: { alignment: input_bam }
    out: [ alignment_with_index ]

  variant_calling_samtools:
    run: ./variant-calling-samtools.cwl
    in:
      genome_with_index: reference_index/genome_with_index
      alignment: input_bam
    out: [ samtools_vcf ]

  variant_calling_freebayes:
    run: ./variant-calling-freebayes.cwl
    in:
      genome_with_index: reference_index/genome_with_index
      alignment: input_bam
    out: [ freebayes_vcf ]

  variant_calling_haplotypecaller:
    run: ./variant-calling-haplotypecaller.cwl
    in:
      genome_with_dictionary: reference_dict/genome_with_dictionary
      alignment_with_index: index_bam/alignment_with_index
      output_filename:
        valueFrom: haplotypecaller_$(inputs.alignment_with_index.nameroot).vcf
    out: [ haplotypecaller_vcf ]

  zip_vcf:
    run: ./zip-vcf.cwl
    in:
      vcf_file:
          - variant_calling_samtools/samtools_vcf
          - variant_calling_freebayes/freebayes_vcf
          - variant_calling_haplotypecaller/haplotypecaller_vcf
    scatter: vcf_file
    out: [ zipped_vcf_file ]

  index_vcf:
    run: ./index-vcf.cwl
    in: { zipped_vcf_file: zip_vcf/zipped_vcf_file }
    scatter: zipped_vcf_file
    out: [ zipped_vcf_file_with_index ]

  count_common_variants:
    run: ./count-common-variants.cwl
    in:
      zipped_vcfs: index_vcf/zipped_vcf_file_with_index
      alignment: input_bam
    out: [ count ]
