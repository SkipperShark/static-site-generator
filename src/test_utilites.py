import unittest

from utilites import extract_markdown_images, extract_markdown_links 

class TestUtilities(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        result = extract_markdown_links(text)
        self.assertEqual(expected, result)
        
        
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        result = extract_markdown_links(text)
        self.assertEqual(expected, result)


    def test_extract_markdown_links_2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        result = extract_markdown_links(text)
        self.assertEqual(expected, result)
    