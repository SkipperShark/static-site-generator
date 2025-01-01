from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    if delimiter in ("", " "):
        raise ValueError("delimiter cant be empty space")
    
    if len(old_nodes) == 0:
        return result
    
    # pseudocode
    # if old_nodes is empty, return empty list
    # if old notes has 1 or more elements
    # iterate over old nodes
    # if old node is not a TEXT type text node, just add it to the result
    # if old node is a TEXT Type text node, split it according to supplied delimiter
    # if closing delimiter not found, raise exception saying that it's invalid markdown syntax
    # text within the delimiter should be text nodes of the TextType text_type parameter
    # text outside of the delimiter should be text nodes of TextType TEXT
    
    #todo after I split the text node of TextType TEXT into a list, how do i 
    #todo know, which elements of the list is the non-text element?
    #todo what if there are more than 1 inline element? 
    
    for node in old_nodes:
        if node.text_type != TextType.Text:
            result.append(node)
            continue
        


def split_node_text_by_delimiter(text, delimiter):
    # copy the string into a new var
    # while the string is not empty
    # find the index of the delimiter
    # get chars up to index of delimiter
    # if no chars, then delimiter is first word
        # find other delimitor
    result = []
    text_to_delimit = text
    
    while len(text_to_delimit) > 0:
        # print(f"")
        # print(f"result : {result}")
        # print(f"text_to_delimit : {text_to_delimit}")
        del_i_open = text_to_delimit.find(delimiter)
        # print(f"opening_delimiter_index : {del_i_open}")

        del_not_found = del_i_open == -1
        if del_not_found:
            result.append(text_to_delimit)
            break
            
        chars = text_to_delimit[0:del_i_open]
        # print(f"chars : {chars}")
        if len(chars) > 0:
            result.append(chars)
            text_to_delimit = text_to_delimit[del_i_open:]
            continue

        else:
            # check if closing delimitor is found
            text_to_delimit = text_to_delimit.lstrip(delimiter)
            closing_del_missing = text_to_delimit.find(delimiter) == -1
            if closing_del_missing:
                raise Exception("missing closing delimiter")
            
            phrases = text_to_delimit.split(delimiter)
            result.append(phrases[0])
            if len(phrases) > 0:
                text_to_delimit = phrases[1]
            continue

    return result

#* ""        
#* "a"
#* "**bolded phrase** at the start"
#* "a **bolded phrase** in the middle"
#* "at the end **bolded phrase**"
#* "incomplete **bolded phrase"

test = ""
print(split_node_text_by_delimiter(test, "**"))

test = "a"
print(split_node_text_by_delimiter(test, "**"))

test = "**bolded phrase** at the start"
print(split_node_text_by_delimiter(test, "**"))

test = "a **bolded phrase** in the middle"
print(split_node_text_by_delimiter(test, "**"))

test = "at the end **bolded phrase**"
print(split_node_text_by_delimiter(test, "**"))

test = "incomplete **bolded phrase"
print(split_node_text_by_delimiter(test, "**"))