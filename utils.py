from models import Pessoas

# Realiza consulta de dados na tabela pessoa
def consulta_pessoas():
    #pessoa = Pessoas.query.filter_by(nome='Ademar')
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Ademar').first()
    print(pessoa.idade)
    # for p in pessoa:
    #     print(p)
    #     print(p.nome)
    #     print(p.idade)

# insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Pepinha', idade=27)
    print(pessoa.idade)
    pessoa.save()

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ademar').first()
    pessoa.idade = 21
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pepinha').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
