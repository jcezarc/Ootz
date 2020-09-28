import logging
from model.Item_model import ItemModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class ItemService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(ItemModel)

    def find(self, params, id=None):
        if id:
            logging.info(f'Procurando "{id}" em Item ...')
            found = self.table.find_one([id])
        else:
            logging.info('Procurando vários registros de Item...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('Novo registro gravado em Item')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Alterando Item ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Registro gravado OK!")
        
    def delete(self, id):
        logging.info('Removendo Item ...')
        self.table.delete(id)
        return resp_ok("Registro deletado OK!")
