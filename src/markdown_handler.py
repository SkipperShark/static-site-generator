from pprint import pp
# 2 new lines = blank link = new block
# 1 new line = continuation of block
# f = open("sample_md.md", "r")
# pp(f.readlines())
# pp(f.read())

def markdown_to_blocks(markdown):
    print("----- markdown"), print(markdown)
    blocks = markdown.split("\n\n")
    print("----- blocks"), print(blocks)
    
    cleaned_blocks = [block.strip("\n") for block in blocks if block != '']
    print("----- cleaned blocks"), print(cleaned_blocks)
    return cleaned_blocks
    

# print(markdown_to_blocks(f.read()))

