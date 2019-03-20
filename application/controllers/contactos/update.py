import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        contactos = config.model_contactos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(contactos) 
    
    def POST(self,nombre):
        formulario = web.input() 
        nombre = formulario['nombre'] 
        telefono = formulario['telefono'] 
        email = formulario['email'] 
        config.model_contactos.update_contacto(nombre, telefono, email)
        raise web.seeother('/') 
