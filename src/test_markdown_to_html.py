
    # TODO: ceate unit tests

import unittest

from htmlnode import LeafNode, ParentNode
from block_markdown import markdown_to_html_node, text_to_children
from textnode import TextNode

class TestMarkdownToHTML(unittest.TestCase):
# Tests for text to html nodes
    def test_text_to_children(self):
        text = "This is another paragraph with _italic_ text and `code` here"
        child_nodes = [
                LeafNode(tag=None, value="This is another paragraph with "),
                LeafNode(tag="i", value="italic"),
                LeafNode(tag=None, value=" text and "),
                LeafNode(tag="code", value="code"),
                LeafNode(tag=None, value=" here"),
                ]
        self.assertEqual(
                text_to_children(text),
                child_nodes
                )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                )

    def test_ordered_list_paragraph(self):
        md = """
1. This is **bolded** paragraph
2. text in a p
3. tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ol><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ol><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_unordered_list_paragraph(self):
        md = """
- This is **bolded** paragraph
- text in a p
- tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ul><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_heading_to_html_node(self):
        md = "### third heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><h3>third heading</h3></div>"
                )
