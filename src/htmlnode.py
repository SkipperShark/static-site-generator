from textnode import TextNode, TextType

class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    
    def props_to_html(self):
        output = ""
        if self.props is None:
            return output

        for (k,v) in self.props.items():
            if v is None:
                v = ""
            output += f' {k}="{v}"'
        return output
    
    
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag}, value={self.value}, "
            f"children={self.children}, props={self.props})"
        )
        
        
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("Tag must not be None")

        super().__init__(tag, value, None, props)
        
        
    def to_html(self):
        # raw text without html tag
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
        
    def __eq__(self, LeafNode):
        return str(LeafNode) == str(self)
        

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must not be None")
        if self.children is None:
            raise ValueError("Children must not be None")
        
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
    
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    
    def __eq__(self, ParentNode):
        return str(ParentNode) == str(self)

