from os.path import abspath

input_file = abspath("Chapter01.md")
prefix_file_name = "Chapter01.md"

# Read the file
file = open(input_file)
md_string = file.read()

# This function accepts a Markdown string and returns markdown string of ToC
def generateToC(md_string):
    lines = md_string.split("\n")
    heading_lines = []
    for line in lines:
        if len(line) > 0 and line[0] == "#":
            heading_lines.append(line)

    formatted_lines = []
    for line in heading_lines:
        level = line.index(" ")
        line_text = line[level + 1 :]
        link_text = prefix_file_name + "#" + line_text.replace(" ", "-").lower()

        line_link = "[{}]({})".format(line_text, link_text)
        lpad = " " * ((level - 1) * 2)
        last_line_level = level
        formatted_lines.append(f"{lpad}- {line_link}")

    print("\n".join(formatted_lines))


generateToC(md_string)