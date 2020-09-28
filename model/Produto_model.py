from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


PK_DEFAULT_VALUE = "000"

class ProdutoModel(Schema):
    sku = Str(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    nome = Str()
    custo = Float()
    preco = Float()
    estoque = Integer()
