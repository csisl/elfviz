# elfviz

elfviz is a command line interface tool to interact with ELF 
binary files.  

### usage

Options for the CLI can be seen by running `python3 main.py --help`.  

```
(venv) elfviz % python3 main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  section-info
  symbol-offset
```

Obtaining section information, and the offset of a symbol in an
ELF file are supported.  

Furthermore, each sub-command has their own unique set of 
options. These options can be seen by running the command
along with the `--help` tag.  

```
(venv) elfviz % python3 main.py section-info --help                                 
Usage: main.py section-info [OPTIONS]

Options:
  --file TEXT
  --section TEXT
  --log TEXT
  --help          Show this message and exit.
```

A sample run to see where the symbol `open` resides in the 
file can be seen below:  

```
(venv) elfviz % python3 main.py symbol-offset --file examples/hello --symbol open
[+] offset: 297696
```

Debugging levels can be set with the `--log` parameter. 


