import re

h1_exp = re.compile("^#[^#].*$")
h2_exp = re.compile("^#{2}[^#].*$")
h3_exp = re.compile("^#{3}[^#].*$")
bold_exp = re.compile("^\*{2}[^\*].*\*{2}$")
italic_exp = re.compile("^\*[^\*].*\*$")
blockquote_exp = re.compile(">.*$")
list_exp = re.compile("^\d\..*$")
item_exp = re.compile("^-[^-].*$")
code_exp = re.compile("^`{3}[^`].*\n[\s\S]*?`{3}$")
bar_exp = re.compile("^--$")
title_exp = re.compile("^\[\w*\]\([\w:\/.]*\)")
image_exp = re.compile("^!\[[^\]]*\]\(\.\.\/[^\)]*\)")

