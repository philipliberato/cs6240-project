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

def get_mapping(line):
    """Maps node value to its label."""
    node = line.split()[0]
    label = line.partition('{')[-1].rpartition('}')[0]
    return {node: label}

def parse_dotlines(dotlines):
    """Parse the given dot file lines into nodes and mappings."""
    mappings = dict()
    nodes = dict()
    for line in dotlines:
        tokens = line.split()
        if tokens[0] in nodes.keys():
            nodes[tokens[0]].append(tokens[2])
        else:
            mappings.update(get_mapping(line))
            nodes[tokens[0]] = []
    return mappings, nodes

def create_documents(mappings, nodes):
    """Converts nodes and mappings to a list of documents."""
    documents = dict()
    for key in nodes.keys():
        documents[mappings[key]] = []
        for val in nodes[key]:
            documents[mappings[key]].append(mappings[val[:-1]])
    formatted_documents = []
    for doc in documents:
        meta = '::' + doc.replace(' ', '_') + '::'
        body = ' '
        for doc_body in documents[doc]:
            body += doc_body + ' '
        formatted_documents.append(meta + body[:-1])
    return formatted_documents

def save_documents(documents):
    """Save the list of documents to a file on disk."""
    for doc in documents:
        print doc

def main():
    """Gets input, parses dot files, and creates documents."""
    dotlines = handle_input()
    mappings, nodes = parse_dotlines(dotlines)
    documents = create_documents(mappings, nodes)
    save_documents(documents)

if __name__ == "__main__":
    main()
