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
9.🔎 Buscar música.
10. alterar artista.
11. alterar album.
12. alterar musica.                    
13.🗑 Deletar artista
14.🗑 Deletar álbum
15.🗑 Deletar música
0. sair
""")

def artista(playlista):
    nome = input("Nome do artista: ")
    naci = input("Nacionalidade do artista: ")
    idade = int(input("Idade: "))
    playlista.append({"Nome do artista": nome, "nacionalidade": naci, "idade": idade})
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
          print(f'Nome: {nome}, nacionalidade: {naci}, idade: {idade}')


def listar_album(play):
    if len(play) == 0:
      print("nenhum album encontrado")
    else:
      for b in play:
         print(f'Nome do album: {b["Nome do album"]}, Ano de lançamento: {b["Ano de lançamento"]}')
    


def buscar_art(playlista):
    buscarA = input("Qual artista? ")
    for a in playlista:
        nome, naci, idade = a
        if nome == buscarA:
            print(f'Nome: {nome}, Nacionalidade: {naci}, Idade: {idade}')
            return
    print(f'Artista "{buscarA}" não encontrado.')

def buscar_alb(play):
    buscarB = input("Qual álbum? ")
    for b in play:
        nome_album, lançam = b
        if nome_album == buscarB:
            print(f'Nome do album: {nome_album}, ano de lançamento: {lançam}')
            return
    print(f'Álbum "{buscarB}" nao encontrado.')

def musica(playmus):
    Nmusica = input("Nome da música: ")
    Nartista = input("Nome do artista: ")
    Nalbum = input ("de que album faz parte essa musica? ")
    ano = input("Ano de lançamento: ")
    playmus.append(f'Nome da musica: {Nmusica}, Nome do artista: {Nartista}, Nalbum: {Nalbum}, ano: {ano}')
    print("Música adicionada!")

def listar_mus(playmus):
    if len(playmus) == 0:
      print("nenhuma música encontrada")
    else:
      for m in playmus:
        Nmusica, Nartista, ano, Nalbum = m
        print (f'listar: {Nmusica}, artista: {Nartista}, ano: {ano}, album: {Nalbum}')

def buscar_msc(playmus):
    buscarM = input("Qual música? ")
    for m in playmus:
        Nmusica, Nartista, Nalbum, ano = m
        if Nmusica == buscarM:
            print(f'Música: {Nmusica}, Artista: {Nartista}, Ano: {ano}, album: {Nalbum}')
            return
    print(f'Música "{buscarM}" não encontrada.')

def deletarA(playlista):
    buscarA = input("Nome do artista: ")
    for a in playlista:
        nome, naci, idade = a
        if nome == buscarA:
            print(f'nome do arista: {nome}, nacionalidade: {naci}, idade: {idade}')
            digitar = input("Digite 'd' para deletar ").lower()
            if digitar == 'd':
                playlista.remove(a)
                print(f'Artista: {nome}, Nacionalidade: {naci}, Idade: {idade},  deletado com sucesso.')
            return
    print(f'Artista "{buscarA}" não encontrado.')

def deletarB(play):
    buscarB = input("Nome do álbum: ")
    for b in play:
        nome_album = b
        if nome_album == buscarB:
            digitar = input("Digite 'd' para deletar: ").lower()
            if digitar == 'd':
                play.remove(b)
                print(f'Álbum "{buscarB}" deletado com sucesso.')
            return
    print(f'Álbum "{buscarB}" não encontrado.')



def deletarM(playmus):
    buscarM = input("Nome da música: ")
    for m in playmus:
        Nmusica = m
        if Nmusica == buscarM:
            digitar = input("Digite 'd' para deletar: ").lower()
            if digitar == 'd':
                playmus.remove(m)
                print(f'Música "{Nmusica}" deletada com sucesso.')
            return
    print(f'Música "{buscarM}" não encontrada.')



def alterar_art(playlista):
    nomeA = input("nome do artista que quer alterar: ")
    for a in playlista:
        nome, naci, idade = a
        if nome == nomeA:
            print(f'nome: {nome}, nacionalidade {naci}, idade{idade}')
           
            novoArt = input("diga o nome do novo artista: ")
            idad = input("idade do novo artista: ")
            idad = int(idad)
            nacio = input ("nacionalidade do novo artist: ")
        
            confirmar = input ("digite '1' se deseja alterar: ")
            confirmar = int(confirmar)
            if confirmar== 1:
                playlista[playlista.index(a)] = novoArt, idad, nacio 
                print(f"o artista foi alterado!/ artista: {novoArt}, idade: {idad}, nacionaliddae: {nacio} ")
            else:
                print("alteração cancelada")
            return
    print (f'artista: {nomeA} não encontrado')

def alterar_alb(play):
    nomeB = input("nome do album que quer alterar: ")
    for b in play:
        nome_album, lançam = b
        if nome_album == nomeB:
            print(f'nome: {nome_album}, lançamento {lançam}')
           
            
            novoAlb = input("diga o nome do novo album")
            novoLan = input("ano de lançamento do novo album")

            confirmar = input ("digite '1' se deseja alterar: ")
           
            if confirmar== 1:
                play[play.index(b)] = novoAlb, novoLan 
                print(f'o artista foi alterado!/ album: {novoAlb}, ano de lançamento: {novoLan} ')
            else:
                print("alteração cancelada")
            return
    print (f'album: {nomeB} não encontrado')

def alterar_mus(playmus):
    nomeM = input("nome da nova musica: ")
    for m in playmus:
        Nmusica, Nartista, ano = m
        if Nmusica == nomeM:
            print(f'nome: {Nmusica}, artista {Nartista}, ano da musica{ano}')
            
            novaMus = input("diga o nome da nova musica")
            art = input("nome do novo artista")
            
            novoAno = input ("ano de lançamento")
            
            confirmar = input ("digite '1' se deseja alterar: ").lower()
        
            if confirmar == 1:
                playmus[playmus.index(m)] = novaMus, art, ano
                print(f'a música  foi alterada!/ música: {novaMus}, artista: {art}, ano de lançamento: {ano} ')
            else:
                print("alteração cancelada")
            return
    print (f'album: {nomeM} não encontrado')

            

import json
def salvar(playlista, play, playmus, filename="dados.json"):
    with open(filename, 'w') as f:
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
            alterar_art(playlista)
        elif opcao == 11:
            alterar_alb(play)
        elif opcao == 12:
            alterar_mus(playmus)         
        elif opcao == 13:
            deletarA(playlista)
        elif opcao == 14:
            deletarB(play)
        elif opcao == 15:
            deletarM(playmus)
        elif opcao == 0:    
            salvar(playlista, play, playmus)
            print("Dados salvos com sucesso! ")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()