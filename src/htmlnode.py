class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to HTML not yet implemented")

    def props_to_html(self):
        attribute_str = ""
        if self.props:
            for prop in self.props:
                attribute_str += f' {prop}="{self.props[prop]}"'
        return attribute_str

    def __repr__(self):
            return f"HTMLNode(tag: {self.tag}\n value: {self.value}\nchildren: {self.children}\nprops: {self.props})"

    def __eq__(self, other):
        if (
                self.tag == other.tag
                and self.value == other.value 
                and self.children == other.children 
                and self.props == other.props
                ):
            return True
        return False

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        if self.children is not None:
            raise ValueError("LeafNode cant have children")

    def to_html(self):

        # check that there is a value
        if self.value == None:
            raise ValueError("LeafNode needs a value")
        # if there is no tag return value as raw text
        if self.tag == None:
            return f"{self.value}"

        # turn the string, tag and eventual props into html a html-string and return it
        html_string = f"<{self.tag}"
        if self.props:
            for prop in self.props:
                html_string +=(f' {prop}="{self.props[prop]}"')
        html_string += (f">{self.value}</{self.tag}>")
        return html_string
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        # check that there isnt any tag and that there IS children
        if self.tag == None:
            raise ValueError("ParentNode needs a tag arg")
        if not self.children:
            raise ValueError("ParentNode needs child arg")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"



