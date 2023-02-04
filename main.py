from flask import Flask, request
from utils import generate_password

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length_str = request.args.get('length', '10')
    if not length_str.isdigit():
        return 'Length should be a digit'

    length = int(length_str)

    if length <= 0:
        return 'Length should be positive digit'

    if length > 1000:
        return 'Password is too long'

    return generate_password(length)


if __name__ == '__main__':
    app.run(debug=True)



'''
https://127.0.0.1:5000/hello/dsjhds?length=10

1. http/s

2. 127.0.0.1/ google.com
 IPv4 
 x.x.x.x
 [0-255].[0-255].[0-255].[0-255]
 0.0.0.0
 255.255.255.255
 255.255.255.255.255
 255.255.255
 256.0.23.15
 
 IPv6

3. PORT :5000
0 - 65535

4. PATH /hello/dsjhds

127.0.0.1 localhost

GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS

'''
