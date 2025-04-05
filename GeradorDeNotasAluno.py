import os
import json

ARQUIVO_DADOS = (r"alunos.json")



# Garante que o arquivo exista e esteja com um dicionário vazio, se não existir ainda
if not os.path.exists(ARQUIVO_DADOS):
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump({}, f, indent=4)
# Função para carregar os dados do arquivo JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Erro ao carregar dados. Iniciando com um dicionário vazio.")
                return {}  # <- Aqui é o ponto importante!
    else:
        print("Arquivo não existe!")
        return {}  # <- Aqui também!

# Função para salvar os dados no arquivo JSON
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as f:  # Abre o arquivo no modo escrita
        json.dump(dados, f, indent=4)  # Salva os dados formatados em JSON

# Função para adicionar um novo aluno
def adicionar_aluno(nome):
    dados = carregar_dados()  # Carrega os dados existentes
    if nome in dados:
        print("Aluno já cadastrado!")
    else:
        dados[nome] = []  # Cria um espaço para armazenar as notas do aluno
        salvar_dados(dados)  # Salva os dados atualizados
        print(f"Aluno {nome} adicionado com sucesso!")

# Função para adicionar notas a um aluno existente
def adicionar_nota(nome, nota):
    dados = carregar_dados()
    if nome in dados:  # Verifica se o aluno existe
        dados[nome].append(nota)  # Adiciona a nova nota
        salvar_dados(dados)  # Salva os dados atualizados
        print(f"Nota {nota} adicionada para {nome}.")
    else:
        print("Aluno não encontrado!")

# Função para calcular a média das notas de um aluno
def calcular_media(nome):
    dados = carregar_dados()
    if nome in dados and dados[nome]:  # Verifica se o aluno existe e tem notas
        media = sum(dados[nome]) / len(dados[nome])  # Calcula a média
        return media
    else:
        return None  # Retorna None se não houver notas

# Função para exibir alunos e suas médias
def exibir_resultados():
    dados = carregar_dados()
    print("\nResultados dos alunos:")
    for nome, notas in dados.items():
        if notas:  # Verifica se há notas registradas
            media = sum(notas) / len(notas)  # Calcula a média
            status = "Aprovado" if media >= 7 else "Reprovado"  # Define a situação do aluno
            print(f"{nome}: Média {media:.2f} - {status}")
        else:
            print(f"{nome}: Sem notas registradas.")

# Menu principal do programa
while True:
    print("\nGerenciador de Notas")
    print("1 - Adicionar Aluno")
    print("2 - Adicionar Nota")
    print("3 - Exibir Resultados")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        adicionar_aluno(nome)
    elif opcao == "2":
        nome = input("Nome do aluno: ")
        nota = float(input("Nota: "))
        adicionar_nota(nome, nota)
    elif opcao == "3":
        exibir_resultados()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
