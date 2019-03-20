import web
import config as config

class Insert:
	def __init__(self):
		pass

	def GET(self):
		return config.render.insert()

	def POST(self):
		formulario = web.input()
		nombre = formulario['nombre']
		telefono = formulario['telefono']
		email = formulario['email']
		config.model_contactos.insert_contacto(nombre, telefono, email)
		raise web.seeother('/')