import web 



db = web.database(
	dbn = 'mysql',  # motor de base de datos
	host = 'localhost',
	db = 'agenda',
	user = 'root',
	pw = '', # contrasena
	port = 3306 #puerto de mariadb
	)
