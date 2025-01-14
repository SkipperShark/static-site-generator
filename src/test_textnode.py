import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, text_node_to_html_node

TEST_TEXT_1 = "hello"
TEST_TEXT_2 = "hello world"
TEST_TEXT_TYPE_1 = TextType.TEXT
TEST_TEXT_TYPE_2 = TextType.BOLD
TEST_URL_1 = "hello.com"
TEST_URL_2 = "world.com"


class TestTextNode(unittest.TestCase):
    
    def test_init_valid_no_url(self):
        node = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        self.assertEqual(node.text, TEST_TEXT_1)
        self.assertEqual(node.text_type, TEST_TEXT_TYPE_1)
        self.assertIsNone(node.url)


    def test_init_valid_with_url(self):
        node = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1, TEST_URL_1)
        self.assertEqual(node.text, TEST_TEXT_1)
        self.assertEqual(node.text_type, TEST_TEXT_TYPE_1)
        self.assertEqual(node.url, TEST_URL_1)
    
    
    def test_init_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode(TEST_TEXT_1, "kek")
        with self.assertRaises(ValueError):
            TextNode(TEST_TEXT_1, "for the horde!")
            

    def test_eq(self):
        node1 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        node2 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        self.assertEqual(node1, node2)
        
        
    def test_inequality_text(self):
        node1 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        node2 = TextNode(TEST_TEXT_TYPE_2, TEST_TEXT_TYPE_1)
        self.assertNotEqual(node1, node2)


    def test_inequality_text_type(self):
        node1 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        node2 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_2)
        self.assertNotEqual(node1, node2)
        
        
    def test_inequality_url(self):
        node1 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1, TEST_URL_1)
        node2 = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1, TEST_URL_2)
        self.assertNotEqual(node1, node2)

        
    def test_repr_no_url(self):
        node = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1)
        self.assertEqual(repr(node), f"TextNode({TEST_TEXT_1}, {TEST_TEXT_TYPE_1.value})")


    def test_repr_with_url(self):
        node = TextNode(TEST_TEXT_1, TEST_TEXT_TYPE_1, TEST_URL_1)
        self.assertEqual(
            repr(node),
            (
                f"TextNode({TEST_TEXT_1}, "
                f"{TEST_TEXT_TYPE_1.value}, {TEST_URL_1})"
            )
        )
        
        
if __name__ == "__main__":
    unittest.main()