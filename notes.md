Text Node
example markdown "hello my name is *bob* and I like pie"
this would be

Text Node = "hello my name is ", type = text
Text Node = "bob", type = bold
Text Node = " and I like pie", type = text

HTML would be 

<p>
    hello my name is <b>bob</b> and I like pie
</p>

HTML node would be
HTMLNode(tag, value, children, props)

HTMLNode("p", None, None, [
    HTMLNode(None, "hello my name is ", [], None),
    HTMLNode("b", "bob ", [], None),
    HTMLNode(None, " and I like pie", [], None),
])


