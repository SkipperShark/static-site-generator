import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    
    def test_init_valid_no_url(self):
        node = TextNode("hello", TextType.BOLD)
        self.assertEqual(node.text, "hello")
        self.assertEqual(node.text_type.value, TextType.BOLD.value)
        self.assertIsNone(node.url)


    def test_init_valid_with_url(self):
        node = TextNode("hello", TextType.BOLD, "google.com")
        self.assertEqual(node.text, "hello")
        self.assertEqual(node.text_type.value, TextType.BOLD.value)
        self.assertEqual(node.url, "google.com")
    
    
    def test_init_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("a text node", "bold")
        with self.assertRaises(ValueError):
            TextNode("a text node", "italic")
            

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
        
        
    def test_inequality_text(self):
        node1 = TextNode("this is a text", TextType.TEXT)
        node2 = TextNode("this is texts", TextType.TEXT)
        self.assertNotEqual(node1, node2)


    def test_inequality_text_type(self):
        node1 = TextNode("this is a text", TextType.BOLD)
        node2 = TextNode("this is a text", TextType.TEXT)
        self.assertNotEqual(node1, node2)
        
        
    def test_inequality_url(self):
        node1 = TextNode("this is a text", TextType.TEXT, "google.com")
        node2 = TextNode("this is a text", TextType.TEXT, "yahoo.com")
        self.assertNotEqual(node1, node2)

        
    def test_repr(self):
        node = TextNode("test text", TextType.BOLD)
        self.assertEqual(repr(node),"TextNode(test text, bold)")

        node = TextNode("test text", TextType.BOLD, "google.com")
        self.assertEqual(repr(node),"TextNode(test text, bold, google.com)")


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