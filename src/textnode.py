from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"
    
    
class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        if text_type not in tuple(TextType):
            raise ValueError("Invalid text type")
        self.text_type = text_type
        self.url = url
        
    
    def __eq__(self, textNode):
        return (
            self.text == textNode.text
            and self.text_type == textNode.text_type
            and self.url == textNode.url
        )
            
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    
