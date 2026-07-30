import re
html = open('index.html', encoding='utf-8').read()
m = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if not m:
    print('No script found')
else:
    js = m.group(1)
    for i, line in enumerate(js.split('\n'), 1):
        stripped = line.strip()
        # Check for literal backslash before backtick
        if r'\`' in line:
            print(f'ESCAPED_BACKTICK line {i}: {stripped[:150]}')
        if r'\${' in line:
            print(f'ESCAPED_DOLLAR line {i}: {stripped[:150]}')
    print('Done')
