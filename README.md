# Variables and Memory Samples

The various scope files show examples of different scopes

Real Python article: https://realpython.com/python-scope-legb-rule/

There are 4 scopes in python:
- function (local)
- enclosing
- global
- built-in

We only mention function and global in the reading. Additionally, python has no block scope, which can be useful to note for anyone who may have worked in a language that _does_ have block scope.

| Files | Description |
| --- | --- |
| scope_00.py | global and built-in |
| scope_01.py | accessing global var from a function |
| scope_02.py | optional; we can play around with errors brought on by trying to modify a  |global | var from wit|in a function |
| scope_03.py | local function variables |
| scope_04.py | shows enclosing scope (basically closure semantics) |