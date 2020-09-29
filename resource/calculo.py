import json
from flask_restful import Resource
from flask import request, jsonify
from service.Item_service import ItemService
from util.messages import resp_ok


def sku_kit(value):
    return f'kit.sku = "{value}"'

class Calculo(Resource):
    def get(self, sku):
        '''
          Cálculo de Kit
          ---
          **Parâmetro**
          `sku` = chave primária do kit
          **Retorno**
          `custo` = soma dos custos dos produtos do kit;
          `preco` = soma de todos os produtos do kit, com o respectivo desconto;
          `qtd_max` = quantidade máxima de Kits para o estoque disponível de cada produto do kit.
          #Consulta
        '''
        service = ItemService()
        service.table.new_condition_event['sku'] = sku_kit
        msg, status_code = service.find({
          'sku': sku
        })
        if status_code != 200:
            return msg, status_code
        dataset = msg.get('data')
        total_custo = 0
        total_preco = 0
        qtd_max = 0
        for item in dataset:
            quantidade = item['quantidade']
            produto = item['produto']
            custo = produto['custo']
            preco = produto['preco']
            desconto = item['desconto']
            estoque = produto['estoque']
            disponivel = estoque / quantidade
            if not qtd_max or qtd_max > disponivel:
              qtd_max = disponivel
            total_custo += custo
            total_preco += preco * (1 - (desconto / 100))
        return resp_ok(
            'Calculo executado com sucesso',
            {
                'preco': total_preco,
                'custo': total_custo,
                'qtd_max': qtd_max
            },
            200
        )
