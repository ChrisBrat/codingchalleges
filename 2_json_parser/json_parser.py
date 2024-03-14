import re
from collections import deque

def valid_int(x):
    try:
        if x.isdigit() == False or (x.startswith("0") and x != "0"):
            return False                    
        int(x)  
        return True
    except Exception as e:                
        return False    

def valid_float(x):
    try:
        if x.startswith("0") and x.startswith("0.") == False and x!= "0":
            return False
        float(x)
        return True
    except Exception as e:        
        return False    
    
def valid_str(x):
    try:        
        result = (len(x) >= 2 and \
        '\n' not in str(x) and \
        '\t' not in str(x) and \
        x[0] == "\"" and \
        x[-1] == "\"")
        if result:
            for y in range(len(x)-1):
                if x[y] == "\\" and x[y+1] not in ["\\", "b","f","t","r","n","u","\"","/"]:
                    return False
        return result        
    except Exception as e:        
        return False      

valid_boolean = lambda x : x.lower() in ['true','false']

valid_brace_match = lambda x,y : (x == '{' and y == '}') or \
                                    (x == '[' and y == ']')

valid_non_duplicate = lambda x,y : x != y

valid_start_array = lambda x : str(x) not in ':,'
valid_array_item_value = lambda x : x in '[{' or \
                                            x == "null" or \
                                            valid_str(x) or \
                                            valid_boolean(x) or \
                                            valid_int(x) or \
                                            valid_float(x)    
valid_array_item = lambda x,y : (x == ',' and valid_array_item_value(y)) or \
                                (x != ',' and y in ",]" and valid_array_item_value(x))
valid_end_array = lambda x : x in ',}]' and x not in ':'

valid_start_object = lambda x : x not in ':,'
valid_object_key = lambda x : valid_str(x)
valid_object_value = lambda x : x in '[{' or \
                            x == "null" or \
                            len(str(x).strip()) == 0 or \
                            valid_str(x) or \
                            valid_boolean(x) or \
                            valid_int(x) or \
                            valid_float(x)
valid_end_object = lambda x : x in ',}]' and x not in ':'

def parse(contents):
    contents = contents.strip() if contents else ""
    if len(contents) == 0:
        return False
    
    content_tokens = []
    inText = False
    inNonText = False
    current_word_tokens = []
    i = 0
    while i < len(contents):
        x = contents[i]        

        if i < (len(contents) -1) and x == "\\" :
            if contents[i+1] in ["\"","\\","\b","\f","\n","\r","\t"]:                
                current_word_tokens.append(x)
                current_word_tokens.append(contents[i+1])
                i += 2
                continue

        if x == "\"" and not inNonText :
            inText = not inText            
        elif not inText :
            if x == ":":
                y = (contents[i+1:]) 
                if y.strip().startswith("\"") == False:
                    match = re.search(r"\{|\[|\,|\}", y)
                    if match and match.span()[0] > 0:
                        content_tokens.append(x)
                        word = contents[i+1:i+match.span()[1]]
                        i+= match.span()[0]+1
                        content_tokens.append(word.strip())
                        continue
            elif x == ",":
                y = (contents[i+1:]) 
                if (y.strip().startswith("\"") or \
                    y.strip().startswith("[") or \
                    y.strip().startswith("{")) == False:
                    match = re.search(r"\,|\]", y)
                    if match and match.span()[0] > 0:
                        content_tokens.append(x)
                        word = contents[i+1:i+match.span()[1]]
                        i+= match.span()[0]+1
                        content_tokens.append(word.strip())
                        continue

        current_word_tokens.append(x)
        if not inText and not inNonText:
            word = "".join(current_word_tokens)            
            if word not in ["\n",""," "]:                
                content_tokens.append(word.strip()) 
            current_word_tokens = []
        i+=1    
    
    stack = deque()
    valid = False
    for i,x in enumerate(content_tokens):

        if x in '[{' and x != '':
            stack.append(x)
        elif x in '}]' and x != '':
            startToken = stack.pop() 
            valid = valid_brace_match(startToken, x)

        if len(stack) == 0 and i+1 < len(content_tokens):
            return False
        elif len(stack) == 0:
            return valid  
        elif len(stack) == 20:
            return False
        
        if i+1 == len(content_tokens) and len(stack) > 0:            
            return False
        
        inArray = False        
        if stack[-1] == '[':
            inArray = True
        elif stack[-1] == '{':
            inArray = False
        valid = True            
        next = content_tokens[i+1]
        
        match x:
            case '[' : 
                valid = valid_start_array(next)
            case '{' : 
                valid = valid_start_object(next)
            case ']' : 
                valid = valid_end_array(next)
            case '}' : 
                valid = valid_end_object(next)
            case _ :
                if inArray:
                    valid = valid_array_item(x,next)
                else : 
                    if (content_tokens[i-1] in "{," and next == ":"):
                        valid = valid_object_key(x)
                    elif x == ':' :
                        valid = valid_object_value(next)
                    elif x == ',' :                        
                        valid = valid_object_key(next)
                    else :
                        valid = valid_object_value(x)
                if valid:    
                    valid = valid_non_duplicate(x,next)
        
        if not valid:
            return False
    return True    