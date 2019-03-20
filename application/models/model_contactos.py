import config as config 

db = config.db

def select_contactos():
    try:
        return db.select('contactos') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return


def select_nombre(nombre):
	try:
		return db.select('contactos', where = 'nombre=$nombre', vars=locals())[0] #selecciona el primer registro que coincida con el nombre dado en el parametro
	except Exception as e:
		print "Model select_nombre Error ()".format(e.args)
		print "Model select_nombre Message {}".format(e.message)
		return None


""" 
metodo para insertar productos
"""

def insert_contacto(nombre, telefono, email):
	try:
		return db.insert('contactos', 
			nombre = nombre,
			telefono = telefono,
			email = email)
	except Exception as e:
		print "Model insert_contacto Error ()".format(e.args)
		print "Model insert_contacto Message {}".format(e.message)
		return None

"""
metodo para eliminar productos
"""

def delete_contacto(nombre):
	try:
		return db.delete('contactos', where = 'nombre=$nombre', vars=locals())
	except Exception as e:
		print "Model delete_contacto Error ()".format(e.args)
		print "Model delete_contacto Message {}".format(e.message)
		return None

def update_contacto(nombre, telefono, email):
	try:
		return db.update('contactos',
			telefono = telefono,
			email = email,
			where = 'nombre=$nombre',
			vars=locals())
	except Exception as e:
		print "Model update_contactos Error ()".format(e.args)
		print "Model update_contactos Message {}".format(e.message)
		return None


