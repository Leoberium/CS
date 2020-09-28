cwlVersion: v1.0
class: Workflow

requirements:
  - class: ScatterFeatureRequirement

inputs:
  input_dir: Directory

outputs:
  outfile:
    type: File[]
    outputSource: hello/outfile

steps:

  list_files:
    run:
      class: ExpressionTool
      requirements:
        - class: InlineJavascriptRequirement
      inputs:
        indir: Directory
      outputs:
        outfile: File[]
      expression: |
        ${
          var samples = [];
          for (var i = 0; i < inputs.indir.listing.length; i++) {
            var file = inputs.indir.listing[i];
            if (/^\w.*$/.test(file.basename)) {
              samples.push(file);
            }
          }
          return {"outfile": samples};
        }
    in:
      indir: input_dir
    out:
      [outfile]

  hello:
    run:
      class: CommandLineTool
      requirements:
        - class: InlineJavascriptRequirement
      inputs:
        infile:
          type: File
          inputBinding:
            loadContents: true
            valueFrom: $("Hello " + inputs.infile.contents.trim() + "!")
      outputs:
        outfile: stdout
      baseCommand: echo
      stdout: ${return inputs.infile.basename}
    in:
      infile: list_files/outfile
    scatter:
      infile
    out:
      [outfile]
