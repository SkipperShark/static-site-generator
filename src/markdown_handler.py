from pprint import pp
from enum import Enum
import re

from node_handler import text_to_textnodes, text_node_to_html_node
from htmlnode import ParentNode, LeafNode


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


def get_heading_level_of_heading_block(heading_block):
    match = re.match(r"^#{1,6} ", heading_block)
    if not match:
        return None

    result = match.group()
    h_level = result.count("#")
    if h_level > 6:
        return None

    return h_level


def text_to_html_nodes(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def paragraph_to_html_node(block):
    return ParentNode("p", text_to_html_nodes(block))


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1 :]
    return ParentNode(
        f"h{level}",
        text_to_html_nodes(text)
    )
    

def unordered_list_to_html_node(block: str):
    lines = [item.lstrip("* ") for item in block.split("\n")]
    li_elems = []
    for line in lines:
        li_elems.append(ParentNode("li", text_to_html_nodes(line)))
    
    return ParentNode("ul", li_elems)


def ordered_list_to_html_node(block):
    lines = block.split("\n")
    li_elems = []
    
    line: str
    for line in lines:
        text = line[line.index(". "):].lstrip(". ")
        li_elem = ParentNode("li", text_to_html_nodes(text))
        li_elems.append(li_elem)
        
    return ParentNode("ol", li_elems)


def quote_to_html_node(block: str):
    lines = block.split("\n")
    lines = [line.lstrip(">").lstrip(" ") for line in lines]
    text = " ".join(lines)
    return ParentNode("blockquote", text_to_html_nodes(text))


def code_to_html_node(block: str):
    text = block.lstrip("```").rstrip("```")
    return ParentNode(
        "code",
        [
            ParentNode("pre", text_to_html_nodes(text))
        ]
    )
    

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == MarkdownBlockTypes.HEADING:
            children.append(heading_to_html_node(block))
            
        elif block_type == MarkdownBlockTypes.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
            
        elif block_type == MarkdownBlockTypes.UNORDERED_LIST:
            children.append(unordered_list_to_html_node(block))
        
        elif block_type == MarkdownBlockTypes.ORDERED_LIST:
            children.append(ordered_list_to_html_node(block))
            
        elif block_type == MarkdownBlockTypes.QUOTE:
            children.append(quote_to_html_node(block))
        
        elif block_type == MarkdownBlockTypes.CODE:
            text = block.lstrip("```").rstrip("```")
            html_elem = ParentNode(
                "code",
                [LeafNode("pre", text)]
            )
            children.append(html_elem)
                
    return ParentNode("div", children)

# f = open("sample_md.md", "r+")
# pp(markdown_to_html_node(f.read()))
test1 = markdown_to_html_node("```i am a code block```")
test2 = ParentNode(
    "div",
    [
        ParentNode(
            "code",
            [LeafNode("pre", "i am a code block")]
        )
    ]
)
print(test1)
print(test2)
print(test1 == test2)
print(str(test1) == str(test2))

