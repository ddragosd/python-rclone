# python-rclone
A Python wrapper for [rclone](https://rclone.org/).

## Status
Work in progress. Experimental.

## Usage

```python
from rclone import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).listremotes()

print(result.get('out'))  
# b'local:\n'
print(result.get('code')) 
# 0
```

###  Commands to be implemented:

* `copy`            Copy files from source to dest, skipping already copied
* `sync`            Make source and dest identical, modifying destination only.
* `listremotes`     List all the remotes in the config file.
* `ls`              List the objects in the path with size and path.
* `lsd`             List all directories/containers/buckets in the path.
* `lsf`             List directories and objects in remote:path formatted for parsing
* `lsjson`          List directories and objects in the path in JSON format.
* `lsl`             List the objects in path with modification time, size and path.