from helloapp import hello
from myapp import myapp

# 这里本地load与setup load的import格式一样
if __name__ == '__main__':
    hello.hello_func()
    myapp.myapp_func()