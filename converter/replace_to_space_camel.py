import re


def convert(string):
    rrr = re.compile(r'\[?\(?[a-zA-Z_][a-zA-Z_0-9]*', re.MULTILINE | re.DOTALL)
    return rrr.sub(replace_to_space_camel, string)

def replace_to_space_camel(s):
    s = s.group(0)
    if '_' not in s:
        return s
    ss = s.split('_')
    if ss[0][0] == '[':
        sss = '[(' + ss[0][2].upper() + ss[0][3:]
    else:
        sss = '[' + ss[0][0].upper() + ss[0][1:]
    for ssss in ss[1:]:
        if not ssss:
            continue
        sss += ' ' + ssss[0].upper() + ssss[1:]
    if ss[0][0] == '[':
        return sss
    else:
        return sss + ']'
