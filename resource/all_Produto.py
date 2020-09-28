import json
from flask_restful import Resource
from flask import request, jsonify
#from flask_jwt_extended import jwt_required
from service.Produto_service import ProdutoService

class AllProduto(Resource):

    # @jwt_required
    def get(self):
        """
        Retorna vários registros de Produto

        #Consulta
        """
        service = ProdutoService()
        return service.find(request.args)
    
    # @jwt_required
    def post(self):
        """
        Grava um novo registro em Produto

        #Gravação
        """
        req_data = request.get_json()
        service = ProdutoService()
        return service.insert(req_data)

    # @jwt_required
    def put(self):
        """
        Updates a record in Produto

        #Gravação
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = ProdutoService()
        return service.update(req_data)
