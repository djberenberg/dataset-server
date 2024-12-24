# dataset-server
A tiny, insecure client/server system for remote execution of `torch` datasets powered by ZeroMQ.

# install

To install, clone the repository, change directories inside and run:
```
pip install -e .
```

# running a server
An example script that serves data stored in a gzip-compressed `jsonl` file is provided in the `scripts` directory.

You can run it by
