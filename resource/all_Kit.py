import json
from flask_restful import Resource
from flask import request, jsonify
#from flask_jwt_extended import jwt_required
from service.Kit_service import KitService

class AllKit(Resource):

    # @jwt_required
    def get(self):
        """
        Retorna vários registros de Kit

        #Consulta
        """
        service = KitService()
        return service.find(request.args)
    
    # @jwt_required
    def post(self):
        """
        Grava um novo registro em Kit

        #Gravação
        """
        req_data = request.get_json()
        service = KitService()
        return service.insert(req_data)

    # @jwt_required
    def put(self):
        """
        Updates a record in Kit

        #Gravação
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = KitService()
        return service.update(req_data)
