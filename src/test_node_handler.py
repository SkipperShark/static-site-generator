import unittest
from textnode import TextType, TextNode
from node_handler import (
    text_node_to_html_node,
    split_nodes_delimiter,
    split_nodes_link,
    split_nodes_images,
    text_to_textnodes
)

TEST_TEXT_1 = "hello world"
TEST_TEXT_2 = "i am a mouse"
TEST_TEXT_3 = "my name is jerry"
TEST_LINK_1 = "to boot dev"
TEST_URL_1 = "https://www.boot.dev"
TEST_LINK_2 = "to youtube"
TEST_URL_2 = "https://www.youtube.com/@bootdotdev"

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
        text_node = TextNode(TEST_TEXT_1, TextType.LINK, TEST_URL_1)
        desired = f'<a href="{TEST_URL_1}">{TEST_TEXT_1}</a>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


    def test_text_node_to_html_node_image(self):
        text_node = TextNode(TEST_TEXT_1, TextType.IMAGE, TEST_URL_1)
        desired = f'<img src="{TEST_URL_1}" alt="{TEST_TEXT_1}"></img>'
        self.assertEqual(text_node_to_html_node(text_node).to_html(), desired)


class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_empty_space_delimiter(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "", TextType.BOLD)
    
    
    def test_no_nodes(self):
        expected = []
        result = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(expected, result)
    
    
    def test_1_inline_element_invalid_syntax(self):
        with self.assertRaises(Exception):
            old_nodes = [
                TextNode(f"**{TEST_TEXT_1}{TEST_TEXT_2}",TextType.TEXT)
            ]
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)


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
        

    def test_delim_bold_and_italic(self):
        node = TextNode(f"**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
        

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
        
        
class TestSplitNodesLink(unittest.TestCase):
    
    def test_no_nodes(self):
        self.assertEqual(split_nodes_link([]), [])
        
        
    def test_text_no_links(self):
        node1 = TextNode(f"{TEST_TEXT_1}", TextType.TEXT)
        node2 = TextNode(f"{TEST_TEXT_2}", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node1, node2]),
            [
                TextNode(f"{TEST_TEXT_1}", TextType.TEXT),
                TextNode(f"{TEST_TEXT_2}", TextType.TEXT),
            ]
        )
        
        
    def test_text_with_1_valid_link(self):
        node = TextNode(
            f"{TEST_TEXT_1}[{TEST_LINK_1}]({TEST_URL_1})",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1),
            ]
        )
        
    
    def test_text_with_2_valid_links(self):
        node = TextNode(
            (
                f"{TEST_TEXT_1}[{TEST_LINK_1}]({TEST_URL_1})"
                f"{TEST_TEXT_2}[{TEST_LINK_2}]({TEST_URL_2})"
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1),
                TextNode(TEST_TEXT_2, TextType.TEXT),
                TextNode(TEST_LINK_2, TextType.LINK, TEST_URL_2),
            ]
        )


    def test_text_with_1_valid_link_and_1_invalid_link(self):
        invalid_link_with_text = f"{TEST_TEXT_2}[{TEST_LINK_2}]({TEST_URL_2}"
        node = TextNode(
            (
                f"{TEST_TEXT_1}[{TEST_LINK_1}]({TEST_URL_1})" +
                invalid_link_with_text
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1),
                TextNode(invalid_link_with_text, TextType.TEXT),
            ]
        )
        
        
    
    def test_text_with_1_invalid_link(self):
        invalid = f"{TEST_TEXT_1}[{TEST_LINK_1}]({TEST_URL_1}{TEST_TEXT_2}"
        node = TextNode(invalid, TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(invalid, TextType.TEXT),
            ]
        )
        
        
    def test_just_1_valid_link(self):
        node = TextNode(f"[{TEST_LINK_1}]({TEST_URL_1})", TextType.TEXT)
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1)
            ]
        )

        
    def test_just_2_valid_links(self):
        node = TextNode(
            (
                f"[{TEST_LINK_1}]({TEST_URL_1})"
                f"[{TEST_LINK_2}]({TEST_URL_2})"
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1),
                TextNode(TEST_LINK_2, TextType.LINK, TEST_URL_2)
            ]
        )


    def test_just_1_invalid_link_and_1_valid_link(self):
        node = TextNode(
            (
                f"[{TEST_LINK_1}]({TEST_URL_1})"
                f"[{TEST_LINK_2}]({TEST_URL_2}"
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_link([node]),
            [
                TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1),
                TextNode(f"[{TEST_LINK_2}]({TEST_URL_2}", TextType.TEXT)
            ]
        )
        

