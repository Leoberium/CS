cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing: [ $(inputs.alignment) ]

baseCommand: [samtools, index]

inputs:
  alignment:
    type: File
    inputBinding:
      position: 0
      valueFrom: $(self.basename)

outputs:
  alignment_with_index:
    type: File
    secondaryFiles: .bai
    outputBinding:
      glob: $(inputs.alignment.basename)
