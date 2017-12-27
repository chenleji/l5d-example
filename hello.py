import consul
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def get_address():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(host_name)


if __name__ == '__main__':
    address = get_address()
    consul.Consul(port=8500, host="consul").agent.service.register(
        "hello",
        address=address,
        port=80,
        check=consul.Check.http("http://"+address+":80/", '5s')
    )
    app.run(host="0.0.0.0", port=80)
