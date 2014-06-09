import os

import tornado
import tornado.web
import tornado.httpserver

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", CalculatorHandler) ,
                ]
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__),
                    'templates'),
                debug = True
                )
        tornado.web.Application.__init__(self, handlers, **settings)

class CalculatorHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

def main():
    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
