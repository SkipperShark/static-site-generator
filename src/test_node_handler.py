import unittest
from textnode import TextType, TextNode
from node_handler import text_node_to_html_node, split_nodes_delimiter

TEST_TEXT_1 = "hello world"
TEST_TEXT_2 = "i am a mouse"
TEST_TEXT_3 = "my name is jerry"

class TestTextNodeToHTMLNode(unittest.TestCase):
    
    def test_text_node_to_html_node_text(self):
        text_node = TextNode(TEST_TEXT_1, TextType.TEXT)
        self.assertEqual(text_node_to_html_node(text_node).to_html(), TEST_TEXT_1)


    def test_text_node_to_html_node_bold(self):
        text_node = TextNode(TEST_TEXT_1, TextType.BOLD)
        desired = f"<b>{TEST_TEXT_1}</b>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_italic(self):
        text_node = TextNode(TEST_TEXT_1, TextType.ITALIC)
        desired = f"<i>{TEST_TEXT_1}</i>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_code(self):
        text_node = TextNode(TEST_TEXT_1, TextType.CODE)
        desired = f"<code>{TEST_TEXT_1}</code>"
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_empty(self):
        text_node = TextNode(TEST_TEXT_1, TextType.LINK)
        desired = f'<a href="">{TEST_TEXT_1}</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_link_not_empty(self):
        text_node = TextNode(TEST_TEXT_1, TextType.LINK, "google.com")
        desired = f'<a href="google.com">{TEST_TEXT_1}</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_image(self):
        text_node = TextNode(TEST_TEXT_1, TextType.IMAGE, "google.com")
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
        old_nodes = [
            TextNode(f"**{TEST_TEXT_1}**{TEST_TEXT_2}",TextType.TEXT)
        ]
        expected = [
            TextNode(TEST_TEXT_1, TextType.BOLD),
            TextNode(TEST_TEXT_2, TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)


    def test_1_inline_element_middle(self):
        old_nodes = [TextNode(
            f"{TEST_TEXT_1}**{TEST_TEXT_2}**{TEST_TEXT_3}",
            TextType.TEXT
        )]
        expected = [
            TextNode(TEST_TEXT_1, TextType.TEXT),
            TextNode(TEST_TEXT_2, TextType.BOLD),
            TextNode(TEST_TEXT_3, TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_1_inline_element_end(self):
        old_nodes = [TextNode(
            f"{TEST_TEXT_1}**{TEST_TEXT_2}**",
            TextType.TEXT
        )]
        expected = [
            TextNode(TEST_TEXT_1, TextType.TEXT),
            TextNode(TEST_TEXT_2, TextType.BOLD),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_2_inline_elements(self):
        old_nodes = [TextNode(
            f"{TEST_TEXT_1}**{TEST_TEXT_2}**{TEST_TEXT_3}**{TEST_TEXT_1}**{TEST_TEXT_2}",
            TextType.TEXT
        )]
        expected = [
            TextNode(TEST_TEXT_1, TextType.TEXT),
            TextNode(TEST_TEXT_2, TextType.BOLD),
            TextNode(TEST_TEXT_3, TextType.TEXT),
            TextNode(TEST_TEXT_1, TextType.BOLD),
            TextNode(TEST_TEXT_2, TextType.TEXT),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)