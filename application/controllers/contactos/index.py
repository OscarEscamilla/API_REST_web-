import web 
import config as config

class Index:

	def __init__(self):
		pass


	def GET(self):
		contactos = config.model_contactos.select_contactos().list() # selecciona todos los registros usando el archivo importado config
		return config.render.index(contactos)




