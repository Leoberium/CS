cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: ShellCommandRequirement

baseCommand: [samtools, mpileup]

inputs:
  genome_with_index:
    type: File
    inputBinding:
      position: 1
      prefix: '-uf'
  alignment:
    type: File
    inputBinding:
      position: 2

outputs:
  samtools_vcf: stdout

arguments:
  - position: 3
    valueFrom: "| bcftools view -vcg -"
    shellQuote: false

stdout: samtools_$(inputs.alignment.nameroot).vcf
