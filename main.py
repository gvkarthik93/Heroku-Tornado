import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

import tensorflow as tf
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('public/index.html')

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test handler is up and running")

class TensorHandler(tornado.web.RequestHandler):
    def get(self):
        serverStatus = tf.constant('TensorFlow Server is up and running')
        sess = tf.Session()
        print(sess.run(serverStatus))
        self.write(sess.run(serverStatus))

def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", TestHandler),
        (r"/tf", TensorHandler),
        (r'/public/(.*)', tornado.web.StaticFileHandler, {'path': 'public/'}),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()