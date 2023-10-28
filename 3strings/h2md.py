# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    # TU CÓDIGO AQUÍ
    dict_start_html = {"<h1>": "</h1>",
                        "<h2>": "</h2>",
                          "<h3>": "</h3>"}
    for elem in dict_start_html:
        if html.startswith(elem) or html.endswith(dict_start_html[elem]):
            start = elem
            end = dict_start_html[elem]
            index_end = html.find(end)
            html = html[len(start):index_end]
            count_cat = "#" if start == "<h1>" else "##" if start == "<h2>" else '###'
            markdown = count_cat + " " + html
    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')