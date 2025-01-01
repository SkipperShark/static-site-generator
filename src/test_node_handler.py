import unittest
from node_handler import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_empty_space_delimiter(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "", TextType.BOLD)
    
    
    def test_no_nodes(self):
        expected = []
        result = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(expected, result)
    
    
    def test_1_inline_element_start(self):
        old_nodes = TextNode(
            "**bolded phrase** in the middle",
            TextType.TEXT
        )
        expected = [
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)


    def test_1_inline_element_middle(self):
        old_nodes = TextNode(
            "This is text with a **bolded phrase** in the middle",
            TextType.TEXT
        )
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_1_inline_element_end(self):
        old_nodes = TextNode(
            "This is text with a **bolded phrase**",
            TextType.TEXT
        )
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
        ]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    
    def test_2_inline_elements(self):
        pass