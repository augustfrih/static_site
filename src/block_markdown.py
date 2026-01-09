

from enum import Enum
import re


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
        max = 6
        if len(block) < max:
            max = len(block)
        for i in range(max):
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
