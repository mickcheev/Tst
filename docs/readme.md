# What is tst?
Tst is a program, that helps you to do competitive programming competitions faster.
It allows to check your solutions in the tests that were loaded from one of allowing
servers, or tests that you created. It enables **Codeforces**

Supports Windows and Linux 


# Instalation

## System requirements
- g++
- Python 3.10 <=
- Python-3 pip


## Instalation process
> `git clone https://github.com/mikacha/Tst | cd Tst`
>
> `python3 setup.py install`

***

# Using
> `tst help` - full command list\
> `tst init` - initialize samples file in the working directory\
> `tst link https://[taskurl]` loads task sample tests from the server to the directory\
> `tst new [filename]` makes new file by default template. Make it **now-exec**

Before the launch of your code you should understand default executable conception.
When you will try to run your code using tst, tst won't know, what file you mean.
So then you should set now-exec file by the special command `tst default [filename]`.
If you made file using `tst new [filename]` then you set [filename] now-exec by default.

> `tst run` compile and launchs your code. Then check it with the samples
