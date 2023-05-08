from inventory_report.inventory.product import Product


mock_product = {
    "id": 1,
    "nome_do_produto": "Nicotine Polacrilex",
    "nome_da_empresa": "Target Corporation",
    "data_de_fabricacao": "2021-02-18",
    "data_de_validade": "2023-09-17",
    "numero_de_serie": "CR25 1551 4467 2549 4402 1",
    "instrucoes_de_armazenamento": "instrucao 1",
 }


def test_cria_produto():

    product = Product(**mock_product)

    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.numero_de_serie, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.instrucoes_de_armazenamento, str)

    assert product.id == mock_product['id']
    assert product.nome_do_produto == mock_product["nome_do_produto"]
    assert product.nome_da_empresa == mock_product["nome_da_empresa"]
    assert product.data_de_fabricacao == mock_product["data_de_fabricacao"]
    assert product.data_de_validade == mock_product["data_de_validade"]
    assert product.numero_de_serie == mock_product["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == (
        mock_product["instrucoes_de_armazenamento"])
