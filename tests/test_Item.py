import sys
sys.path.append('..')
from service.Item_service import ItemService
from model.Item_model import ItemModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found

def test_find_success():
    table = FakeTable(ItemModel)
    record = table.default_values()
    table.insert(record)
    service = ItemService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = ItemService(FakeTable(ItemModel))
    msg, status_code = service.find(None, PK_DEFAULT_VALUE)
    assert status_code == 404

def test_insert_success():
    table = FakeTable(ItemModel)
    service = ItemService(table)
    record = table.default_values()
    status_code = service.insert(record)[1]
    assert status_code == 201

def test_insert_failure():
    service = ItemService(FakeTable(ItemModel))
    status_code = service.insert({})[1]
    assert status_code == 400
