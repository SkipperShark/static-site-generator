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
    
    