

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
    if block.startswith("#"):
        max = 6
        if len(block) < max:
            max = len(block)
        for i in range(max):
            if block[i] == " ":
                return BlockType.HEADING
            if block[i] != "#":
                return BlockType.PARAGRAPH
        return BlockType.PARAGRAPH

    if block.startswith("´´´\n") and block.endswith("´´´"):
        return BlockType.CODE

    if block.startswith("> "):
        for i in range(len(block) - 2):
            if block[i] == "\n":
                if block[i + 1] != ">" or block[i + 2] != " ":
                    return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for i in range(len(block) - 2):
            if block[i] == "\n":
                if block[i + 1] != "-" or block[i + 2] != " ":
                    return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST


    if block.startswith("1. "):
        number = 1
        for i in range(len(block) - 3):
            if block[i] == "\n":
                if block[i + 1] != number or block[i + 2] != "." or block[i + 3] != " ":
                    return BlockType.PARAGRAPH
                number += 1
        return BlockType.UNORDERED_LIST
