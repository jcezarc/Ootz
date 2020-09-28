from flask_restful import Resource
from flask_jwt_extended import jwt_required

from service.Item_service import ItemService

class ItemById(Resource):

    decorators=[jwt_required]

    # @jwt_required
    def get(self, id):
        """
        Procura em Item pelo campo id

        #Consulta
        """
        service = ItemService()
        return service.find(None, id)

    # @jwt_required
    def delete(self, id):
        """
        Deleta um registro de Item

        #Gravação
        """
        service = ItemService()
        return service.delete([id])
