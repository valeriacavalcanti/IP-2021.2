Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10+2
12
>>> 14//4
3
>>> 14%4
2
>>> 14/4
3.5
>>> type(10)
<class 'int'>
>>> type(14)
<class 'int'>
>>> type(14//4)
<class 'int'>
>>> type(14/4)
<class 'float'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import sys
>>> sys.float_info.max
1.7976931348623157e+308
>>> float('inf')
inf
>>> type(sys.float_info.max)
<class 'float'>
>>> type(float('inf'))
<class 'float'>
>>> 
>>> 
>>> 
>>> 
>>> 'valeria'
'valeria'
>>> type('valeria')
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> type('123')
<class 'str'>
>>> type("12.34")
<class 'str'>
>>> 
>>> 
>>> 
>>> 'ifpb'*4
'ifpbifpbifpbifpb'
>>> 'ifpb'+'ifpb'
'ifpbifpb'
>>> 'ifpb'/4
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    'ifpb'/4
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 'ifpb'+2
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    'ifpb'+2
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> 
>>> 
>>> True
True
>>> true
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type('True')
<class 'str'>
>>> 'ramon"
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> 
>>> 
>>> 20 > 2
True
>>> type(20>2)
<class 'bool'>
>>> True and True
True
>>> 10 + 2 / 2
11.0
>>> (10+2)/2
6.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> not 2**3>10/2
False
>>> 
>>> 
>>> 
>>> 
>>> nome = "valéria"
>>> nome
'valéria'
>>> idade = 15
>>> idade
15
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'idade', 'nome', 'sys']
>>> nome
'valéria'
>>> idade
15
>>> nada = None
>>> type(nome)
<class 'str'>
>>> type(idade)
<class 'int'>
>>> 
>>> 
>>> 
>>> 
>>> teste = 10
>>> type(teste)
<class 'int'>
>>> teste = 20
>>> type(teste)
<class 'int'>
>>> teste = 12.2
>>> type(teste)
<class 'float'>
>>> teste = 'pode?'
>>> type(teste)
<class 'str'>
>>> teste = True
>>> type(teste)
<class 'bool'>
>>> 
>>> 
>>> idade = 15
>>> 