#Python Gems

This is a project that contains many small useful python programs.

##Programs

###Shell WolframAlpha

* Sehll WolframAlpha is a commandline based mathematical tool. Easy to use and no need to open browser. It provides full WolframAlpha functions, except graphs.
```
$ ./calc.py int_0^1sinxdx

[Definite integral]
    integral_0^1 sin(x) dx = 1-cos(1) ~~ 0.45970
[Riemann sums]
    left sum | (sin(1/2) sin((n-1)/(2 n)) csc(1/(2 n)))/n = 2 sin^2(1/2)-(sin(1/2) cos(1/2))/n+O((1/n)^2)
    (assuming subintervals of equal length)
[Indefinite integral]
    integral sin(x) dx = -cos(x)+constant
```
