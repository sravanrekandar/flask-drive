# This function accepts a Markdown string and returns markdown string of ToC
import re


def generateToC(md_string, prefix):
    links_dictionary = {}
    lines = md_string.split("\n")
    heading_lines = []
    for line in lines:
        if len(line) > 0 and line[0] == "#" and ("#!/bin/bash" not in line):
            heading_lines.append(line)

    formatted_lines = []
    for line in heading_lines:
        level = line.index(" ")

        line_text = line[level + 1 :]
        link_text = line_text.strip().lower()
        link_text = line_text.replace(" ", "-")
        link_text = re.sub("[^a-zA-Z\\d\\s:-]", "", link_text)

        link_text = prefix + "#" + link_text

        # Handle duplicate names
        if link_text in links_dictionary:
            link_num = links_dictionary[link_text]
            links_dictionary[link_text] += 1
            link_text += str(link_num)
        else:
            links_dictionary[link_text] = 1

        line_link = "[{}]({})".format(line_text, link_text)
        left_pading = " " * ((level - 1) * 2)
        formatted_lines.append(f"{left_pading}- {line_link}")

    # print('\n'.join(formatted_lines))
    return "\n".join(formatted_lines)


def main():
    input_files = [
        {"file_name": "Chapter01.md", "prefix": "Chapter01.md"},
        {"file_name": "Chapter02.md", "prefix": "Chapter02.md"},
        {"file_name": "Chapter03.md", "prefix": "Chapter03.md"},
        {"file_name": "Chapter04.md", "prefix": "Chapter04.md"},
    ]

    markdowns = []
    for f in input_files:
        file = open(f["file_name"])
        md_string = file.read()
        markdowns.append(generateToC(md_string, f["prefix"]))

    print("\n".join(markdowns))


if __name__ == "__main__":
    main()
