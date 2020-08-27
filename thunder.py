#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,sys,json
from subprocess import check_output
from os.path import basename

TAG="thunder"
if os.environ.get("THUNDER_TAG"):
    TAG = os.environ.get("THUNDER_TAG")

def usage():
        return "thunder.py [key] [input_file] [template_file] (optional: [keyval_data])"

"""
Add line(s) to file based on key, template_file & keyval_data
"""
def addline(vargs):
    args = vargs[1:]
    if len(args) < 3:
        print("usage: " + usage())
        exit(1)

    key = args[0]
    input_file = args[1]
    template_file = args[2]
    keyval_data = ''
    if len(args) > 3:
        keyval_data = args[3]

    if keyval_data != '' and os.path.isfile(keyval_data):
        with open(keyval_data,'r') as f:
            for keyvalline in f:
                #print("debug:keyvalline_multiple",keyvalline)
                #print("debug:key,input_file,template_file",key,input_file,template_file)
                editfile(key,input_file,template_file,keyvalline)
    else:
        editfile(key,input_file,template_file,keyval_data)

"""
Get dictionary of key val line (v1=var1&v2=var2&v3=var3)
"""
def getkeyval(keyvalline):
    keyval = {}
    if keyvalline != '':
        keyvalarr = keyvalline.split("&")
        for i in range(0,len(keyvalarr)):
            thekey = keyvalarr[i].split("=",1)[0].strip()
            val = keyvalarr[i].split("=",1)[1].strip()
            keyval[thekey]=val
    return keyval
    

"""
READ key, input_file, template_file, keyvalline (v1=var1&v2=var2) and 
WRITE changes to input_file
"""
def editfile(key,input_file,template_file,keyvalline):
    keyval = getkeyval(keyvalline)
    new_content = make_new_content(template_file,keyval)
    #print("debug:new_content",new_content)
    content = ""
    found = False
    with open(input_file,'r') as f:
        for line in f:
            content += line 
            if not found and is_comment_line(line,key):
                content += indented_line(line,new_content)
                found = True
    
    #print("debug:content_write",content)
    with open(input_file,'w') as f:
        f.write(content)
    
"""
Make indented line for eve
"""
def indented_line(prev_line, new_line):
    indented_line = new_line
    indents = len(prev_line) - len(prev_line.lstrip())
    if indents != 0:
    
        indent_spaces = ""
        
        for i in range(0,indents):
            indent_spaces += " "

        contents = []
        for line in indented_line.split(os.linesep):
            
            contents.append(indent_spaces + line)
    
        indented_line = os.linesep.join(contents)

    return indented_line


"""
Check if line contains eve comment
"""
def is_comment_line(line,key):
    jscomment = "/* "+TAG+":"+key+" */" in line
    htmlcomment = "<!-- "+TAG+":"+key+" -->" in line
    pythoncomment = '""" '+TAG+':'+key+' """' in line
    latexcomment = '% '+TAG+':'+key in line #untested
    return jscomment or htmlcomment or pythoncomment or latexcomment
        

"""
Make content to place in new line based on template_file & keyval_data
"""
def make_new_content(template_file,keyval):
    content = ""
    with open(template_file,'r') as f:
        content = f.read()

    for key,val in keyval.items():
        content = content.replace("{{"+key+"}}",val)
    
    return content

 
if __name__ == '__main__':
    addline(sys.argv)
