import unittest
from markdown_handler import (
    markdown_to_blocks, block_to_block_type, MarkdownBlockTypes as mdBlockTypes
)

HEADING_1_BLOCK = "# This is a heading1"
HEADING_2_BLOCK = "## This is a heading2"
PARAGRAPH_BLOCK = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
UNORDERED_LIST_BLOCK_1 = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
UNORDERED_LIST_BLOCK_2 = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
CODE_BLOCK = "```i am a code block```"
CODE_BLOCK_INVALID = "```i am a code block"
QUOTE_BLOCK = ">I am a quote"
ORDERED_LIST_BLOCK_IN_ORDER = "1. First item\n2. 2nd item"
ORDERED_LIST_BLOCK_OUT_OF_ORDER = "1. First item\n3. 3RD item"

class TestMarkDownToBlocks(unittest.TestCase):
    
    def test_1_block_1_lines(self):
        self.assertEqual(
            markdown_to_blocks(HEADING_1_BLOCK),
            [HEADING_1_BLOCK]
        )
        
    
    def test_1_block_with_2_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_1_BLOCK}\n{HEADING_1_BLOCK}"),
            [f"{HEADING_1_BLOCK}\n{HEADING_1_BLOCK}"]
        )
        
        
    def test_2_blocks_each_with_1_line(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_1_BLOCK}\n\n{PARAGRAPH_BLOCK}"),
            [HEADING_1_BLOCK, PARAGRAPH_BLOCK]
        )
        
    
    def test_2_blocks_one_block_with_1_line_one_block_with_multiple_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_1_BLOCK}\n\n{UNORDERED_LIST_BLOCK_1}"),
            [HEADING_1_BLOCK, UNORDERED_LIST_BLOCK_1]
        )
        
        
    def test_2_blocks_both_with_multiple_lines(self):
        self.assertEqual(
            markdown_to_blocks(f"{UNORDERED_LIST_BLOCK_1}\n\n{UNORDERED_LIST_BLOCK_1}"),
            [UNORDERED_LIST_BLOCK_1, UNORDERED_LIST_BLOCK_1]
        )
        
        
    def test_3_blocks(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_1_BLOCK}\n\n{PARAGRAPH_BLOCK}\n\n{UNORDERED_LIST_BLOCK_1}"),
            [HEADING_1_BLOCK, PARAGRAPH_BLOCK, UNORDERED_LIST_BLOCK_1]
        )
        
    
    def test_2_blocks_with_3_blank_lines_between_them(self):
        self.assertEqual(
            markdown_to_blocks(f"{HEADING_1_BLOCK}\n\n\n\n{PARAGRAPH_BLOCK}"),
            [HEADING_1_BLOCK, PARAGRAPH_BLOCK]
        )
        

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading_1(self):
        self.assertEqual(
            block_to_block_type(HEADING_1_BLOCK), mdBlockTypes.HEADING
        )
        
        
    def test_heading_2(self):
        self.assertEqual(
            block_to_block_type(HEADING_2_BLOCK), mdBlockTypes.HEADING
        )


    def test_code_block_valid(self):
        self.assertEqual(
            block_to_block_type(CODE_BLOCK), mdBlockTypes.CODE
        )


    def test_code_block_invalid(self):
        self.assertEqual(
            block_to_block_type(CODE_BLOCK_INVALID),
            mdBlockTypes.PARAGRAPH
        )


    def test_quote_block(self):
        self.assertEqual(
            block_to_block_type(QUOTE_BLOCK), mdBlockTypes.QUOTE
        )
        

    def test_unordered_list_asterisk(self):
        self.assertEqual(
            block_to_block_type(UNORDERED_LIST_BLOCK_1),
            mdBlockTypes.UNORDERED_LIST
        )


    def test_unordered_list_dash(self):
        self.assertEqual(
            block_to_block_type(UNORDERED_LIST_BLOCK_2),
            mdBlockTypes.UNORDERED_LIST
        )
        
        
    def test_ordered_list_in_order(self):
        self.assertEqual(
            block_to_block_type(ORDERED_LIST_BLOCK_IN_ORDER),
            mdBlockTypes.ORDERED_LIST
        )
        
        
    def test_ordered_list_out_of_order(self):
        self.assertEqual(
            block_to_block_type(ORDERED_LIST_BLOCK_OUT_OF_ORDER),
            mdBlockTypes.ORDERED_LIST
        )
        
        
    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type(PARAGRAPH_BLOCK),
            mdBlockTypes.PARAGRAPH
        )
    