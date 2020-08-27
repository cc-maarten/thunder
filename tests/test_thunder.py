#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,sys,json
from subprocess import check_output
from os.path import basename
from os.path import dirname,realpath
from subprocess import check_output

sys.path.append(dirname(dirname(realpath(__file__))))


from thunder import indented_line, addline

import unittest
 
class TestEveAddline(unittest.TestCase):
    
    def test_indented_line_multiple(self):
        prev_line = "    {"
        new_line = "this is an indented line, nice\nthis is next line"
        result = indented_line(prev_line,new_line)
        expected = "    this is an indented line, nice\n    this is next line"
        self.assertEqual(result, expected)
    
    def test_indented_line(self):
        prev_line = "    {"
        new_line = "this is an indented line, nice"
        result = indented_line(prev_line,new_line)
        expected = "    this is an indented line, nice"
        self.assertEqual(result, expected)

    def test_addline_to_py_file(self):
        key = "pytest"
        input_file = "data/basic.py"
        template_file = "data/templates/pystuff.hb"
        
        args = [key,input_file,template_file]
        addline(args)
            
        input_file_starter = "data/starter_basic.py"
        expected_file_path = "data/expected_basic.py"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)


        self.assertEqual(result, expected)

    def test_addline_to_js_file(self):
        key = "jstest"
        input_file = "data/basic.js"
        template_file = "data/templates/jsstuff.hb"
        
        args = [key,input_file,template_file]
        addline(args)
            
        input_file_starter = "data/starter_basic.js"
        expected_file_path = "data/expected_basic.js"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)


        self.assertEqual(result, expected)
    
    def test_addline_to_html_file(self):
        key = "htmltest"
        input_file = "data/basic.html"
        template_file = "data/templates/htmlstuff.hb"
        
        args = [key,input_file,template_file]
        addline(args)
            
        input_file_starter = "data/starter_basic.html"
        expected_file_path = "data/expected_basic.html"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)


        self.assertEqual(result, expected)

    def test_addline_to_py_file_with_vars(self):
        key = "pytest"
        input_file = "data/basic.py"
        template_file = "data/templates/vars_pystuff.hb"
        keyval = "v4=var4&v5=var5&v6=var6"       

        args = [key,input_file,template_file,keyval]
        addline(args)
            
        input_file_starter = "data/starter_basic.py"
        expected_file_path = "data/expected_basic_with_vars.py"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)

        self.assertEqual(result, expected)

    def test_addline_to_js_file_with_vars(self):
        key = "jstest"
        input_file = "data/basic.js"
        template_file = "data/templates/vars_jsstuff.hb"
        keyval = "v2=var2&v3=var3"       

        args = [key,input_file,template_file,keyval]
        addline(args)
            
        input_file_starter = "data/starter_basic.js"
        expected_file_path = "data/expected_basic_with_vars.js"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)

        self.assertEqual(result, expected)


    def test_addline_to_html_file_with_vars(self):
        key = "htmltest"
        input_file = "data/basic.html"
        template_file = "data/templates/vars_htmlstuff.hb"
        keyval = "v1=var1"       

        args = [key,input_file,template_file,keyval]
        addline(args)
            
        input_file_starter = "data/starter_basic.html"
        expected_file_path = "data/expected_basic_with_vars.html"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)

        self.assertEqual(result, expected)

    def test_addline_to_html_file_with_vars_multiple_file(self):
        key = "htmltest"
        input_file = "data/basic.html"
        template_file = "data/templates/vars_htmlstuff.hb"
        keyval = "data/keyval/html.txt"       

        args = [key,input_file,template_file,keyval]
        addline(args)
            
        input_file_starter = "data/starter_basic.html"
        expected_file_path = "data/expected_basic_with_vars_multiple.html"
        result = ""
        expected = ""
        with open(input_file,'r') as f:
            result = f.read()
        
        with open(expected_file_path,'r') as f2:
            expected = f2.read()

        starter_content = ""
        with open(input_file_starter,'r') as f3:
            starter_content = f3.read()
        
        with open(input_file,'w') as f4:
            f4.write(starter_content)

        self.assertEqual(result, expected)

 
if __name__ == '__main__':
    unittest.main()

