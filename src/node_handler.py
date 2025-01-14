from textnode import TextType, TextNode
from htmlnode import LeafNode

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
            props = {
                "src" : text_node.url,
                "alt" : ""
            }
            return LeafNode("img", "", props)
        case _:
            raise Expection("invalid text node text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    if delimiter in ("", " "):
        raise ValueError("delimiter cant be empty space")
    
    if len(old_nodes) == 0:
        return result
    
    def split_node_text_by_delimiter(text, delimiter):
        result = []
        text_to_delimit = text
        
        while len(text_to_delimit) > 0:
            delim_i_open = text_to_delimit.find(delimiter)
            delim_not_found = delim_i_open == -1
            if delim_not_found:
                result.append({
                    "text" : text_to_delimit,
                    "delimited" : False
                })
                break
                
            chars = text_to_delimit[0:delim_i_open]
            if len(chars) > 0:
                result.append({
                    "text" : chars,
                    "delimited" : False
                })
                text_to_delimit = text_to_delimit[delim_i_open:]
                continue

            else:
                text_to_delimit = text_to_delimit.lstrip(delimiter)
                delim_i_close = text_to_delimit.find(delimiter)
                if delim_i_close == -1:
                    raise Exception("missing closing delimiter")
                
                delimited_phrase = text_to_delimit[0:delim_i_close]
                result.append({
                    "text" : delimited_phrase,
                    "delimited" : True
                })
                text_to_delimit = text_to_delimit[delim_i_close+len(delimiter):]
                continue

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
