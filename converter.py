import re


def replace_to_camel(s):
    s = s.group(0)
    if '_' not in s:
        return s
    ss = s.split('_')
    sss = ss[0]
    for ssss in ss[1:]:
        if not ssss:
            continue
        sss += ssss[0].upper() + ssss[1:]
    return sss


def replace_to_space_camel(s):
    s = s.group(0)
    if '_' not in s:
        return s
    ss = s.split('_')
    for ssss in ss:
        if not ssss:
            continue
        sss += ' ' + ssss[0].upper() + ssss[1:]
    return sss


def main(s):
    rrr = re.compile(r'[a-zA-Z_][a-zA-Z_0-9]*', re.MULTILINE | re.DOTALL)
    # return rrr.sub(replace_to_camel, s)
    return rrr.sub(replace_to_space_camel, s)


if __name__ == '__main__':
    sample_string = """
test = "hoge_foo" + "var" + "python_ruby"
too_foo
tet_
"""
    print main(sample_string)
