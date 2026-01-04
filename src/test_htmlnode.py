import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode(props="h", value="headertext")
        node2 = HTMLNode(props="h", value="headertext")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode(tag="cool", value="headertext")
        node2 = HTMLNode(props="h", value="headertext")
        self.assertNotEqual(node, node2)

    def test_props_to_html1(self):
        node = HTMLNode(tag="p", value="This is a paragraph of text", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual (node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual(
            "HTMLNode(tag: None\n value: None\nchildren: None\nprops: None)", repr(node)
        )


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag=None, value="coolbeans")
        node2 = LeafNode(tag=None, value="coolbeans")
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_mult(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "style": "color:tomato"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" style="color:tomato">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag=None, value="coolbeans")
        parent = ParentNode("div", [node])
        self.assertEqual(parent.to_html(), "<div>coolbeans</div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_with_props(self):
        node = LeafNode("p", "Hello, world!")
        parent = ParentNode("div", [node], {"href": "https://www.google.com", "style": "color:tomato"})
        self.assertEqual(parent.to_html(), '<div href="https://www.google.com" style="color:tomato"><p>Hello, world!</p></div>')

    # def test_leaf_to_html_a(self):
    #     node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
    #     self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent_to_html_mult(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "style": "color:tomato"})
        parent = ParentNode("div", [node])
        self.assertEqual(parent.to_html(), '<div><a href="https://www.google.com" style="color:tomato">Click me!</a></div>')

    def test_parent_no_tag_raises(self):
        child = LeafNode(None, "hi")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_nested_parents_with_props(self):
        inner = ParentNode("span", [LeafNode(None, "text")], {"class": "inner"})
        outer = ParentNode("div", [inner], {"id": "outer"})
        self.assertEqual(
            outer.to_html(),
            '<div id="outer"><span class="inner">text</span></div>',
        )

if __name__ == "__main__":
    unittest.main()
