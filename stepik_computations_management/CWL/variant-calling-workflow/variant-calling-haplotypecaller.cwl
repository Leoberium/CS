cwlVersion: v1.0
class: CommandLineTool

baseCommand:
  - java

inputs:
  genome_with_dictionary:
    type: File
    inputBinding:
      position: 3
      prefix: -R
  alignment_with_index:
    type: File
    inputBinding:
      position: 4
      prefix: -I
  output_filename:
    type: string
    inputBinding:
      position: 5
      prefix: -o

outputs:
  haplotypecaller_vcf:
    type: File
    outputBinding:
      glob: $(inputs.output_filename)

arguments:
  - position: 1
    prefix: '-jar'
    valueFrom: /opt/gatk/GenomeAnalysisTK.jar
  - position: 2
    prefix: '-T'
    valueFrom: HaplotypeCaller
