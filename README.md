# Thunder: A simple Python tool to develop LIGHTNING fast! - Append code and build your massive code template library.

The idea is simple: coding is mostly appending and substracting lines of code. 

The thunder.py tool empowers you to easily append lines of code to specific areas of your project.

## Install
```
git clone https://github.com/learnermaarten/thunder
```

## Append code
### Usage
```
python thunder.py [thunder_tag] [input_file] [template_file] (optional: [keyval_data])
```

#### How it works:

1. Add "thunder tags" to specific areas of files you want append code to.
2. Create (a) file(s) with the data you want to append often.
3. Use thunder to add the data from those files to the marked areas.

##### Example usage:

###### Append lines to file from template
```
python thunder.py test1 demo/index.html demo-templates/madewithlove.html 
# Added line: <p>Made with <3</p>
```

###### Append lines to file from template with variable
```
python thunder.py test1 demo/index.html demo-templates/madewithlovewithvar.html name=Nick
# Added line: <p>Made with <3 by Nick</p>
```

###### Append lines to file from template with multiple variables
```
python thunder.py test1 demo/index.html demo-templates/madewithlovewithvars.html name=Nick&year=2020
# Added line: <p>Made with <3 by Nick in 2020</p>
```

##### Thunder tags
Thunder uses tags, because it needs to know where exactly you want to append lines. You can use the following tags for the following filetype:

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

##### Thunder variables
If you want to append lines from your templates and use variables you can use curly brackets ({{name}}).
Then when you execute thunder, use the third argument to set the value of a variable (var=value). If you want to use multiple variables use the & seperator (var1=value1&var2=value2), for example: 
```
python thunder.py test1 demo/index.html demo-templates/madewithlovewithvars.html name=Nick&year=2020
```

## Build your massive code template library
"" - quote compound interest

A few ideas to get started with your massive code template library:
- use a designated folder to store all your valuable code snippets
- make subfolders to organize your codebase
- use thunder.py in your own setup scripts
