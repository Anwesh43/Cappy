import tornado.web
import tornado

class CappyHandler:
    class EndpointContainer:
        def __init__(self,endpoint,cb,templating):
            self.endpoint = endpoint
            self.cb = cb
            self.templating = templating
        def convertToRequests(self):
            handlerStr = "class {0}Handler(tornado.web.RequestHandler):\n\tdef get(self):\n\t\tself.write('{1}')".format(self.endpoint.capitalize(),self.cb())
            if self.templating:
                paramStr = ""
                htmlPage = ""
                index = 0
                itemsLength = len(self.cb().items())
                for (key,value) in self.cb().items():
                    index = index+1
                    if key == "page":
                        htmlPage = paramStr
                    else:
                        paramStr = paramStr+",{0}='{1}'".format(key,value)
                handlerStr = "class {0}Handler(tornado.web.RequestHandler):\n\tdef get(self):\n\t\tself.render('{1}'{2})".format(self.endpoint.capitalize(),self.cb()["page"],paramStr)
            exec(handlerStr)
            exec("request=(r'{0}',{1}Handler)".format('/'+self.endpoint,self.endpoint.capitalize()))
            return request
    def __init__(self):
        self.endpointContainers = []
        self.requests = []


    def __createEndpointsHandler(self):
        self.requests = []
        for endpointContainer in self.endpointContainers:
            self.requests.append(endpointContainer.convertToRequests())

    def route(self,endpoint,cb,templating=False):
        self.endpointContainers.append(CappyHandler.EndpointContainer(endpoint,cb,templating))
    def createServer(self):
        self.__createEndpointsHandler()
        self.app = tornado.web.Application(self.requests)

    def startServer(self,port=8000):
        print 'started listening on {0}'.format(port)
        self.app.listen(port)
        tornado.ioloop.IOLoop.current().start()
