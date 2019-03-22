import config

class Edit:

    def __init__(self):
        pass
    
    def GET(self, id_contacto):
        result = config.model.get_contacto(int(id_contacto))
        return config.render.edit(result)

    def POST(self, id_contacto):
        form = config.web.input()
        """
        image = config.web.input(product_image={})
        filedir = 'static/files'
        filepath = image.product_image.filename.replace('\\', '/')
        filename = filepath.split('/')[-1]
        fout = open(filedir + '/' + filename, 'w')
        fout.write(image.product_image.file.read())
        fout.close()
        product_image = filename
        """

        config.model.edit_contacto(
            form['id_contacto'],
            form['nombre'],
            form['telefono'],
            form['email'],
        )
        raise config.web.seeother('/')
        