
    # TODO: ceate unit tests

import unittest

from htmlnode import LeafNode, ParentNode
from main import text_to_htmlnodes
from markdown_to_html import markdown_to_html_node
from textnode import TextNode

class TestMarkdownToHTML(unittest.TestCase):
# Tests for text to html nodes
    def test_text_to_html(self):
        text = """  
This is another paragraph with _italic_ text and `code` here

""" 
        child_nodes = [
                LeafNode(tag
                ]
        html_node = ParentNode(tag="p", children=child_nodes)
        self.assertEqual(
                text_to_htmlnodes(text),
                html_node
                )

# test the final product TODO implement more tests
#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here
#
# This is another paragraph with _italic_ text and `code` here
#
# """
#
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#                 html,
#                 "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#                 )
#     def test_codeblock(self):
#         md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
#
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#                 html,
#                 "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#                 )
