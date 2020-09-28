cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing: [ $(inputs.genome) ]

baseCommand: java

inputs:
  genome:
    type: File
    secondaryFiles: .fai
    inputBinding:
      position: 2
      prefix: R=
      separate: false
      valueFrom: $(self.basename)
  output_filename:
    type: string
    inputBinding:
      position: 3
      prefix: O=
      separate: false

outputs:
  genome_with_dictionary:
    type: File
    secondaryFiles: [ .fai, ^.dict ]
    outputBinding:
      glob: $(inputs.genome.basename)

arguments:
  - position: 0
    prefix: '-jar'
    valueFrom: /opt/picard/picard.jar
  - position: 1
    valueFrom: CreateSequenceDictionary