class TestSplitNodesImages(unittest.TestCase):
    
    def test_no_nodes(self):
        self.assertEqual(split_nodes_images([]), [])
        
        
    def test_text_no_images(self):
        node1 = TextNode(f"{TEST_TEXT_1}", TextType.TEXT)
        node2 = TextNode(f"{TEST_TEXT_2}", TextType.TEXT)
        self.assertEqual(
            split_nodes_images([node1, node2]),
            [
                TextNode(f"{TEST_TEXT_1}", TextType.TEXT),
                TextNode(f"{TEST_TEXT_2}", TextType.TEXT),
            ]
        )
        
        
    def test_text_with_1_valid_image(self):
        node = TextNode(
            f"{TEST_TEXT_1}![{TEST_LINK_1}]({TEST_URL_1})",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
            ]
        )
        
    
    def test_text_with_2_valid_images(self):
        node = TextNode(
            (
                f"{TEST_TEXT_1}![{TEST_LINK_1}]({TEST_URL_1})"
                f"{TEST_TEXT_2}![{TEST_LINK_2}]({TEST_URL_2})"
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
                TextNode(TEST_TEXT_2, TextType.TEXT),
                TextNode(TEST_LINK_2, TextType.IMAGE, TEST_URL_2),
            ]
        )


    def test_text_with_1_valid_image_and_1_invalid_image(self):
        invalid_link_with_text = f"{TEST_TEXT_2}[{TEST_LINK_2}]({TEST_URL_2})"
        node = TextNode(
            (
                f"{TEST_TEXT_1}![{TEST_LINK_1}]({TEST_URL_1})" +
                invalid_link_with_text
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
                TextNode(invalid_link_with_text, TextType.TEXT),
            ]
        )
        
        
    
    def test_text_with_1_invalid_image(self):
        invalid = f"{TEST_TEXT_1}![{TEST_LINK_1}]({TEST_URL_1}{TEST_TEXT_2}"
        node = TextNode(invalid, TextType.TEXT)
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(invalid, TextType.TEXT),
            ]
        )
        
        
    def test_just_1_valid_image(self):
        node = TextNode(f"![{TEST_LINK_1}]({TEST_URL_1})", TextType.TEXT)
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1)
            ]
        )

        
    def test_just_2_valid_images(self):
        node = TextNode(
            (
                f"![{TEST_LINK_1}]({TEST_URL_1})"
                f"![{TEST_LINK_2}]({TEST_URL_2})"
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
                TextNode(TEST_LINK_2, TextType.IMAGE, TEST_URL_2)
            ]
        )


    def test_just_1_invalid_image_and_1_valid_image(self):
        invalid_image_md = f"[{TEST_LINK_2}]({TEST_URL_2})"
        node = TextNode(
            (
                f"![{TEST_LINK_1}]({TEST_URL_1})"
                + invalid_image_md
            ),
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_images([node]),
            [
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
                TextNode(invalid_image_md, TextType.TEXT)
            ]
        )


class TestTextToTextNodes(unittest.TestCase):
    
    def test_text_only(self):
        self.assertEqual(
            text_to_textnodes(TEST_TEXT_1),
            [TextNode(TEST_TEXT_1, TextType.TEXT)]
        )
        
        
    def test_bold_only(self):
        self.assertEqual(
            text_to_textnodes(f"**{TEST_TEXT_1}**"),
            [TextNode(TEST_TEXT_1, TextType.BOLD)]
        )
    
    
    def test_italic_only(self):
        self.assertEqual(
            text_to_textnodes(f"*{TEST_TEXT_1}*"),
            [TextNode(TEST_TEXT_1, TextType.ITALIC)]
        )


    def test_code_only(self):
        self.assertEqual(
            text_to_textnodes(f"`{TEST_TEXT_1}`"),
            [TextNode(TEST_TEXT_1, TextType.CODE)]
        )


    def test_image_only(self):
        self.assertEqual(
            text_to_textnodes(f"![{TEST_LINK_1}]({TEST_URL_1})"),
            [TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1)]
        )


    def test_link_only(self):
        self.assertEqual(
            text_to_textnodes(f"[{TEST_LINK_1}]({TEST_URL_1})"),
            [TextNode(TEST_LINK_1, TextType.LINK, TEST_URL_1)]
        )


    def test_all(self):
        text = (
            f"{TEST_TEXT_1}**{TEST_TEXT_2}**{TEST_TEXT_3}*{TEST_TEXT_1}*"
            f"{TEST_TEXT_2}`{TEST_TEXT_3}`{TEST_TEXT_1}"
            f"![{TEST_LINK_1}]({TEST_URL_1})"
            f"[{TEST_LINK_2}]({TEST_URL_2})"
        )
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_TEXT_2, TextType.BOLD),
                TextNode(TEST_TEXT_3, TextType.TEXT),
                TextNode(TEST_TEXT_1, TextType.ITALIC),
                TextNode(TEST_TEXT_2, TextType.TEXT),
                TextNode(TEST_TEXT_3, TextType.CODE),
                TextNode(TEST_TEXT_1, TextType.TEXT),
                TextNode(TEST_LINK_1, TextType.IMAGE, TEST_URL_1),
                TextNode(TEST_LINK_2, TextType.LINK, TEST_URL_2)
            ]
        )