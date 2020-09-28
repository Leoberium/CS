cwlVersion: v1.0
class: CommandLineTool
baseCommand: [wc, -w]

inputs:
  input_file: File

outputs:
  word_count: stdout

stdin: $(inputs.input_file.path)
stdout: output
