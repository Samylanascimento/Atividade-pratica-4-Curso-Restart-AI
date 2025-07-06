
def calcula_preco_total():
  nome_produto = "Cadeira Infantil"
  preco_unitario = 12.40
  quantidade = 3

  preco_total = preco_unitario * quantidade

  print(f"Produto: {nome_produto}")
  print(f"Preço Unitário: R$ {preco_unitario:.2f}")
  print(f"Quantidade: {quantidade}")
  print(f"Preço Total: R$ {preco_total:.2f}")

calcula_preco_total()
