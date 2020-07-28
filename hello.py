from flask import Flask
hello = Flask(__name__)

@hello.route('/')
def hello_world():
     return '<B>Sri Aurobindo</B>'

if __name__ == '__main__':
    hello.run()
