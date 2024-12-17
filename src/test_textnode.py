import unittest

from textnode import TextNode, TextType

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
    
        
if __name__ == "__main__":
    unittest.main()