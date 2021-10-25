# elfviz

elfviz is a command line interface tool to interact with ELF 
binary files.  

### installation

`click` and `pyelftools` are required installations.  

```
pip install click
pip install pyelftools
```

### usage

Options for the CLI can be seen by running `python3 elfviz.py --help`.  

```
(venv) elfviz % python3 elfviz.py --help
Usage: elfviz.py [OPTIONS] FILE COMMAND [ARGS]...

Options:
  --debug 
  --help           Show this message and exit.

Commands:
  all-sections
  section-header
  symbol-offset

```

A path to the file that should be examined is a required argument
for the main program.  

elfviz can be run with debugging when the `--debug` flag is passed as an OPTION.

Supported functionality can be seen under `Commands`. 

Furthermore, each sub-command has their own unique set of arguments and options.
These can be seen by running the command along with the `--help` tag.  

```
(venv) elfviz % python3 elfviz.py examples/hello section-header --help
Usage: elfviz.py FILE section-header [OPTIONS] SECTION

Options:
  --help  Show this message and exit.
```

### examples

Below, the `.got` section header details are obtained with the `section-header`
command.  

```
(venv) elfviz % python3 elfviz.py examples/hello section-header .got
sh_name:        231
sh_type:        SHT_PROGBITS
sh_flags:       3
sh_addr:        7048952
sh_offset:      757496
sh_size:        248
sh_link:        0
sh_info:        0
sh_addralign:   8
sh_entsize:     0
```

Getting a symbol offset in the file with a debugging level set:  

```
(venv) elfviz % python elfviz.py --debug examples/hello symbol-offset open
DEBUG:root:[!] symbol address: 0x448ae0
DEBUG:root:[!] symbol at section index 6
DEBUG:root:[!] symbol [ open ] in section: .plt
DEBUG:root:[!] section address: 0x400418
[+] offset: 297696
```

