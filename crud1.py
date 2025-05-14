from re import M
def menu():
  print ("""
                      CRUD: MÚSICAS
    -----------------------------------------------------

     *🎵  PLAYLISTA - SUA PLAYLIST PERSONALIZADA 🎵 *
    =====================================================
        🎧 𝑶𝒓𝒈𝒂𝒏𝒊𝒛𝒆 𝒔𝒖𝒂𝒔 𝒎𝒖́𝒔𝒊𝒄𝒂𝒔.🎼 𝑽𝒊𝒗𝒂 𝒔𝒖𝒂 𝒗𝒊𝒃𝒆.🎧
    =====================================================    
🎶

1.📃Adicionar artista.
2.📃Adicionar album.
3. listar artista.
4. listar album.
5.🔎buscar artista.
6.🔎buscar album.
7.🖊adicionar música.
8.listar musica .
9. buscar musica
10.🗑Deletar artista.
11. deletar album.
12. deletar musica.
13.Sair.
  """)
 

def artista(playlista):
    nome = input("Nome do artista: ")
    naci = input("Nacionalidade do artista: ")
    idade =int(input("idade:"))
    playlista.append((nome, naci, idade))
    print("dados do artista dicionado com sucesso! ")

def album(play):
    nome_album = input ("nome do album: ")
    lançam = input ("ano de lançamento: ")
    play.append({"Nome do album": nome_album, "Ano de lançamento": lançam})
    print("album adicionado!")

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



def buscar_art(playlista):
    buscarA = input ("qual artista?")
    for a in playlista:
      nome, naci, idade = a
      if nome == buscarA:
        print(f'Nome do artista: {nome}, Nacionalidade: {naci}, idade: {idade}')
        break
    else:
      print(f'Artista: {buscarA} nao   encontrado')

def buscar_alb(play):
    buscarB= input ("qual album?")
    for b in play:
      nome_album, lançam = b
      if b["Nome do album"] == buscarB:
        print(f'nome: {b["Nome do album"]}, lançamento{b["Ano de lançamento"]}')
        break
    else:
      print(f'album: {buscarB} não encontrado')


def musica(playmus):
    Nmusica = input("nome da música")
    Nartista = input ("nome do artista")
    ano = input ("Ano de lançamento")
    playmus.append((Nmusica, Nartista, ano))
    print("musica adicionada!")

def listar_mus(playmus):
    if len(playmus) == 0:
      print("nenhuma música encontrada")
    else:
      for m in playmus:
        Nmusica, Nartista, ano = m
        print (f'listar: {Nmusica}, artista: {Nartista}, ano: {ano}')

def buscar_msc(playmus):
    buscarM = input ("qual música?")
    for m in playmus:
      Nmusica, Nartista, ano = m
      if Nmusica == buscarM:
        print(f'Nome do da musica: {Nmusica} artista {Nartista}, ano {ano} ')
        break
    else:
      print(f'musica: {buscarM}, nao encontrada!')
     

def deletarA(playlista):
      buscarA = input ("nome do artista")
      for a in playlista:
          nome, naci, idade = a
          if nome == buscarA:
            print(f'nome: {nome}, nacionalidade{naci}, idade{idade}')
            deletarA = int(input("digite 0 para excluir"))
            if deletarA == 1:
              del playlista[playlista.index(a)]
              print(f'artista: {nome} , deletado(a)!')
              break
      else:
        print(f'musica: {buscarA}, nao encontrada')


def deletarB(play):
      buscarB = input ("nome do ALBUM")
      for b in play:
          nome_album, lançam = b
          if b['nome do album'] == buscarB:
              print(f'nome: {b["Nome do album"]}, lançamento{b["Ano de lançamento"]}')
          deletarB = int(input ("digite 00 para excluir "))
          if deletarB == 0:
              del play[play.index(b)]
              print(f'album: {b["Nome do album"]}, deletado!')
              break
      else:
        print(f'musica {buscarB}, nao encontrada')


def deletarM(playmus):
      buscarM = input ("nome da musica ")
      for m in playmus:
          Nmusica, Nartista, ano = m
          if Nmusica == buscarM:
            print(f'nome: {Nmusica}, artista{Nartista}')
            deletarM = int (input ("digite 000 para excluir "))
            if deletarM == 0:
              del playmus[playmus.index(m)]
              print(f'musica: {Nmusica}, deletada!')
              break
      else:
        print(f'musica {buscarM}, nao encontrada')


def main():
    playlista = []
    play = []
    playmus =[]
    opcao = 1
    while opcao != 0:
        menu()
        opcao = int(input("qual opção deseja? "))
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
          break
        else:
          print("Opção inválida. Tente novamente.")



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


def main_1():
    playlista, play, playmus = carregar()
    opcao = 1
    while opcao != 0:
        menu()
        opcao = int(input(opcao))    
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
             print("Dados salvos com sucesso!")
        break
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
     main_1()