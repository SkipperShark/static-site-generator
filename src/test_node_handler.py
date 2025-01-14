import unittest
from textnode import TextType, TextNode
from node_handler import text_node_to_html_node, split_nodes_delimiter

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


class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_empty_space_delimiter(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "", TextType.BOLD)
    
    
    def test_no_nodes(self):
        expected = []
        result = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(expected, result)
    
    
    def test_1_inline_element_start(self):
        old_nodes = [TextNode(
            "**bolded phrase** in the middle",
            TextType.TEXT
        )]
        expected = [
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)


    def test_1_inline_element_middle(self):
        old_nodes = [TextNode(
            "This is a text with a **bolded phrase** in the middle",
            TextType.TEXT
        )]
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_1_inline_element_end(self):
        old_nodes = [TextNode(
            "This is a text with a **bolded phrase**",
            TextType.TEXT
        )]
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_2_inline_elements(self):
        old_nodes = [TextNode(
            "This is a text with 2 **bolded phrases** in **one** sentence",
            TextType.TEXT
        )]
        expected = [
            TextNode("This is a text with 2 ", TextType.TEXT),
            TextNode("bolded phrases", TextType.BOLD),
            TextNode(" in ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" sentence", TextType.TEXT),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)