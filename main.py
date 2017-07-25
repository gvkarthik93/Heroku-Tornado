import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('public/index.html')

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test handler is working")
 
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r'/public/(.*)', tornado.web.StaticFileHandler, {'path': 'public/'}),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()