from lib.Cappy import CappyHandler
cappy = CappyHandler()
def helloCb():
    return "hello World"
def okCb():
    return "Ok"
cappy.handleRequest('hello',helloCb)
cappy.handleRequest('ok',okCb)
cappy.createServer()
cappy.startServer()
