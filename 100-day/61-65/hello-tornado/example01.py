"""
example01.py
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('<h1>Hello, world!</h1>')


def main():
    app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
