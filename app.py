import web 

urls = (
	'/','application.controllers.contactos.index.Index',
	'/insert', 'application.controllers.contactos.insert.Insert',
	'/update/(.*)', 'application.controllers.contactos.update.Update',
	'/delete/(.*)', 'application.controllers.contactos.delete.Delete',
	'/view/(.*)', 'application.controllers.contactos.view.View',

	)


if __name__ == "__main__":
	web.config.debug = False
	app = web.application(urls, globals())
	app.run()