from pprint import pp
from enum import Enum
import re

from node_handler import text_to_textnode, text_node_to_html_node

class MarkdownBlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip().strip("\n") for block in blocks if block != '']


def block_to_block_type(block: str):
    lines = block.split("\n")
    if re.match(r"^#{1,6} ", block):
        return MarkdownBlockTypes.HEADING

    elif block.startswith("```") and block.endswith("```"):
        return MarkdownBlockTypes.CODE

    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return MarkdownBlockTypes.PARAGRAPH
            continue
        return MarkdownBlockTypes.QUOTE

    elif block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                return MarkdownBlockTypes.PARAGRAPH
            continue
        return MarkdownBlockTypes.UNORDERED_LIST


    elif re.match(r"^\d*. ", block):
        for line in lines:
            if not re.match(r"^\d*. ", block):
                return MarkdownBlockTypes.PARAGRAPH
            continue
        return MarkdownBlockTypes.ORDERED_LIST

    return MarkdownBlockTypes.PARAGRAPH

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    print("block")
    print(blocks)

    for block in blocks:
        print("\n--------------- new iteration of block")
        print("block")
        print(block)
        block_type = block_to_block_type(block)
        print(f"block type : {block_type}")
        
        if block_type == MarkdownBlockTypes.PARAGRAPH:
            text_nodes = text_to_textnode(block)
            print("text nodes")
            print(text_nodes)
            
            
    return

f = open("sample_md.md", "r+")
print(markdown_to_html_node(f.read()))


    # split the markdown into blocks
    # for each block
    # determine the type of block
    # split the text of the block into text nodes using (text_to_textnode)
    # for each textnode, convert them into leaf nodes
    # depending on the type of block, create the appropriate parent html node
    # then, put all the leaf nodes as children of the parent html node
    
    # all blocks should be under a parent html node (which is a div)
    
    #Split the markdown into blocks (you already have a function for this)
    #Loop over each block:
    #Determine the type of block (you already have a function for this)
    #Based on the type of block, create a new HTMLNode with the proper data
    #Assign the proper child HTMLNode objects to the block node. I created a
    # shared text_to_children(text) function that works for all block types.
    # It takes a string of text and returns a list of HTMLNodes that represent
    # the inline markdown using previously created functions
    # (think TextNode -> HTMLNode).
    #Make all the block nodes children under a single parent HTML node
    # (which should just be a div) and return it.