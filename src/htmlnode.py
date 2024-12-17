class HTMLNode:
    
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
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"