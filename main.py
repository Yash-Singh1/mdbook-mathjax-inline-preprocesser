import re
import sys
import json

if len(sys.argv) > 1:
  sys.exit(0)
else:
  data = json.load(sys.stdin)
  for i in range(len(data[1]['sections'])):
    data[1]['sections'][i]['Chapter']['content'] = re.sub(r'^((?<!\\)(?:\\\\)*)\$\$', '\g<1>\\\\\\\\[', data[1]['sections'][i]['Chapter']['content'], flags=re.MULTILINE)
    data[1]['sections'][i]['Chapter']['content'] = re.sub(r'((?<!\\)(?:\\\\)*)\$\$$', '\g<1>\\\\\\\\]', data[1]['sections'][i]['Chapter']['content'], flags=re.MULTILINE)
  for i in range(len(data[1]['sections'])):
    data[1]['sections'][i]['Chapter']['content'] = re.sub(r'((?<!\\)(?:\\\\)*)\$(.+?)((?<!\\)(?:\\\\)*)\$', r'\g<1>\\\\\(\g<2>\\\\\)\g<3>', data[1]['sections'][i]['Chapter']['content'])
  print(json.dumps(data[1]))
