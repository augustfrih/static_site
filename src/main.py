from block_markdown import markdown_to_blocks
from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node


def main():
    text = TextNode("This is some anchor text", "link", "http://www.boot.dev")
    print(text)

def markdown_to_html_node(markdown):
    # split markdowns into blocks
    blocks = markdown_to_blocks(markdown)

    # iterate through the blocks
    for block in blocks:

        # Determine the type of block
        block_type = block_to_block_type(block)

        # create a new HTMLNode based on the block
        match block_type:
            case BlockType.PARAGRAPH:
                nodes = text_to_textnodes(text)
                pass
            case BlockType.HEADING:
                # TODO implement
                pass
            case BlockType.ORDERED_LIST:
                # TODO implement
                pass
            case BlockType.UNORDERED_LIST:
                # TODO implement
                pass
            case BlockType.QUOTE:
                # TODO implement
                pass
            case BlockType.CODE:
                # TODO implement
                pass
            case _:
                raise Exception("not a valid blocktype")


        # TODO: Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) 
        # function that works for all block types. It takes a string of text and returns a list of HTMLNodes that 
        # represent the inline markdown using previously created functions (think TextNode -> HTMLNode).


        # TODO: The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. 
        # I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.

    # TODO: make make all the block nodes under a single parent htmlnode which should just be div node and return it


def text_to_children(text):
    # create a list of htmlnodes
    nodes = text_to_htmlnodes(text)


    
    return ParentNode(TODO)

def text_to_htmlnodes(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

if __name__ == "__main__":
    main()
