import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        
    def test_repr_with_url(self):
        text = "test text"
        text_type = TextType.BOLD
        url = "test url"
        node = TextNode(text, text_type, url)
        self.assertEqual(str(node),f"TextNode({text}, {text_type.value}, {url})")
    
    
    def test_repr_no_url(self):
        text, text_type= "test text", TextType.BOLD
        node = TextNode(text, text_type)
        self.assertEqual(str(node),f"TextNode({text}, {text_type.value}, {None})")
        self.assertEqual(node.url, None)
    
    
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("a text node", "bold")
        with self.assertRaises(ValueError):
            TextNode("a text node", "italic")
            


class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("hello world", TextType.TEXT)
        desired = "hello world"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("hello world", TextType.BOLD)
        desired = "<b>hello world</b>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("hello world", TextType.ITALIC)
        desired = "<i>hello world</i>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_code(self):
        text_node = TextNode("hello world", TextType.CODE)
        desired = "<code>hello world</code>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_empty(self):
        text_node = TextNode("hello world", TextType.LINK)
        desired = '<a href="">hello world</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_not_empty(self):
        text_node = TextNode("hello world", TextType.LINK, "google.com")
        desired = '<a href="google.com">hello world</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_image(self):
        text_node = TextNode("hello world", TextType.IMAGE, "google.com")
        desired = '<img src="google.com" alt=""></img>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)

            
if __name__ == "__main__":
    unittest.main()