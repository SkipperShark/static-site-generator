import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

TEST_TAG = "p"
TEST_VALUE = "hello world"
TEST_CHILDREN = []
TEST_PROPS_1 = {
    "href": "https://www.google.com", 
    "target": "_blank",
}
TEST_PROPS_2 = {
    "href": "https://www.google.com", 
}
TEST_PROPS_3 = {}

class TestHTMLNode(unittest.TestCase):
    
    def test_init(self):
        html_node = HTMLNode(TEST_TAG, TEST_VALUE, TEST_CHILDREN, TEST_PROPS_1)
        self.assertEqual(html_node.tag, TEST_TAG)
        self.assertEqual(html_node.value, TEST_VALUE)
        self.assertEqual(html_node.children, TEST_CHILDREN)
        self.assertEqual(html_node.props, TEST_PROPS_1)

    
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode().to_html()
    

    def test_props_to_html_no_props(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(), "")


    def test_props_to_html_with_2_props(self):
        self.assertEqual(
            HTMLNode(props = TEST_PROPS_1).props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )


    def test_props_to_html_with_1_prop(self):
        self.assertEqual(
            HTMLNode(props = TEST_PROPS_2).props_to_html(),
            ' href="https://www.google.com"'
        )
        
        
    def test_props_to_html_empty_dict(self):
        html_node = HTMLNode(props = TEST_PROPS_3)
        self.assertEqual(html_node.props_to_html(), "")

        
    def test_repr(self):
        html_node = HTMLNode(TEST_TAG, TEST_VALUE, TEST_CHILDREN, TEST_PROPS_1)
        self.assertEqual(
            str(html_node),
            (
                f"HTMLNode(tag={TEST_TAG}, value={TEST_VALUE}, "
                f'children={TEST_CHILDREN}, '
                f'props={TEST_PROPS_1})'
            )
        )


class TestLeafNode(unittest.TestCase):

    
    def test_init_valid(self):
        leaf_node = LeafNode(TEST_TAG, TEST_VALUE, TEST_PROPS_1)
        self.assertEqual(leaf_node.tag, TEST_TAG)
        self.assertEqual(leaf_node.value, TEST_VALUE)
        self.assertIsNone(leaf_node.children)
        self.assertEqual(leaf_node.props, TEST_PROPS_1)

        
    def test_init_invalid(self):
        with self.assertRaises(ValueError):
            LeafNode("tag", None)


    def test_init_tag_is_not_string(self):
        tag = 1
        leaf_node = LeafNode(tag, TEST_VALUE)
        self.assertEqual(leaf_node.to_html(), f"<1>{TEST_VALUE}</1>")


    def test_to_html_no_props(self):
        leaf_node = LeafNode(TEST_TAG, TEST_VALUE)
        desired = f"<{TEST_TAG}>{TEST_VALUE}</{TEST_TAG}>"
        self.assertEqual(leaf_node.to_html(), desired)


    def test_to_html_with_2_props(self):
        leaf_node = LeafNode("a", TEST_VALUE, TEST_PROPS_1)
        desired = f'<a href="https://www.google.com" target="_blank">{TEST_VALUE}</a>'
        self.assertEqual(leaf_node.to_html(), desired)


    def test_to_html_with_1_prop(self):
        leaf_node_2 = LeafNode("a", TEST_VALUE, TEST_PROPS_2)
        desired2 = f'<a href="https://www.google.com">{TEST_VALUE}</a>'
        self.assertEqual(leaf_node_2.to_html(), desired2)


    def test_to_html_no_tag(self):
        leaf_node = LeafNode(None, TEST_VALUE)
        self.assertEqual(leaf_node.to_html(), TEST_VALUE)
        
    
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


    # def test_to_html_no_children(self):
    #     node = ParentNode("p", None)
    #     with self.assertRaises(ValueError):
    #         self.assertEqual(node.to_html())


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