import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        test_input = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        desired_output = ' href="https://www.google.com" target="_blank"'
        html_node = HTMLNode(props = test_input) 
        self.assertEqual(html_node.props_to_html(), desired_output)
        
        
    def test_props_to_html_no_props(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")
        
        
    def test_props_to_html_empty_dict(self):
        html_node = HTMLNode(props = {})
        self.assertEqual(html_node.props_to_html(), "")
        
        
    def test_props_to_html_one_key_value(self):
        desired = ' test="hello world"'
        html_node = HTMLNode(props = {"test": "hello world"})
        self.assertEqual(html_node.props_to_html(), desired)
        
    
    def test_repr(self):
        tag = "test tag"
        value = "test value"
        children = ["test child 1", "test child 2"]
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        desired = f"HTMLNode(tag={tag}, value={value}, children={children}, props={props})"
        html_node = HTMLNode(tag, value, children, props)
        self.assertEqual(str(html_node), desired)


class TestLeafNode(unittest.TestCase):
    
    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("tag", None)


    def test_with_value_with_tag(self):
        leaf_node_1 = LeafNode("p", "This is a paragraph of text.")
        desired1 = "<p>This is a paragraph of text.</p>"
        leaf_node_2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        desired2 = "<a>Click me!</a>"
        self.assertEqual(leaf_node_1.to_html(), desired1)
        self.assertEqual(leaf_node_2.to_html(), desired2)
        
    
    
    def test_with_value_no_tag(self):
        text = "My text"
        leaf_node = LeafNode(None, text)
        self.assertEqual(leaf_node.to_html(), text)
    
    
    def test_tag_is_not_string(self):
        tag = 1
        text = "My text"
        leaf_node = LeafNode(tag, text)
        self.assertEqual(leaf_node.to_html(), "<1>My text</1>")


class TestParentNode(unittest.TestCase):
    
    def test_to_html_children_only(self):
        desired = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), desired)


    def test_to_html_nested_parent(self):
        desired = "<p><p>test<b>hello</b></p>my name is bob</p>"
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "test"),
                        LeafNode("b", "hello")
                        
                    ]
                ),
                LeafNode(None, "my name is bob")
            ]
        )
        self.assertEqual(node.to_html(), desired)


    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            self.assertEqual(node.to_html())


    def test_to_html_nested_parent_only(self):
        desired = "<p><p>first line<b>test</b></p></p>"
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "first line"),
                        LeafNode("b", "test")
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), desired)
        
        
if __name__ == "__main__":
    unittest.main()