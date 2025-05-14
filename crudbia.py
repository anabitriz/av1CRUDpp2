
def menu():
    print("""
                      CRUD: MÚSICAS
    -----------------------------------------------------
     *🎵  PLAYLISTA - SUA PLAYLIST PERSONALIZADA 🎵 *
    =====================================================
        🎧 Organize suas músicas. 🎼 Viva sua vibe. 🎧
    =====================================================
1.📃 Adicionar artista
2.📃 Adicionar álbum
3.📋 Listar artista
4.📋 Listar álbum
5.🔎 Buscar artista
6.🔎 Buscar álbum
7.🖊 Adicionar música
8.📋 Listar música
9.🔎 Buscar música
10.🗑 Deletar artista
11.🗑 Deletar álbum
12.🗑 Deletar música
13.💾 Salvar e sair
""")

def artista(playlista):
    nome = input("Nome do artista: ")
    naci = input("Nacionalidade do artista: ")
    idade = int(input("Idade: "))
    playlista.append((nome, naci, idade))
    print("Dados do artista adicionados com sucesso!")

def album(play):
    nome_album = input("Nome do álbum: ")
    lançam = input("Ano de lançamento: ")
    play.append({"Nome do album": nome_album, "Ano de lançamento": lançam})
    print("Álbum adicionado!")

def listar_artista(playlista):
    if len(playlista) == 0: 
      print("nenhuma lista artista encontrado")
    else:
        for a in playlista:
          nome, naci, idade = a
          print(f'Nome: {nome}, nacionalidade: {naci}, idade {idade}')


def listar_album(play):
    if len(play) == 0:
      print("nenhum album encontrado")
    else:
      for b in play:
         print(f'Nome do album: {b["Nome do album"]}, Ano de lançamento: {b["Ano de lançamento"]}')
    if not play:
        print("Nenhum álbum encontrado.")
    else:
        for b in play:
            print(f'Nome do álbum: {b["Nome do album"]}, Ano de lançamento: {b["Ano de lançamento"]}')


def buscar_art(playlista):
    buscarA = input("Qual artista? ")
    for nome, naci, idade in playlista:
        if nome == buscarA:
            print(f'Nome: {nome}, Nacionalidade: {naci}, Idade: {idade}')
            return
    print(f'Artista "{buscarA}" não encontrado.')

def buscar_alb(play):
    buscarB = input("Qual álbum? ")
    for b in play:
        if b["Nome do album"] == buscarB:
            print(f'Nome: {b["Nome do album"]}, Lançamento: {b["Ano de lançamento"]}')
            return
    print(f'Álbum "{buscarB}" não encontrado.')

def musica(playmus):
    Nmusica = input("Nome da música: ")
    Nartista = input("Nome do artista: ")
    ano = input("Ano de lançamento: ")
    playmus.append((Nmusica, Nartista, ano))
    print("Música adicionada!")

def listar_mus(playmus):
    if len(playmus) == 0:
      print("nenhuma música encontrada")
    else:
      for m in playmus:
        Nmusica, Nartista, ano = m
        print (f'listar: {Nmusica}, artista: {Nartista}, ano: {ano}')

def buscar_msc(playmus):
    buscarM = input("Qual música? ")
    for Nmusica, Nartista, ano in playmus:
        if Nmusica == buscarM:
            print(f'Música: {Nmusica}, Artista: {Nartista}, Ano: {ano}')
            return
    print(f'Música "{buscarM}" não encontrada.')

def deletarA(playlista):
    buscarA = input("Nome do artista: ")
    for a in playlista:
        nome, _, _ = a
        if nome == buscarA:
            digitar = input("Digite 's' para confirmar exclusão: ").lower()
            if digitar == 's':
                playlista.remove(a)
                print(f'Artista "{nome}" deletado com sucesso.')
            return
    print(f'Artista "{buscarA}" não encontrado.')

def deletarB(play):
    buscarB = input("Nome do álbum: ")
    for b in play:
        if b["Nome do album"] == buscarB:
            digitar = input("Digite 's' para confirmar exclusão: ").lower()
            if digitar == 's':
                play.remove(b)
                print(f'Álbum "{buscarB}" deletado com sucesso.')
            return
    print(f'Álbum "{buscarB}" não encontrado.')



def deletarM(playmus):
    buscarM = input("Nome da música: ")
    for m in playmus:
        Nmusica, _, _ = m
        if Nmusica == buscarM:
            digitar = input("Digite 's' para confirmar exclusão: ").lower()
            if digitar == 's':
                playmus.remove(m)
                print(f'Música "{Nmusica}" deletada com sucesso.')
            return
    print(f'Música "{buscarM}" não encontrada.')


import json
def salvar(playlista, play, playmus, filename="dados.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump((playlista, play, playmus), f)

def carregar(filename="dados.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [], [], []

def main():
    playlista, play, playmus = carregar()
    opcao = 1
    while opcao != 0:
        menu()
        try:
            opcao = int(input("Qual opção deseja? "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        if opcao == 1:
            artista(playlista)
        elif opcao == 2:
            album(play)
        elif opcao == 3:
            listar_artista(playlista)
        elif opcao == 4:
            listar_album(play)
        elif opcao == 5:
            buscar_art(playlista)
        elif opcao == 6:
            buscar_alb(play)
        elif opcao == 7:
            musica(playmus)
        elif opcao == 8:
            listar_mus(playmus)
        elif opcao == 9:
            buscar_msc(playmus)
        elif opcao == 10:
            deletarA(playlista)
        elif opcao == 11:
            deletarB(play)
        elif opcao == 12:
            deletarM(playmus)
        elif opcao == 13:
            salvar(playlista, play, playmus)
            print("Dados salvos com sucesso! ")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
 