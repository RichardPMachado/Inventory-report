from inventory_report.inventory.product import Product


def test_cria_produto():
    result = ("""O produto Nicotine Polacrilex fabricado em 2021-02-18
 por Target Corporation com validade até 2023-09-17
 precisa ser armazenado instrucao 1.""")
    product = Product(
      1,
      'Nicotine Polacrilex',
      'Target Corporation',
      '2021-02-18',
      '2023-09-17',
      'CR25 1551 4467 2549 4402 1',
      'instrucao 1')
    print(product)
    assert product == result
