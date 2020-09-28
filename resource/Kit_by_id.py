from flask_restful import Resource
from flask_jwt_extended import jwt_required

from service.Kit_service import KitService

class KitById(Resource):

    decorators=[jwt_required]

    # @jwt_required
    def get(self, sku):
        """
        Procura em Kit pelo campo sku

        #Consulta
        """
        service = KitService()
        return service.find(None, sku)

    # @jwt_required
    def delete(self, sku):
        """
        Deleta um registro de Kit

        #Gravação
        """
        service = KitService()
        return service.delete([sku])
