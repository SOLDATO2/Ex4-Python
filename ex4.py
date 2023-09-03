"""
A estrategia utilizada para armazenar multiplos usuarios com nomes de chaves iguais foi utilizar o sistema "ID" para gerar parametros dentro de banco_usuarios e então,
alimentar estes parametros com dicionarios que serão gerados com o dicionario que será retornado pela função cadastrar_usuario
"""


def cadastrar_usuario(*args): #funcao responsavel por gerar um dicionario com chaves e valores para cadastro
    dicio = {} #dicionario temporario
    for x in args:
        dicio[x] = input(f"Digite um valor para o campo {x}: ") # define valor para os campos
    while(True):
        campos = input("Campos obrigatorios registrados, registre mais campos opcionais separados por virgula e\n digite 'sair' para sair: ").split(",") #executa apos os campos obrigatorios terem sido preenchidos
        for y in campos:
            if y == "sair":
                return dicio
            else:
                dicio[y] = input(f"Digite um valor para o campo {y}: ") #preenche os campos opcionais

def imprimir_usuarios(*args, **kwargs): # funcao responsavel por opcoes de submenus para mostrar os usuarios cadastrados
    possivel_busca =[] # lista para armazenar usuarios que possuem parametros que o usuario necessita
    if not args and not kwargs : # se nao tiver argumentos em args e kwargs, executa essa porcao
        print("Imprimindo todos")
        print(banco_usuarios)
    elif args and not kwargs: # se tiver arumentos em args ( busca por nomes )
        for x in args:
            for y in banco_usuarios:
                nome_banco = banco_usuarios[y].get("nome") #pega o conteudo da chave nome
                if nome_banco == x: # compara se o nome em args existe no banco, e se existir, mostra o registro inteiro do usuario
                    print(banco_usuarios[y])
    elif kwargs and not args: #se tiver argumentos em kwargs (bucas por campos)
        for x in banco_usuarios:
            for campo, valor in kwargs.items(): # utiliza campo e valor como referencia dos argumentos em kwargs
                if campo in banco_usuarios[x] and banco_usuarios[x][campo] == valor: # se o campo existir no banco usuarios e o campo tiver o mesmo valor de kwargs, salvar em uma lista de possivel resultado
                    possivel_busca.append(banco_usuarios[x])
        print(f"A busca retornou os seguinte opções: {possivel_busca}") # mostra os possiveis resultados
    elif kwargs and args: # Porcao de codigo similar aos anteriores. Ira mostrar usuarios com parametros especificos entre x y z usuarios.
        banco_filtrado = []
        for nome in args: 
            for cadastro in banco_usuarios:
                if banco_usuarios[cadastro].get("nome") == nome:
                    banco_filtrado.append(banco_usuarios[cadastro])

        for cadastro in banco_filtrado:
            atende_condicoes = True 
            for campo, valor in kwargs.items():
                if campo not in cadastro or cadastro[campo] != valor:
                    atende_condicoes = False # se o usuario não tiver o mesmo valor do campo ou não tiver o campo, não mostrar as informações do usuario
                    break
            if atende_condicoes:
                print(cadastro)
                
        
        
banco_usuarios = {} # banco usuarios global
while(True):
    #usuario precisa definir nome como opcao obrigatoria, pois ele esta registrando usuarios
    campos_obgrigatorios = input("Digite campos obrigatorios para registro separados por virgulas (OBS: é necessario no minimo cadastrar 'nome' como campo obrigatorio!): ").split(",")
    if "nome" not in campos_obgrigatorios:
        print("parametro nome não foi identificado, por favor tente novamente")
    else:
        break
    
while(True):
    print("1-cadastrar usuário\n2-imprimir usuários \n0-encerra\n")
    escolha = input("Escolha uma opção: ")
    
    match escolha:
        case "1":
            dicio_ref = cadastrar_usuario(*campos_obgrigatorios)
            id_cadastro = id(dicio_ref) # define id para separar usuarios e nao ocorrer conflito de informações
            banco_usuarios[id_cadastro] = dicio_ref.copy()
            print("Usuario cadastrado")
        case "2":
            print("Escolha uma opção: \n1 - impirmir todos\n2 - filtrar por nomes\n3 - filtrar por campos\n4 - filtrar por nomes e campos\n")
            opcao = input()
            match opcao:
                case "1":
                    imprimir_usuarios() #todos
                case "2":
                    argumentos = input("Escreva nomes que voce procura separados por ',': ").split(",") #args
                    imprimir_usuarios(*argumentos)
                case "3":
                    dicionario_ref = {}
                    argumentos = input("Digite campos para busca separados por ',' (exemplo: nome,idade): ").split(",") #kwargs
                    for x in argumentos:
                        dicionario_ref[x] = input(f"Digite um valor para {x}: ")
                    imprimir_usuarios(**dicionario_ref)
                case "4":
                    argumentos = input("Digite nomes separados por ',' para filtrar por nomes: ").split(",")
                    dicionario_ref = {}
                    campos_argumentos = input("Digite campos para busca separados por ',' (exemplo: nome,idade): ").split(",")

                    for x in campos_argumentos:
                        dicionario_ref[x] = input(f"Digite um valor para {x}: ")

                    imprimir_usuarios(*argumentos, **dicionario_ref)
        case "0":
            break