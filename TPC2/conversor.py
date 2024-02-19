import re

txt = "> hola"
h1_exp = re.search("^#[^#].*$", txt)
h2_exp = re.search("^#{2}[^#].*$", txt)
h3_exp = re.search("^#{3}[^#].*$", txt)

bold_exp = re.search("^\*{2}[^\*].*\*{2}$", txt)
italic_exp = re.search("^\*[^\*].*\*$", txt)

blockquote_exp = re.search(">.*", txt)

list_exp = re.search("", txt)


if blockquote_exp:
    print("match")
else:
    print("no match")

