cwlVersion: v1.0
class: ExpressionTool

requirements:
  - class: InlineJavascriptRequirement

inputs:
  infile:
    type: File
    inputBinding:
      loadContents: true

outputs:
  string_list: string[]

expression: |
  ${
    var file = inputs.infile.contents.trim();
    var ch, cnt;
    var counts = {};
    for (var i = 0; i < file.length; i++) {
      ch = file.charAt(i);
      cnt = counts[ch];
      counts[ch] = cnt ? cnt + 1 : 1;
    }
    var s = [];
    for (ch in counts) {
      s.push(ch + ": " + counts[ch]);
    }
    s.sort();
    return {"string_list": s};
  }
