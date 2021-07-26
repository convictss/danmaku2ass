import codecs
with open(r'./1.xml', 'r', encoding='utf-8', errors='replace') as f:
    s = f.read()
    print(len(s))

with open(r'./1j.xml', 'r', encoding='utf-8', errors='replace') as f:
    s = f.read()
    print(s.startswith('\ufeff'))
    s = s.replace('\ufeff', '')
    print(len(s))
    # print(codecs.BOM_UTF8)
    # print(s[:3] == codecs.BOM_UTF8)
    # print(s[:3] == '\xef\xbb\xbf')

