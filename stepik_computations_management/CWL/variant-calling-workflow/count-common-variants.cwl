cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: ShellCommandRequirement

baseCommand: [vcf-isec, -f]

inputs:
  zipped_vcfs:
    type: File[]
    inputBinding:
      position: 2
  alignment:
    type: File

outputs:
  count: stdout

arguments:
  - position: 1
    prefix: -n
    valueFrom: "+2"
  - position: 3
    valueFrom: "| grep -v ^# -c"
    shellQuote: false

stdout: $(inputs.alignment.nameroot)_count.txt
