import re

def extract_markdown_images(text):
    result = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        return result
    
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result.extend(matches)
    return result


def extract_markdown_links(text):
    result = []
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        return result
    
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    result.extend(matches)
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