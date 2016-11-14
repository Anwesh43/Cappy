import tornado.web
import tornado

class CappyHandler:
    class EndpointContainer:
        def __init__(self,endpoint,cb):
            self.endpoint = endpoint
            self.cb = cb
        def convertToRequests(self):
            handlerStr = "class {0}Handler(tornado.web.RequestHandler):\n\tdef get(self):\n\t\tself.write('{1}')".format(self.endpoint.capitalize(),self.cb())
            exec(handlerStr)
            exec("request=(r'{0}',{1}Handler)".format('/'+self.endpoint,self.endpoint.capitalize()))
            return request
    def __init__(self):
        self.endpointContainers = []
        self.requests = []

    def createEndpointsHandler(self):
        self.requests = []
        for endpointContainer in self.endpointContainers:
            self.requests.append(endpointContainer.convertToRequests())

    def handleRequest(self,endpoint,cb):
        self.endpointContainers.append(CappyHandler.EndpointContainer(endpoint,cb))
    def createServer(self):
        self.createEndpointsHandler()
        self.app = tornado.web.Application(self.requests)
        print self.requests

    def startServer(self,port=8000):
        print 'started listening on {0}'.format(port)
        self.app.listen(port)
        tornado.ioloop.IOLoop.current().start()
