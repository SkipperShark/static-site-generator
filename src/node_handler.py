from textnode import TextType, TextNode

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

#* ""        
#* "a"
#* "**bolded phrase** at the start"
#* "a **bolded phrase** in the middle"
#* "at the end **bolded phrase**"
#* "incomplete **bolded phrase"

# test = ""
# print(split_node_text_by_delimiter(test, "**"))

# test = "a"
# print(split_node_text_by_delimiter(test, "**"))

# test = "**bolded phrase** at the start"
# print(split_node_text_by_delimiter(test, "**"))

# test = "a **bolded phrase** in the middle"
# print(split_node_text_by_delimiter(test, "**"))

# test = "at the end **bolded phrase**"
# print(split_node_text_by_delimiter(test, "**"))

# test = "two **bolded** words in **one** sentence"
# print(split_node_text_by_delimiter(test, "**"))

# test = "incomplete **bolded phrase"
# print(split_node_text_by_delimiter(test, "**"))
