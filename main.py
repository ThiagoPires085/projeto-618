from itertools import product


banco_de_dados = [
    {
      'codigo': 1,
      'nome': 'mouse',
      'preco': 150.00,
      'disponivel': True
    }
]

codigo_atual = 1

def cadastrar_produto(nome:str, preco: float) -> None:  
    global codigo_atual
    codigo_atual += 1
    produto = {
      "codigo": codigo_atual,
      "nome": nome,
      "preco": preco,
      "disponivel": True
      
  }
    banco_de_dados.append(produto)
    print('produto adicionado com sucesso!')


def listar_produtos():
  print('---PRODUTOS CADASTRADOS---')
  for produto in banco_de_dados:
    print(f"codigo: {produto['codigo']}")
    print(f"nome: {produto['nome']}")
    print(f"preço: {produto['preco']}")
    print(f"disponivel: {produto['disponivel']}")
    print('-'*50)


def buscar_produto(codigo: int):
  for produto in banco_de_dados:
    if produto['codigo'] == codigo:
      return produto
  return None

def deletar_produto(codigo: int):
  produto = buscar_produto(codigo)
  if produto:
    banco_de_dados.remove(produto)
    print('produto removido com sucesso')
    return
  print('produto não encontrado')


def editar_produto(codigo: int, novo_nome: str, novo_preco: float):
  produto = buscar_produto(codigo)
  if produto:
    # produto = {
    #   'nome': nome_antigo,
    #   'preco': preco_antigo
    # }
    produto['nome'] = novo_nome
    produto['peco'] = novo_preco
    print('dados alterados com sucesso')
    return
  print('produto não encontrado')

def menu():
    print('---bem vindo ao menu---')
    while True:
      print('1 - adicionar produto')
      print('2 - editar produto')
      print('3 - listar produtos')
      print('4 - buscar produto')
      print('5 - deletar produto')
      print('0 - sair')
      opcao = input('selecione uma opção')
      if opcao == '1':
        nome = input('digite o nome do produto: ')
        preco = float(input('digite o preço do produto: '))
        cadastrar_produto(nome, preco)
      elif opcao =='2':
        codigo = int(input('digite o código do produto: '))
        nome = input('digite o nome do produto: ')
        preco = float(input('digite o preço do produto: '))
        editar_produto(codigo, nome, preco)
      elif opcao == '3':
        listar_produtos()
      elif opcao == '4':
        codigo = int(input('digite o código do produto: '))
        print(buscar_produto(codigo))
      elif opcao == '5':
        codigo = int(input('digite o código do produto: '))
        deletar_produto(codigo)
      elif opcao == '0':
        print('você saiu do progama')
        break
      else:
        print('opção invalida')

menu()




cadastrar_produto("fone de ouvido", 59.99)
editar_produto(1, "processador", 899.99)
listar_produtos()
editar_produto(-1, "fone", 500)






