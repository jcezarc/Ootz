import logging
from model.Produto_model import ProdutoModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class ProdutoService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(ProdutoModel)

    def find(self, params, sku=None):
        if sku:
            logging.info(f'Procurando "{sku}" em Produto ...')
            found = self.table.find_one([sku])
        else:
            logging.info('Procurando vários registros de Produto...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('Novo registro gravado em Produto')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Alterando Produto ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Registro gravado OK!")
        
    def delete(self, sku):
        logging.info('Removendo Produto ...')
        self.table.delete(sku)
        return resp_ok("Registro deletado OK!")
