import pandas as pd
animais = []
def validar(nome, tipo):
    if tipo == str:
        if not nome:
            print('erro: não deixe o nome do animal/comida em branco!')
            return False
        if len(nome) <= 3:
            print('erro: animal/comida inválido!, cada um deve conter pelo menos 4 letras!')
            return False
        if nome.isdigit():
            print('erro: não digite numeros no nome do animal/comida!')
            return False
        return True
def criar():
    animal = input('Digite o nome de um animal: ').strip()
    if validar(animal, str): #*Aqui mudou!// agora está validando!
        comida = input('Digite o nome de uma comida para o animal: ').strip()
        if validar(comida, str): #! aqui mudou! agora está validando!
            animais.append({'animal': animal, 'comida': comida}) #!se as duas validação for verdade o appendcomeça! 
        else:  #* Aqui mudou! se a validação da comida for false, ela cai nesse bloco
            print('erro ao validar a comida!')
    else:  #*Aqui mudou! se a validação do animal for false, ele cai nesse bloco
        print('erro ao validar o nome do animal!')
def loop():
    while True:
        criar()
        go = input('[P]arar?').strip().upper() 
        if go == 'P':
            break
        df = pd.DataFrame(animais) #! aqui mudou! #agora o df salva a lista (animais)
        df.to_json('teste_1.json', orient='records') #! e aqui ele pega a info e joga p/ json!
def mostrar():
    df = pd.read_json('teste_1.json')
    for _, dados in df.iterrows(): #! aqui foi mudado! # agora o for funciona!
        print(f'\n Animal: [dados{"animal"}] Comida: [dados{"comida"}]')
def filtros_comida():
    comida = input('Digite o nome da comida que queira filtrar!: ').strip()
    df = pd.read_json('teste_1.json')
    df_comida = df[df["comida"] == comida]
    print(df_comida)
def filtros_animal():
    animal = input('Digite o nome do animal que queira filtrar!: ').strip()
    df = pd.read_json('teste_1.json')
    df_animal = df[df["animal"] == animal] #! aqui foi mudado!/ agora não ocorre mais bug
    print(df_animal)
def troca_comida(): 
    animal = input('Digite um animal: ').strip()
    comida = input('Digiete a comida que queira trocar: ').strip()
    df = pd.read_json('teste_1.json')
    df.loc[df["animal"] == animal, 'comida'] = comida
    df.to_json('teste_1.json',orient='records')
def troca_animal():
    animal = input('Digite o animal que queira trocar: ').strip()
    df = pd.read_json('teste_1.json')
    df.loc[df["animal"] == animal,'animal'] = animal
    df.to_json('teste_1.json',orient='records')
def excluir_animal():
    animal = input('Digite o animal que queira excluir!: ').strip()
    df.pd.read_json('teste_1.json')
    df.loc[df["animal"] != animal]
    df.to_json('teste_1.json',orient='records')
def excluir_comida():
    comida = input('Digite uma comida que queira remover!: ').strip()
    df.pd.read_json('teste_1.json')
    df.loc[df["comida"] != comida]
    df.to_json('teste_1.json',orient='records')
def interacion():
    interagir_usuario = input('[A]cessar, [R]emover, [F]iltrar,[T]roca de dados: ').strip().upper()
    if interagir_usuario == 'A':
        try:
            mostrar()
        except FileNotFoundError:
            print('erro: arquivo vázio!')
            loop()
            mostrar() 
        except FileExistsError:
            print('erro inesperado!, arquivo.json não foi encontrado!')
            loop()
            mostrar()
    elif interagir_usuario == 'R':
        interaçao = input('Deseja Remover um [A]nimal ou [C]omida?: ').strip().upper()
        if interaçao == 'A':
            try:
                excluir_animal()
            except ValueError:
                print('erro: tenha certeza que o animal existe no arquivo.json!')
            except FileNotFoundError:
                print('erro: arquivo.json está vazio!')
                loop()
                excluir_animal()
            except FileExistsError:
                print('erro inesperado! arquivo.json não foi encontrado!')
                loop()
                excluir_animal()
        elif interaçao == 'C':
            try:
                excluir_comida()
            except ValueError:
                print('erro: tenha certeza que o animal existe no arquivo.json!')
            except FileNotFoundError:
                print('erro: o arquivo.json está vazio! a remoção não será possivel!')
                loop()
                excluir_comida()
            except FileExistsError:
                print('erro inesperado! o arquivo.json nãoo foi encontrado!')
                loop()
                excluir_comida()
        else:
            print('erro de digitação!, digite uma das letras listadas acima!')
    elif interagir_usuario == 'F':
        __interaçao__ = input('Deseja Filtrar [A]nimais ou [C]omida? ').strip().upper()
        if __interaçao__ == 'A':
            try:
                filtros_animal()
            except ValueError:
                print('erro: tenha certeza de filtrar um animal já existente!')
                mostrar()
                filtros_animal()
            except FileNotFoundError:
                print('erro: arquivo vázio!')
                loop()
                filtros_animal()
            except FileExistsError:
                print('erro inesperado! arquivo.json não foi encontrado!')
                loop()
                filtros_animal()
        elif __interaçao__ == 'C':
            try:
                filtros_comida()
            except ValueError:
                print('erro! tenha certeza que essa comida existe!')
                try:
                    mostrar()
                    filtros_animal
                except FileNotFoundError:
                    print('arquivo.json vazio!')
                    loop()
                    filtros_comida()
                except FileExistsError:
                    print('erro! arquivo.json inexistente!')
                    loop()
                    filtros_comida()
            except FileNotFoundError:
                print('arquivo.json vazio!')
                loop()
                filtros_comida()
            except FileExistsError:
                print('erro! arquivo.json inexistente!')
                loop()
                filtros_comida()
        else:
            print('erro de digitação!, tenha certeza que digitou a letra correta!')
    elif __interaçao__ == 'T':
        _interagir_ = input('Deseja Trocar os dados dos [A]nimais ou [C]omida?').strip().upper()
        if _interagir_ == 'A':
            try:
                troca_animal()
            except ValueError:
                try:
                    print('erro! certifique-se que o animal exista no arquivo.json!')
                    mostrar()
                except FileNotFoundError:
                    print('erro arquivo.json vazio!')
                    loop()
                    troca_animal()
                except FileExistsError:
                    print('erro arquivo.json não encontrado!')
                    loop()
                    troca_animal()
            except FileNotFoundError:
                print('erro! arquivo.json vazio!')
                loop()
                troca_animal()
            except FileExistsError:
                print('erro! arquivo.json não foi encontrado!')
                loop()
                troca_animal()
        elif _interagir_ == 'C':
            try:
                troca_comida()
            except FileExistsError:
                print('erro! arquivo.json não foi encontrado!')
                loop()
                troca_comida()
            except ValueError:
                print('erro! tenha certeza de que a comida esteja no arquivo.json')
            except FileNotFoundError:
                print('erro! o arquivo.json não foi encontrado!')
                loop()
                troca_comida()
    else:
        print('erro de digitação! se certifique que a letra escrita corresponde as que estão acima!')
interacion()