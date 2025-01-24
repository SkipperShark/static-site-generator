import unittest
from generate_page import extract_title

HEADING_1_BLOCK = "# This is a heading1"
HEADING_1_BLOCK_2 = "# This is also a heading1"
HEADING_2_BLOCK = "## This is a heading2"

class TestExtractTitle(unittest.TestCase):
    
    def test_no_markdown(self):
        with self.assertRaises(Exception):
            extract_title("")
    
    def test_markdown_with_no_heading_block(self):
        with self.assertRaises(Exception):
            extract_title("hello my name is bob")
    
    
    def test_markdown_with_h2_heading_block(self):
        with self.assertRaises(Exception):
            extract_title(HEADING_2_BLOCK)
    
    
    def test_markdown_with_h1_block(self):
        self.assertEqual(extract_title(HEADING_1_BLOCK), "This is a heading1")
    
    
    def test_markdown_with_2_h1_blocks(self):
        self.assertEqual(
            extract_title(f"{HEADING_1_BLOCK}\n\n{HEADING_1_BLOCK_2}"),
            "This is a heading1"
        )