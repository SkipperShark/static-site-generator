import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    sample_text_1 = "hello"
    sample_text_2 = "hello world"
    sample_text_type_1 = TextType.TEXT
    sample_text_type_2 = TextType.BOLD
    sample_url_1 = "hello.com"
    sample_url_2 = "world.com"
    
    def test_init_valid_no_url(self):
        node = TextNode(self.sample_text_1, self.sample_text_type_1)
        self.assertEqual(node.text, self.sample_text_1)
        self.assertEqual(node.text_type, self.sample_text_type_1)
        self.assertIsNone(node.url)


    def test_init_valid_with_url(self):
        node = TextNode(
            self.sample_text_1, self.sample_text_type_1, self.sample_url_1
        )
        self.assertEqual(node.text, self.sample_text_1)
        self.assertEqual(node.text_type, self.sample_text_type_1)
        self.assertEqual(node.url, self.sample_url_1)
    
    
    def test_init_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode(self.sample_text_1, "kek")
        with self.assertRaises(ValueError):
            TextNode(self.sample_text_1, "for the horde!")
            

    def test_eq(self):
        node1 = TextNode(self.sample_text_1, self.sample_text_type_1)
        node2 = TextNode(self.sample_text_1, self.sample_text_type_1)
        self.assertEqual(node1, node2)
        
        
    def test_inequality_text(self):
        node1 = TextNode(self.sample_text_1, self.sample_text_type_1)
        node2 = TextNode(self.sample_text_2, self.sample_text_type_1)
        self.assertNotEqual(node1, node2)


    def test_inequality_text_type(self):
        node1 = TextNode(self.sample_text_1, self.sample_text_type_1)
        node2 = TextNode(self.sample_text_1, self.sample_text_type_2)
        self.assertNotEqual(node1, node2)
        
        
    def test_inequality_url(self):
        node1 = TextNode(
            self.sample_text_1, self.sample_text_type_1, self.sample_url_1
        )
        node2 = TextNode(
            self.sample_text_1, self.sample_text_type_1, self.sample_url_2
        )
        self.assertNotEqual(node1, node2)

        
    def test_repr_no_url(self):
        node = TextNode(self.sample_text_1, self.sample_text_type_1)
        self.assertEqual(repr(node),"TextNode(test text, bold)")


    def test_repr_with_url(self):
        node = TextNode(
            self.sample_text_1, self.sample_text_type_1, self.sample_url_1
        )
        self.assertEqual(
            repr(node),
            (
                f"TextNode({self.sample_text_1}, "
                f"{self.sample_text_type_1.value}, {self.sample_url_1})"
            )
        )


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