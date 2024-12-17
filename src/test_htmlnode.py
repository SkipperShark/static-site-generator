import unittest

from htmlnode import HTMLNode

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

    
        
if __name__ == "__main__":
    unittest.main()