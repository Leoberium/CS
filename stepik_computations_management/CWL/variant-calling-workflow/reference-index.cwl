cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing: [ $(inputs.genome) ]

baseCommand: [samtools, faidx]

inputs:
  genome:
    type: File
    inputBinding:
      position: 0
      valueFrom: $(self.basename)

outputs:
  genome_with_index:
    type: File
    secondaryFiles: .fai
    outputBinding:
      glob: $(inputs.genome.basename)
