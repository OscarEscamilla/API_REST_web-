import web
import config as config 

class Delete:

	def __init__(self):
		pass

	def GET(self, nombre):
		contactos = config.model_contactos.select_nombre(nombre)
		return config.render.delete(contactos)

	def POST(self, nombre):
		formulario = web.input() 
		nombre = formulario['nombre']
		config.model_contactos.delete_contacto(nombre)
		raise web.seeother('/') 