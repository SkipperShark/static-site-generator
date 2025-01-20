from pprint import pp
from enum import Enum
import re

class MarkdownBlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown) -> list[str]:
    blocks = markdown.split("\n\n")
    return [block.strip.strip().strip("\n") for block in blocks if block != '']


def block_to_block_type(markdown_block: str) -> str:
    if re.match(r"^#{1,6} ", markdown_block):
        return MarkdownBlockTypes.HEADING
    elif markdown_block.startswith("```") and markdown_block.endswith("```"):
        return MarkdownBlockTypes.CODE
    elif markdown_block.startswith(">"):
        return MarkdownBlockTypes.QUOTE
    elif markdown_block.startswith("* ") or markdown_block.startswith("- "):
        return MarkdownBlockTypes.UNORDERED_LIST
    elif re.match(r"^\d*. ", markdown_block):
        return MarkdownBlockTypes.ORDERED_LIST

    return MarkdownBlockTypes.PARAGRAPH