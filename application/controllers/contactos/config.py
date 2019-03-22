import web
import application.models.model_contactos

render = web.template.render('application/views/contactos/', base='master')
model = application.models.model_contactos
    