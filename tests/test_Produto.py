import sys
sys.path.append('..')
from service.Produto_service import ProdutoService
from model.Produto_model import ProdutoModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found

def test_find_success():
    table = FakeTable(ProdutoModel)
    record = table.default_values()
    table.insert(record)
    service = ProdutoService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = ProdutoService(FakeTable(ProdutoModel))
    msg, status_code = service.find(None, PK_DEFAULT_VALUE)
    assert status_code == 404

def test_insert_success():
    table = FakeTable(ProdutoModel)
    service = ProdutoService(table)
    record = table.default_values()
    status_code = service.insert(record)[1]
    assert status_code == 201

def test_insert_failure():
    service = ProdutoService(FakeTable(ProdutoModel))
    status_code = service.insert({})[1]
    assert status_code == 400
