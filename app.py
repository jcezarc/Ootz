# -*- coding: utf-8 -*-
import logging
import uuid
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_jwt_extended import create_access_token, JWTManager
from resource.user_controller import valid_user
from util.swagger_generator import FlaskSwaggerGenerator
from model.Produto_model import ProdutoModel
from resource.Produto_by_id import ProdutoById
from resource.all_Produto import AllProduto
from model.Kit_model import KitModel
from resource.Kit_by_id import KitById
from resource.all_Kit import AllKit
from model.Item_model import ItemModel
from resource.Item_by_id import ItemById
from resource.all_Item import AllItem


BASE_PATH = '/Ootz'

def config_routes(app):
    api = Api(app)
    #--- Resources: ----
    api.add_resource(ProdutoById, f'{BASE_PATH}/Produto/<sku>', methods=['GET'], endpoint='get_Produto_by_id')
    api.add_resource(AllProduto, f'{BASE_PATH}/Produto', methods=['GET'], endpoint='get_AllProduto')
    api.add_resource(AllProduto, f'{BASE_PATH}/Produto', methods=['POST'], endpoint='post_Produto')
    api.add_resource(AllProduto, f'{BASE_PATH}/Produto', methods=['PUT'], endpoint='put_Produto')
    api.add_resource(ProdutoById, f'{BASE_PATH}/Produto/<sku>', methods=['DELETE'], endpoint='delete_Produto')
    api.add_resource(KitById, f'{BASE_PATH}/Kit/<sku>', methods=['GET'], endpoint='get_Kit_by_id')
    api.add_resource(AllKit, f'{BASE_PATH}/Kit', methods=['GET'], endpoint='get_AllKit')
    api.add_resource(AllKit, f'{BASE_PATH}/Kit', methods=['POST'], endpoint='post_Kit')
    api.add_resource(AllKit, f'{BASE_PATH}/Kit', methods=['PUT'], endpoint='put_Kit')
    api.add_resource(KitById, f'{BASE_PATH}/Kit/<sku>', methods=['DELETE'], endpoint='delete_Kit')
    api.add_resource(ItemById, f'{BASE_PATH}/Item/<id>', methods=['GET'], endpoint='get_Item_by_id')
    api.add_resource(AllItem, f'{BASE_PATH}/Item', methods=['GET'], endpoint='get_AllItem')
    api.add_resource(AllItem, f'{BASE_PATH}/Item', methods=['POST'], endpoint='post_Item')
    api.add_resource(AllItem, f'{BASE_PATH}/Item', methods=['PUT'], endpoint='put_Item')
    api.add_resource(ItemById, f'{BASE_PATH}/Item/<id>', methods=['DELETE'], endpoint='delete_Item')
    
    #-------------------

def set_swagger(app):
    swagger_url = '/docs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/api',
        config={
            'app_name': "*- Ootz -*"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


def swagger_details(args):
    id_route = args[0]
    params = args[1]
    model = None
    resource = None
    docstring = ""
    if id_route == 'docs':
        docstring = """Documentação Swagger
        #Doc
        """
    elif id_route == 'Produto':
        if not params:
            resource = AllProduto
        else:
            resource = ProdutoById
        model = ProdutoModel()
    elif id_route == 'Kit':
        if not params:
            resource = AllKit
        else:
            resource = KitById
        model = KitModel()
    elif id_route == 'Item':
        if not params:
            resource = AllItem
        else:
            resource = ItemById
        model = ItemModel()
    
    ignore = False
    return model, resource, docstring, ignore

logging.basicConfig(
    filename='Ootz.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

APP = Flask(__name__)
CORS(APP)
# APP.config['JWT_SECRET_KEY'] = str(uuid.uuid4())
# JWT = JWTManager(APP)
config_routes(APP)
set_swagger(APP)

@APP.route('/api')
def get_api():
    """
    Dados da API

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)

@APP.route('/health')
def health():
    return 'OK', 200

@APP.route('/handshake', methods=['POST'])
def handshake():
    user = request.json.get('user')
    password = request.json.get('password')
    found, user_id = valid_user(user, password)
    if not found:
        return "Usuário/Senha não conferem", 403
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token), 200

if __name__ == '__main__':
    APP.run(debug=True)
