import os
from pathlib import Path

from markdown_handler import (
    markdown_to_blocks,
    block_to_block_type,
    MarkdownBlockTypes,
    get_heading_level_of_heading_block,
    markdown_to_html_node
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


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md_f = open(from_path, "r")
    md_data = md_f.read()
    
    template_f = open(template_path, "r")
    template_data = template_f.read()
    
    html_node = markdown_to_html_node(md_data)
    content = html_node.to_html()
    
    title = extract_title(md_data)
    
    html = template_data.replace(r"{{ Title }}", title) \
        .replace(r"{{ Content }}", content)
        
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
        
    f = open(dest_path, "w")
    f.write(html)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    src = Path(dir_path_content)
    dst = Path(dest_dir_path)

    if src.is_file():
        generate_page(src, template_path, dst.with_suffix(".html"))
        return
    
    for path in src.iterdir():
        generate_page_recursive(
            dir_path_content = src / path.name,
            template_path = template_path,
            dest_dir_path = dst / path.name
        )