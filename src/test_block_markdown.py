import unittest 
from block_markdown import BlockType, block_to_block_type, extract_title, markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ]
            )

    def test_markdown_to_blocks_extra_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

    def test_only_newlines(self):
        md = "\n\n\n   \n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block_no_blank_lines(self):
        md = "Just a single paragraph\nwith a newline\nbut no blank lines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [md])

    def test_leading_trailing_blank_lines(self):
        md = """

First block

Second block

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    # Unittests for block_to_block_type

    def test_block_to_block_type(self):
        block = "just a regular old paragraph"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_block_heading(self):
        block = "## heading"
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_block_to_block_code(self):
        block = """
```
This is code
```"""
        self.assertEqual(BlockType.CODE , block_to_block_type(block))
        
    def test_block_to_block_ul(self):
        block = """
- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))
    
    def test_block_to_block_ol(self):
        block = """
1. This is the first list item in a list block
2. This is a list item
3. This is another list item
"""
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))
        
    def test_block_to_block_ol_2(self):
        block = """
1. This is the first list item in a list block
2. This is a list item
3. This is another list item
this is not another list item
"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_block_to_block_quote(self):
        block = """
> This is a quote.
> This is a quote.
"""
        self.assertEqual(BlockType.QUOTE , block_to_block_type(block))
        

    def test_extract_title(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

# title

- This is a list
- with items

"""
        self.assertEqual(extract_title(md), "title")

    def test_extract_title(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

## title

- This is a list
- with items

"""
        with self.assertRaises(Exception):
            extract_title(md), "title"

