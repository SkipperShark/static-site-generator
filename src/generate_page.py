from markdown_handler import (
    markdown_to_blocks,
    block_to_block_type,
    MarkdownBlockTypes,
    get_heading_level_of_heading_block
)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    heading_blocks = []
    for block in blocks:
        if block_to_block_type(block) == MarkdownBlockTypes.HEADING:
            heading_blocks.append(block)
            
    if len(heading_blocks) == 0:
        raise Exception("no heading blocks in markdown, can't extract title")
    
    for block in heading_blocks:
        if get_heading_level_of_heading_block(block) == 1:
            return block.strip("#").strip(" ")
        
    raise Exception("no h1 header in markdown, can't extract title")