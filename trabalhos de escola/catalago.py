filmes = []
jogos = []
series = []

while True:
    print("==== CATALAGO ===")
    pessoa = input("\n1. Adicionar Filme \n2. Adicionar Jogo \n3. Adicionar Série \n4. Sair\n5. Exibir lista\nEscolha: ")

    if pessoa == "":
        continue
    elif pessoa == "4":
        print("Saindo...")
        break
    elif pessoa == "1":
        filmes = input("Digite o nome do filme: ")
        filmes.append(filmes)
        print(f"Filmes: {filmes}")
    elif pessoa == "2":
        jogo = input("Digite o nome do jogo: ")
        jogos.append(jogo)
        print(f"Jogos: {jogos}")
    elif pessoa == "3":
        serie_nome = input("Digite o nome da série: ")
        series.append(serie_nome)
        print(f"Séries: {series}")
    elif pessoa == "5":
        print("=== EXIBIR CATALOGO ===")
        if not filmes and not jogos and not series:
            print("Nenhum item cadastrado.")
        else:
            print("Filmes:", filmes)
            print("Jogos:", jogos)
            print("Séries:", series)
    else:
        print("Opção inválida. Tente novamente.")