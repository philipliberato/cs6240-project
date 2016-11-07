"""Converts dot files to documents"""
from pprint import pprint

def handle_input():
    """Opens and returns file corresponding to filename arg."""
    filename = raw_input()
    dotfile = open(filename)
    lines = []
    for line in dotfile:
        formatted_line = line.rstrip('\r\n').lstrip('\t')
        if formatted_line[:4] == 'Node':
            lines.append(formatted_line)
    return lines

def parse_dotlines(dotlines):
    """Parse the given dot file lines into nodes."""
    nodes = dict()
    for line in dotlines:
        tokens = line.split()
        if tokens[0] in nodes.keys():
            nodes[tokens[0]].append(tokens[2])
        else:
            nodes[tokens[0]] = []
    pprint(nodes)

def main():
    """Gets input, parses dot files, and creates documents."""
    dotlines = handle_input()
    parse_dotlines(dotlines)

if __name__ == "__main__":
    main()
