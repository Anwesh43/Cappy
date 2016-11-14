from __init__ import CappyHandler
cappy = CappyHandler()
def helloCb():
    return "hello World"
def okCb():
    return "Ok"
def testHtmlPage():
    return {"page":"demoTemplates/hello.html","name":"Anwesh","age":24}
cappy.route('hello',helloCb)
cappy.route('ok',okCb)
cappy.route('testHello',testHtmlPage,True)
cappy.createServer()
cappy.startServer()
