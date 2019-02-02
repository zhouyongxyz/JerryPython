from tornado import ioloop, gen, iostream
from tornado.tcpclient import TCPClient


@gen.coroutine
def Trans():
    stream = yield TCPClient().connect( '127.0.0.1',8888 )
    try:
        while True:
            print(TCPClient)
            DATA = {
                "name":"Windows python",
                "type":"windows"
            };

            yield stream.write(0x)
            yield stream.write(str(DATA))
            back = yield stream.read_bytes(20)
            print(back)
            if DATA=='over':
                break
    except iostream.StreamClosedError:
        pass

if __name__ == '__main__':
    ioloop.IOLoop.current().run_sync(Trans)