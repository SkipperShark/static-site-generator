
import unittest

from textnode import TextNode, TextType
from node_converter import text_node_to_html_node

TEST_TEXT = "hello world"

class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode(TEST_TEXT, TextType.TEXT)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), TEST_TEXT)


    def test_text_node_to_html_node_bold(self):
        text_node = TextNode(TEST_TEXT, TextType.BOLD)
        desired = f"<b>{TEST_TEXT}</b>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_italic(self):
        text_node = TextNode(TEST_TEXT, TextType.ITALIC)
        desired = f"<i>{TEST_TEXT}</i>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_code(self):
        text_node = TextNode(TEST_TEXT, TextType.CODE)
        desired = f"<code>{TEST_TEXT}</code>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_empty(self):
        text_node = TextNode(TEST_TEXT, TextType.LINK)
        desired = f'<a href="">{TEST_TEXT}</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_not_empty(self):
        text_node = TextNode(TEST_TEXT, TextType.LINK, "google.com")
        desired = f'<a href="google.com">{TEST_TEXT}</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_image(self):
        text_node = TextNode(TEST_TEXT, TextType.IMAGE, "google.com")
        desired = '<img src="google.com" alt=""></img>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)

            