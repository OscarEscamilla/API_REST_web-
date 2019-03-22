import config

class View:
    
    def __init__(self):
        pass

    def GET(self, id_contacto):
        id_contacto = int(id_contacto)
        result = config.model.get_contacto(id_contacto)
        return config.render.view(result)
