# Thunder
A simple Python tool to develop LIGHTNING fast! - Append code and build your code template library.


## Install
```
git clone REPO
```

## Usage
```
python thunder.py [key] [input_file] [template_file] (optional: [keyval_data])
```

## How it works:
1. Add "thunder tags" to areas of files you want append code to.
2. Create (a) file(s) with the data you want to append often.
3. Use thunder to add the data from those files to the marked areas.

### (1) How to use tags:
Thunder uses tags, because it needs to know where exactly to append lines. You can use the tags for the following filetype:


HTML:
```
<!-- thunder:TAG -->
```

JavaScript:
```
/* thunder:TAG */
```

Python:
```
""" thunder:TAG """
```

LaTeX:
```
% thunder:TAG
```


### Example usage:

##### Add data to file after thunder tag
sword@kate-pc thunder$ python thunder.py test1 ../thunder-manual-demo/test.html ../thunder-manual-demo/data.txt 
sword@kate-pc thunder$ cat ../thunder-manual-demo/test.html <!-- thunder:test1 -->
HI THIS IS AWESOME DATA OF {{name}}

##### Add data to file with variable after thunder tag
sword@kate-pc thunder$ python thunder.py test1 ../thunder-manual-demo/test.html ../thunder-manual-demo/data.txt name=nick
sword@kate-pc thunder$ cat ../thunder-manual-demo/test.html <!-- thunder:test1 -->
HI THIS IS AWESOME DATA OF nick
HI THIS IS AWESOME DATA OF {{name}}

##### Add data to file with multiple variables after thunder tag
sword@kate-pc thunder$ python thunder.py test1 ../thunder-manual-demo/test.html ../thunder-manual-demo/data.txt name=nick
sword@kate-pc thunder$ cat ../thunder-manual-demo/test.html <!-- thunder:test1 -->
HI THIS IS AWESOME DATA OF nick
HI THIS IS AWESOME DATA OF {{name}}

