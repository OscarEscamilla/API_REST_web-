import web
import config
import json


class Api_contactos:
    def get(self, id_contacto):
        try:
            # http://api_products?user_hash=12345&action=get
            if id_contacto == None:
                result = config.model.get_all_contactos()
                contactos_json = []
                for row in result:
                    tmp = str(dict(row))
                    contactos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(contactos_json)
            else:
                # http://api_products?user_hash=12345&action=get&id_product=1
                result = config.model.get_contacto(int(id_contacto))
                contactos_json = []
                contactos_json.append(str(dict(result)))
                web.header('Content-Type', 'application/json')
                return json.dumps(contactos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            contactos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(contactos_json)

# https://0.0.0.0:8080/api_products?user_hash=12345&action=put&id_product=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre, telefono, email):
        try:
            config.model.insert_contacto( nombre, telefono, email)
            contactos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(contactos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None
# http://api_products?user_hash=12345&action=get&id_product=1
    def delete(self, id_contacto):
        try:
            config.model.delete_contacto(id_contacto)
            contactos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(contactos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None
# https://0.0.0.0:8080/api_products?user_hash=12345&action=update&id_product=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_contacto, nombre, telefono, email):
        try:
            config.model.edit_contacto(id_contacto, nombre, telefono, email)
            contactos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(contactos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            contactos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(contactos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_contacto=None,
            nombre=None,
            telefono=None,
            email=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_contacto = user_data.id_contacto
            nombre = user_data.nombre
            telefono = user_data.telefono
            email = user_data.email

            if user_hash == '12345':  # user_hash
                if action == None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_contacto)
                elif action == 'put':
                    return self.put(nombre, telefono, email)
                elif action == 'delete':
                    return self.delete(id_contacto)
                elif action == 'update':
                    return self.update(id_contacto, nombre, telefono, email)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
