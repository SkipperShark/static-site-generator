from pprint import pp

from textnode import TextType, TextNode
from htmlnode import LeafNode
from utilites import extract_markdown_images, extract_markdown_links, split_node_text_by_delimiter

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("text node is not the correct type")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props = {
                "src" : text_node.url,
                "alt" : text_node.text
            })
        case _:
            raise Expection("invalid text node text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    if delimiter in ("", " "):
        raise ValueError("delimiter cant be empty space")
    
    if len(old_nodes) == 0:
        return result
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        for ele in split_node_text_by_delimiter(node.text, delimiter):
            if ele["delimited"] == False:
                result.append(TextNode(ele["text"], TextType.TEXT))
            else:
                result.append(TextNode(ele["text"], text_type))
        
    return result


def split_nodes_link(old_nodes):
    result = []
    if len(old_nodes) == 0:
        return result
    
    class clsItem:
        def __init__(self, text, is_link, link_text=None, link_url=None):
            self.text = text
            self.is_link = is_link
            self.link_text = link_text
            self.link_url = link_url
    
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            result.append(node)
            continue

        node_text = str(node.text)
        items = []

        for link in links:
            link_text, link_url = link[0], link[1]
            link_md = f"[{link_text}]({link_url})"
            parts = node_text.partition(link_md)
            
            for i, part in enumerate(parts):
                match i:
                    case 0:
                        items.append(clsItem(part, False))
                    case 1:
                        items.append(clsItem(part, True, link_text, link_url))
                    case _:
                        pass
            
            node_text = parts[2]

        if len(node_text) > 0:
            items.append(clsItem(node_text, False))
        
        for item in items:
            if item.is_link:
                result.append(TextNode(item.link_text, TextType.LINK, item.link_url))
            else:
                if len(item.text) == 0:
                    continue
                result.append(TextNode(item.text, TextType.TEXT))

    print("-----")
    return result


def split_nodes_images(old_nodes):
    result = []
    if len(old_nodes) == 0:
        return result
    
    class clsItem:
        def __init__(self, text, is_link, link_text=None, link_url=None):
            self.text = text
            self.is_link = is_link
            self.link_text = link_text
            self.link_url = link_url
    
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            result.append(node)
            continue

        node_text = str(node.text)
        items = []

        for link in links:
            link_text, link_url = link[0], link[1]
            link_md = f"![{link_text}]({link_url})"
            parts = node_text.partition(link_md)
            
            for i, part in enumerate(parts):
                match i:
                    case 0:
                        items.append(clsItem(part, False))
                    case 1:
                        items.append(clsItem(part, True, link_text, link_url))
                    case _:
                        pass
            
            node_text = parts[2]

        if len(node_text) > 0:
            items.append(clsItem(node_text, False))
        
        for item in items:
            if item.is_link:
                result.append(TextNode(item.link_text, TextType.IMAGE, item.link_url))
            else:
                if len(item.text) == 0:
                    continue
                result.append(TextNode(item.text, TextType.TEXT))

    return result
    


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_link(nodes)
    return nodes