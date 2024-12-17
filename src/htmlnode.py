class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError()
    
    
    def props_to_html(self):
        output = ""
        if self.props is None:
            return output

        for (k,v) in self.props.items():
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
            raise ValueError("Must have value")

        super().__init__(tag, value, None, props)
        
        
    def to_html(self):
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
        
        
        
test = LeafNode("p", "This is a paragraph of text.")
test2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

print(test.to_html())
print(test2.to_html())