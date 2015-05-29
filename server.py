import cherrypy

class HelloWorld(object):
  def index(self):
    return "Hello World, now with auto-deployment!!"
  index.exposed = True

# bind to all interfaces to make this app external
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(HelloWorld())
