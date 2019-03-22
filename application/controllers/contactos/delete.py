import config


class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_contacto):
        result = config.model.get_contacto(int(id_contacto))
        return config.render.delete(result)

    def POST(self, id_contacto):
        form = config.web.input()
        config.model.delete_contacto(form['id_contacto'])
        raise config.web.seeother('/')
