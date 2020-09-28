from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Produto_model import ProdutoModel
from model.Kit_model import KitModel


PK_DEFAULT_VALUE = "000"

class ItemModel(Schema):
    id = Str(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    quantidade = Integer()
    desconto = Float()
    produto = Nested(ProdutoModel)
    kit = Nested(KitModel)
