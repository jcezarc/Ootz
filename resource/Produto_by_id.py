from flask_restful import Resource
from flask_jwt_extended import jwt_required

from service.Produto_service import ProdutoService

class ProdutoById(Resource):

    decorators=[jwt_required]

    # @jwt_required
    def get(self, sku):
        """
        Procura em Produto pelo campo sku

        #Consulta
        """
        service = ProdutoService()
        return service.find(None, sku)

    # @jwt_required
    def delete(self, sku):
        """
        Deleta um registro de Produto

        #Gravação
        """
        service = ProdutoService()
        return service.delete([sku])
