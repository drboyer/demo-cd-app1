import cherrypy

class HelloWorld(object):
  def index(self):
    return "Hello World (version 2.0!)"
  index.exposed = True

cherrypy.quickstart(HelloWorld())
