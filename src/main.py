from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def main():
    text = TextNode("This is some anchor text", "link", "http://www.boot.dev")
    print(text)

def copy_contents():
    # TODO delete all contents of public dir

    # TODO copy all files and subdirectories from static to public



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
        

if __name__ == "__main__":
    main()
