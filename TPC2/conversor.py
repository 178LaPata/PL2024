import re, os

h1_exp = re.compile("^#[^#].*$")
h2_exp = re.compile("^#{2}[^#].*$")
h3_exp = re.compile("^#{3}[^#].*$")
bold_exp = re.compile("^\*{2}[^\*].*\*{2}$")
italic_exp = re.compile("^\*[^\*].*\*$")
blockquote_exp = re.compile(">.*$")
list_exp = re.compile("^\d\..*$")
item_exp = re.compile("^-[^-].*$")
code_exp = re.compile("^`[^`].*[^`]`$")
bar_exp = re.compile("^--$")
title_exp = re.compile("^\[\w*\]\([\w:\/.]*\)")
image_exp = re.compile("^!\[[^\]]*\]\(\.\.\/[^\)]*\)")

preHTML =  """
<!DOCTYPE html>
<html>
    <head>
        <title>Conversor MD para HTML</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="utf-8"/>
    </head>
    <body>
        <div>
"""

posHTML = """
        </div>
    </body>
</html>
"""

def convert(line):
    retos = ""
    curvos = ""
    for i in range(len(line)):
        if line[i] == "[":
            for j in range(i+1, len(line)):
                if line[j] == "]":
                    break
                retos += line[j]
        if line[i] == "(":
            for j in range(i+1, len(line)):
                if line[j] == ")":
                    break
                curvos += line[j]
    if line[0] == "!":
        return f"<img src={curvos} alt={retos}>\n"
    else:
        return f"<a href={curvos}>{retos}</a>\n"

def convert_md2html(md_file):
    with open(md_file, 'r') as md:
        conteudoHTML = ""
        for line in md:
            if h1_exp.match(line):
                conteudoHTML += f"<h1>{line[2:]}</h1>\n"
            elif h2_exp.match(line):
                conteudoHTML += f"<h2>{line[3:]}</h2>\n"
            elif h3_exp.match(line):
                conteudoHTML += f"<h3>{line[4:]}</h3>\n"
            elif bold_exp.match(line):
                conteudoHTML += f"<b>{line[2:-3]}</b>\n"
            elif italic_exp.match(line):
                conteudoHTML += f"<i>{line[1:-2]}</i>\n"
            elif blockquote_exp.match(line):
                conteudoHTML += f"<blockquote>{line[1:]}</blockquote>\n"
            elif list_exp.match(line):
                if conteudoHTML[-6:] == "</ol>\n":
                    conteudoHTML = conteudoHTML[:-6] + f"<li>{line[2:]}</li>\n</ol>\n"
                else:
                    conteudoHTML += f"<ol><li>{line[2:]}</li></ol>\n"
            elif item_exp.match(line):
                if conteudoHTML[-6:] == "</ul>\n":
                    conteudoHTML = conteudoHTML[:-6] + f"<li>{line[2:]}</li>\n</ul>\n"
                else:
                    conteudoHTML += f"<ul><li>{line[2:]}</li></ul>\n"
            elif code_exp.match(line):
                conteudoHTML += f"<code>{line[1:-2]}</code>\n"
            elif bar_exp.match(line):
                conteudoHTML += f"<hr>\n"
            elif title_exp.match(line):
                conteudoHTML += convert(line)
            elif image_exp.match(line):
                conteudoHTML += convert(line)
            else:
                conteudoHTML += f"<p>{line}</p>\n"

    html_file = os.path.splitext(md_file)[0] + ".html"
    with open(html_file, 'w') as html:
        html.write(preHTML + conteudoHTML + posHTML)
    return html_file

convert_md2html("teste.md")
