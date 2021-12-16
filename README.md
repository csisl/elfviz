# elfviz

elfviz is a command line interface tool to interact with ELF 
binary files.  

### installation

`click` and `pyelftools` are required installations.  

```
pip install click
pip install pyelftools
pip install ipython
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

### interactive

An interactive mode has been added to facilitate running multiple
commands on the ELF binary in one session. The main object to operate on
is called `elf`.

```
(venv) elfviz % python3 elfviz.py examples/hello interactive

In [1]: help(elf)


In [2]: elf.show_elf_header()
e_ident:        Container({'EI_MAG': [127, 69, 76, 70], 'EI_CLASS': 'ELFCLASS64', 'EI_DATA': 'ELFDATA2LSB', 'EI_VERSION': 'EV_CURRENT', 'EI_OSABI': 'ELFOSABI_LINUX', 'EI_ABIVERSION': 0})
e_type: ET_EXEC
e_machine:      EM_X86_64
e_version:      EV_CURRENT
e_entry:        4196944
e_phoff:        64
e_shoff:        845136
e_flags:        0
e_ehsize:       64
e_phentsize:    56
e_phnum:        6
e_shentsize:    64
e_shnum:        38
e_shstrndx:     37
```  

To see a full list of available methods use `dir(elf)` or `help(elf)`.  

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

