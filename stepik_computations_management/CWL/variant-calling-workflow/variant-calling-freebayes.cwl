cwlVersion: v1.0
class: CommandLineTool

baseCommand:
  - freebayes

inputs:
  genome_with_index:
    type: File
    inputBinding:
      position: 1
      prefix: '-f'
  alignment:
    type: File
    inputBinding:
      position: 2
outputs:
  freebayes_vcf: stdout

stdout: freebayes_$(inputs.alignment.nameroot).vcf
