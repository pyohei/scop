"""Convert snake case into Camel case."""
import re

def convert(string):
    rrr = re.compile(r'\[?\(?[a-zA-Z_][a-zA-Z_0-9]*', re.MULTILINE | re.DOTALL)
    return rrr.sub(_replace_to_camel, string)

def _replace_to_camel(s):
    s = s.group(0)
    if '_' not in s:
        return s
    ss = s.split('_')
    # sss = ss[0]
    sss = ss[0][0].upper() + ss[0][1:]
    for ssss in ss[1:]:
        if not ssss:
            continue
        sss += ' ' + ssss[0].upper() + ssss[1:]
    return sss
