from pprint import pp
from enum import Enum

class MarkdownBlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown) -> list[str]:
    print("----- markdown"), print(markdown)
    blocks = markdown.split("\n\n")
    print("----- blocks"), print(blocks)
    
    cleaned_blocks = [block.strip("\n") for block in blocks if block != '']
    print("----- cleaned blocks"), print(cleaned_blocks)
    return cleaned_blocks
    

def block_to_block_type(markdown_block) -> str:
