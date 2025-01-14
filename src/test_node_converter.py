
import unittest

from textnode import TextNode, TextType
from node_converter import text_node_to_html_node

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

            