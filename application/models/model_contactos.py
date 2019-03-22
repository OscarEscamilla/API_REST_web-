import web
import config

db = config.db


def get_all_contactos():
    try:
        return db.select('contactos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def get_contacto(id_contacto):
    try:
        return db.select('contactos', where='id_contacto=$id_contacto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get aMessage {}".format(e.message)
        return None

def delete_contacto(id_contacto):
    try:
        return db.delete('contactos', where='id_contacto=$id_contacto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None

def insert_contacto(nombre, telefono, email):
    try:
        db.insert('contactos',
                  nombre=nombre,
                  telefono=telefono,
                  email=email,
                  )
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None

def edit_contacto(id_contacto, nombre, telefono, email):
    try:
        db.update('contactos',
                  nombre=nombre,
                  telefono=telefono,
                  email=email,
                  where='id_contacto=$id_contacto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model update Message {}".format(e.message)
        return None
