
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

from enum import Enum



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            new_blocks.append(block)
    return new_blocks 

def block_to_block_type(block):
    block = block.strip()

    if block.startswith("#"):
        if len(block) < 6:
            top = len(block)
        else:
            top = 6

        for i in range(top):
            if block[i] == " ":
                return BlockType.HEADING
            if block[i] != "#":
                return BlockType.PARAGRAPH
        return BlockType.PARAGRAPH

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith("> "):
        newlines = block.split("\n")
        for line in newlines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        newlines = block.split("\n")
        for line in newlines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST


    if block.startswith("1. "):
        newlines = block.split("\n")
        for i in range(2, len(newlines) + 1):
            if not newlines[i - 1].startswith(f"{i}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    # split markdowns into blocks
    blocks = markdown_to_blocks(markdown)
    
    html_blocks = []

    # iterate through the blocks
    for block in blocks:

        # Determine the type of block
        block_type = block_to_block_type(block)

        # create a new HTMLNode based on the block
        match block_type:
            case BlockType.PARAGRAPH:
                paragraph = block_to_paragraph(block)
                children = text_to_children(paragraph)
                parentnode = ParentNode(tag="p", children=children)
            case BlockType.HEADING:
                h_num = 6
                for i in range(6):
                    if block[i] != "#":
                        h_num = i
                        break
                cleaned_block = block[h_num:].strip()
                children = text_to_children(cleaned_block)
                parentnode = ParentNode(tag=f"h{h_num}", children=children)
            case BlockType.ORDERED_LIST:
                lines = clean_up_list_block(block)
                list_items = []
                for line in lines:
                    children = text_to_children(line)
                    li = ParentNode(tag=f"li", children=children)
                    list_items.append(li)
                parentnode = ParentNode(tag="ol", children=list_items)
            case BlockType.UNORDERED_LIST:
                lines = clean_up_list_block(block)
                list_items = []
                for line in lines:
                    children = text_to_children(line)
                    li = ParentNode(tag=f"li", children=children)
                    list_items.append(li)
                parentnode = ParentNode(tag="ul", children=list_items)
            case BlockType.QUOTE:
                quote = clean_up_quote_block(block)
                children = text_to_children(quote)
                parentnode = ParentNode(tag="blockquote", children=children)
            case BlockType.CODE:
                content = clean_up_code_block(block)
                textnode = TextNode(content=content, text_type=TextType.CODE)
                parentnode = ParentNode(tag="pre", children=[text_node_to_html_node(textnode)])

        html_blocks.append(parentnode)

    return ParentNode(tag="div", children=html_blocks)


def text_to_children(text):
    # create a list of htmlnodes
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    
    return children

def block_to_paragraph(block):
    lines = block.split("\n")
    stripped_lines = [line.strip() for line in lines]
    paragraph = " ".join(stripped_lines)
    return paragraph

def clean_up_code_block(block):
    lines = block.split("\n")
    middle = lines[1:-1]
    paragraph = "\n".join(middle) + "\n"
    return paragraph

def clean_up_list_block(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.split(" ", 1)
        if len(cleaned_line) == 2:
            cleaned_lines.append(cleaned_line[1])
    return cleaned_lines

def clean_up_quote_block(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line[1:].lstrip)
    return " ".join(cleaned_lines)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            parts = line.split(" ", 1)
            if len(parts) == 2:
                heading = parts[1].strip
                return heading
    
    raise Exception("No heading found")
