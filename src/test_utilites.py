import unittest

from utilites import extract_markdown_images, extract_markdown_links 
IMAGE_LINK_1 = "https://i.imgur.com/aKaOqIh.gif"
IMAGE_LINK_2 = "https://i.imgur.com/fJRm4Vk.jpeg"
LINK_1 = "https://www.boot.dev"
LINK_2 = "https://www.youtube.com/@bootdotdev"

class TestUtilities(unittest.TestCase):
    
    def test_extract_markdown_images_valid(self):
        text = (
            f"This is text with a ![rick roll]({IMAGE_LINK_1})"
            f"and ![obi wan]({IMAGE_LINK_2})"
        )
        expected = [
            ("rick roll", IMAGE_LINK_1),
            ("obi wan", IMAGE_LINK_2)
        ]
        result = extract_markdown_images(text)
        self.assertEqual(expected, result)


    def test_extract_markdown_images_invalid(self):
        text = (
            f"This is text with a ![rick roll]({IMAGE_LINK_1})"
            f"and ![obi wan]{IMAGE_LINK_2})"
        )
        expected = [
            ("rick roll", IMAGE_LINK_1)
        ]
        result = extract_markdown_images(text)
        self.assertEqual(expected, result)
        
        
    def test_extract_markdown_links_valid(self):
        text = (
            f"This is text with a link [to boot dev]({LINK_1}) and"
            f"[to youtube]({LINK_2})"
        )
        expected = [
            ("to boot dev", LINK_1),
            ("to youtube", LINK_2)
        ]
        result = extract_markdown_links(text)
        self.assertEqual(expected, result)


    def test_extract_markdown_links_invalid(self):
        text = (
            f"This is text with a link [to boot dev]({LINK_1} and"
            f"[to youtube]({LINK_2})"
        )
        expected = [
            ("to youtube", LINK_2)
        ]
        result = extract_markdown_links(text)
        self.assertEqual(expected, result)
    