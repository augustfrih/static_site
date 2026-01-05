import re
from textnode import TextNode, TextType 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    # iterate through the old nodes
    for node in old_nodes:
        # check that the node is text type, else append it to list and continue
        if node.text_type != TextType.TEXT or node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        if text.count(delimiter) % 2 != 0:
            raise Exception("textnode has an odd amount of delimiters")
        
        # split the text using the delimiter
        split_text = text.split(delimiter)
        
        # check if first textpart is delimiter
        new_text_type = False
        if text.startswith(delimiter):
            new_text_type = True

        # iterate through the text parts and append it to new_nodes
        for text_part in split_text:
            # if text_part.isspace(): //uncomment this if you dont want nodes that are only whitespace
            #     continue
            if new_text_type:
                new_nodes.append(TextNode(content=text_part, text_type=text_type))
            else:
                new_nodes.append(TextNode(content=text_part, text_type=TextType.TEXT))
            new_text_type = not new_text_type

    return new_nodes

#function that takes raw markdown, splits out images and returns it all as TextNodes
def split_nodes_images(old_nodes):

    new_nodes = []

    for node in old_nodes:
        # check that the node is text type, else append it to list and continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = dict(extract_markdown_images(text))
        if not images:
            new_nodes.append(node)
            continue

        split_text = []
        for image in images:
            tmp = text.split(f"![{image}]({images[image]})", 1)
            




    return new_nodes

                


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
