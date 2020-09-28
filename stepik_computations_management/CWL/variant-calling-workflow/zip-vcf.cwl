cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: InitialWorkDirRequirement
    listing: [ $(inputs.vcf_file) ]

baseCommand: bgzip

inputs:
  vcf_file:
    type: File
    inputBinding:
      position: 1
      valueFrom: $(self.basename)

outputs:
  zipped_vcf_file:
    type: File
    outputBinding:
      glob: $(inputs.vcf_file.basename).gz
