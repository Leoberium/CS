cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: InitialWorkDirRequirement
    listing: [ $(inputs.zipped_vcf_file) ]

baseCommand: tabix

inputs:
  zipped_vcf_file:
    type: File
    inputBinding:
      position: 2
      valueFrom: $(self.basename)

outputs:
  zipped_vcf_file_with_index:
    type: File
    secondaryFiles: .tbi
    outputBinding:
      glob: $(inputs.zipped_vcf_file.basename)

arguments:
  - position: 1
    prefix: -p
    valueFrom: vcf
