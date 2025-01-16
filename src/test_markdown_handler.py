import unittest
from markdown_handler import markdown_to_blocks

HEADING_BLOCK = "# This is a heading"
PARAGRAPH_BLOCK = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
LIST_BLOCK = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"

class TestMarkDownToBlocks(unittest.TestCase):
    
    def test_1_block_1_lines(self):
        self.assertEqual(
            markdown_to_blocks(HEADING_BLOCK),
            [HEADING_BLOCK]
        )
        
    
    def test_1_block_with_2_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_BLOCK}\n{HEADING_BLOCK}"),
            [f"{HEADING_BLOCK}\n{HEADING_BLOCK}"]
        )
        
        
    def test_2_blocks_each_with_1_line(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_BLOCK}\n\n{PARAGRAPH_BLOCK}"),
            [HEADING_BLOCK, PARAGRAPH_BLOCK]
        )
        
    
    def test_2_blocks_one_block_with_1_line_one_block_with_multiple_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_BLOCK}\n\n{LIST_BLOCK}"),
            [HEADING_BLOCK, LIST_BLOCK]
        )
        
        
    def test_2_blocks_both_with_multiple_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{LIST_BLOCK}\n\n{LIST_BLOCK}"),
            [LIST_BLOCK, LIST_BLOCK]
        )
        
        
    def test_3_blocks(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_BLOCK}\n\n{PARAGRAPH_BLOCK}\n\n{LIST_BLOCK}"),
            [HEADING_BLOCK, PARAGRAPH_BLOCK, LIST_BLOCK]
        )
        
    
    def test_2_blocks_with_3_blank_lines_between_them(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_BLOCK}\n\n\n\n{PARAGRAPH_BLOCK}"),
            [HEADING_BLOCK, PARAGRAPH_BLOCK]
        )