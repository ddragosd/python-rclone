# python-rclone
A Python wrapper for [rclone](https://rclone.org/).

`rclone` must be already installed and discoverable in `$PATH`. 

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
print(result.get('error'))
```

###  Implemented commands:

* `copy`            Copy files from source to dest, skipping already copied
* `sync`            Make source and dest identical, modifying destination only.
* `listremotes`     List all the remotes in the config file.
* `ls`              List the objects in the path with size and path.
* `lsjson`          List directories and objects in the path in JSON format.
* `delete`          Remove the contents of path.

Even if not all `rclone` commands have been exposed, it's possible to invoke any command using `run_cmd` method directly, as shown in the example bellow:

```python
from rclone import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).run_cmd(command="lsd", extra_args=["local:/tmp", "-v", "--dry-run"])
```

### Logging and Debugging

```python
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

from rclone import rclone

cfg = """[local]
type = local
nounc = true"""
result = rclone.with_config(cfg).listremotes()
```


