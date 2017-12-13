# pyc-test

+ env

```
$ python --version
Python 2.7.10
```

+ module test

```
$ python testModule.py
Hello
```

### script test python module

```
$ tree -a
.
├── .gitignore
├── importModule.py
├── readme.py
└── testModule.py

0 directories, 4 files
$ python importModule.py
Hello
$ tree -a
.
├── .gitignore
├── importModule.py
├── readme.py
├── testModule.py
└── testModule.pyc

0 directories, 5 files
```

