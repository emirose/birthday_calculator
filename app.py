import os

import tornado
import tornado.web
import tornado.httpserver

import models.birthday_calculator as birthday_calculator

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", CalculatorHandler) ,
            (r"/calculate", CalculatorHandler)
                ]
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__),
                    'templates'),
                debug = True
                )
        tornado.web.Application.__init__(self, handlers, **settings)

class CalculatorHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html', results=None)

    def post(self):
        birthdate = self.get_argument('birthdate')
        results = birthday_calculator.calculate(birthdate)
        self.render('index.html', results=results)

def main():
    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
