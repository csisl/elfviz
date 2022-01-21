# notes

Link to man pages: http://manpages.ubuntu.com/manpages/xenial/man5/elf.5.html

## entry

An entry for a symbol contains the following information:

* name
* symbol type
* symbol binding attributes
* symbol visibility
* section header information
* value
* size

Sample information:
```
Container(
  {'st_name': 13818,
  'st_info': Container(
      {'bind': 'STB_WEAK', 'type': 'STT_FUNC'}
  ),
  'st_other': Container(
    {'visibility': 'STV_DEFAULT'}
  ),
  'st_shndx': 6,
  'st_value': 4492000,
  'st_size': 286})
```


## section header

We can get the section header by looping through the sections
with `elffile.iter_sections()` and obtaining a `Section` object.
The Section object has a header attribute where we can see the 
following:

```
Container(
  {'sh_name': 65,
  'sh_type': 'SHT_PROGBITS',
  'sh_flags': 6,
  'sh_addr': 4195352,
  'sh_offset': 1048,
  'sh_size': 184,
  'sh_link': 0,
  'sh_info': 0,
  'sh_addralign': 8,
  'sh_entsize': 0}
)
```