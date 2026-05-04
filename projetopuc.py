import json

# Aluno: Leonardo Bezerra Ferraro
# Curso: Analise e Desenvolvimento de Sistemas

def salvar_arquivo(lista, projetopuc):
    with open(projetopuc +'.json', 'w') as f:
        json.dump(lista, f, indent=4)
        f.close()

def ler_arquivo(projetopuc):
    try:
        with open(projetopuc +'.json', 'r') as f:
            lista = json.load(f)
            f.close()
            return lista
    except:
        salvar_arquivo(lista, projetopuc)
        return []


# Função - Menu principal
def mostrar_menu_princi():
    print('............................')
    print('Seja bem-vindo(a) ao Menu Principal')
    print('(1).Estudantes')
    print('(2).Professores')
    print('(3).Disciplinas')
    print('(4).Turmas')
    print('(5).Matrículas')
    print('(0).Sair')
    print('............................')

# Função - Menu de Operações
def mostrar_menu_opera():
    print('............................')
    print('Opção válida!')
    print('Menu de Operações - {}'.format(opcaocad))
    print('(1).Incluir')
    print('(2).Listar')
    print('(3).Excluir')
    print('(4).Alterar')
    print('(5).Voltar ao menu anterior')
    print('............................')

# Função - Menu incluir
def menuincluir():
    print('Função Incluir:')

    # Opção Estudante
    if m1 == 1:
        codigo = int(input('Digite o codigo {}:'.format(opcaocad)))
        nome = str(input('Digite o nome completo:'))
        cpf = str(input('Digite o cpf:'))
        dados_estu = {}
        dados_estu["Codigo Estudante"] = codigo
        dados_estu["Nome"] = nome
        dados_estu["CPF"] = cpf
        lista.append(dados_estu)
        salvar_arquivo(lista, 'arquivo_lista.json')


    # Opção Professor
    if m1 == 2:
        codigo_prof = int(input('Digite o codigo do professor:'))
        nome = str(input('Digite o nome completo:'))
        cpf = str(input('Digite o cpf:'))
        dados_prof = {}
        dados_prof["Codigo Professor"] = codigo_prof
        dados_prof["Nome"] = nome
        dados_prof["CPF"] = cpf
        lista.append(dados_prof)
        salvar_arquivo(lista, 'arquivo_lista.json')


    # Opção Disciplina
    if m1 == 3:
        codigo_disc = int(input('Digite o codigo da disciplina:'))
        nome = str(input('Digite o nome da disciplina:'))
        dados_disc = {}
        dados_disc["Codigo Disciplina"] = codigo_disc
        dados_disc["Nome"] = nome
        lista.append(dados_disc)
        salvar_arquivo(lista, 'arquivo_lista.json')



    # Opção Turma
    if m1 == 4:
        codigo_tur = int(input('Digite o codigo da turma:'))
        codigo_prof = int(input('Digite o codigo do professor:'))
        codigo_disc = int(input('Digite o codigo da disciplina:'))
        dados_tur = {}
        dados_tur["Codigo Turma"] = codigo_tur
        dados_tur["Codigo Prof."] = codigo_prof
        dados_tur["Codigo Disci."] = codigo_disc
        lista.append(dados_tur)
        salvar_arquivo(lista, 'arquivo_lista.json')


    # Opção Matrícula
    if m1 == 5:
        codigo_matri = int(input('Digite o codigo da matrícula:'))
        codigo_estu = int(input('Digite o codigo do estudante:'))
        dados_matri = {}
        dados_matri["Codigo Matricula"] = codigo_matri
        dados_matri["Codigo"] = codigo_estu
        lista.append(dados_matri)
        salvar_arquivo(lista, 'arquivo_lista.json')


# Função - Menu Listar
def menu_listar():

    # Opção estudante
    if m1 == 1:
        lista = ler_arquivo("arquivo_lista.json")
        if len(lista) == 0:
            print('Não há {} cadastrados'.format(opcaocad))
            input('Pressione ENTER para continuar')
        else:
            print('Lista de {} cadastrados:'.format(opcaocad))
            for dados_estu in lista:
                print(dados_estu)

    # Opção professor
    elif m1 == 2:
        lista = ler_arquivo("arquivo_lista.json")
        if len(lista) == 0:
            print('Não há {} cadastrados'.format(opcaocad))
            input('Pressione ENTER para continuar')
        else:
            print('Lista de {} cadastrados:'.format(opcaocad))
            for dados_prof in lista:
                print(dados_prof)

    # Opção disciplina
    elif m1 == 3:
        lista = ler_arquivo("arquivo_lista.json")
        if len(lista) == 0:
            print('Não há {} cadastrados'.format(opcaocad))
            input('Pressione ENTER para continuar')
        else:
            print('Lista de {} cadastrados:'.format(opcaocad))
            for dados_disc in lista:
                print(dados_disc)

    # Opção turma
    elif m1 == 4:
        lista = ler_arquivo("arquivo_lista.json")
        if len(lista) == 0:
            print('Não há {} cadastrados'.format(opcaocad))
            input('Pressione ENTER para continuar')
        else:
            print('Lista de {} cadastrados:'.format(opcaocad))
            for dados_tur in lista:
                print(dados_tur)

    # Opção matricula
    elif m1 == 5:
        lista = ler_arquivo("arquivo_lista.json")
        if len(lista) == 0:
            print('Não há {} cadastrados'.format(opcaocad))
            input('Pressione ENTER para continuar')
        else:
            print('Lista de {} cadastrados:'.format(opcaocad))
            for dados_matri in lista:
                print(dados_matri)



# Função - Menu Excluir
def menu_excluir():
    print('Função Excluir:')
    codigo_exc = int(input('Digite o codigo que deseja excluir:'))
    remover = None
    if m1 == 1:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Estudante"] == codigo_exc:
                remover = dicionario
                break
        if remover is None:
            print('{} não encontrado!'.format(opcaocad))
        else:
            lista.remove(remover)
            print('Cadastro removido com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')

    if m1 == 2:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Professor"] == codigo_exc:
                remover = dicionario
                break
        if remover is None:
            print('{} não encontrado!'.format(opcaocad))
        else:
            lista.remove(remover)
            print('Cadastro removido com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')

    if m1 == 3:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Disciplina"] == codigo_exc:
                remover = dicionario
                break
        if remover is None:
            print('Disciplina não encontrada!')
        else:
            lista.remove(remover)
            print('Cadastro removido com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')

    if m1 == 4:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Turma"] == codigo_exc:
                remover = dicionario
                break
        if remover is None:
            print('Turma não encontrada!')
        else:
            lista.remove(remover)
            print('Cadastro removido com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')

    if m1 == 5:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Matricula"] == codigo_exc:
                remover = dicionario
                break
        if remover is None:
            print('Matrícula não encontrada!')
        else:
            lista.remove(remover)
            print('Cadastro removido com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')


# Função - Menu Alterar
def menu_alterar():
    print('Função Alterar:')
    codigo_alt = int(input('Digite o codigo que deseja alterar:'))
    alterar = None
    if m1 == 1:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Estudante"] == codigo_alt:
                alterar = dicionario
                break
        if alterar is None:
            print('Cadastro não encontrado!')
        else:
            alterar["Codigo Estudante"] = int(input('Digite o novo codigo:'))
            alterar["Nome"] = str(input('Digite o novo nome:'))
            alterar["CPF"] = str(input('Digite o novo cpf:'))
            print('Cadastro alterado com sucesso!')
            input('Pressione ENTER para continuar')
            salvar_arquivo(lista, 'arquivo_lista.json')
            return

    if m1 == 2:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Professor"] == codigo_alt:
                alterar = dicionario
                break
        if alterar is None:
            print('Cadastro não encontrado!')
        else:
            alterar["Codigo Professor"] = int(input('Digite o novo codigo:'))
            alterar["Nome"] = str(input('Digite o novo nome:'))
            alterar["CPF"] = str(input('Digite o novo cpf:'))
            salvar_arquivo(lista, 'arquivo_lista.json')
            return

    if m1 == 3:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Disciplina"] == codigo_alt:
                alterar = dicionario
                break
        if alterar is None:
            print('Cadastro não encontrado!')
        else:
            alterar["Codigo Disciplina"] = int(input('Digite o novo codigo da disciplina:'))
            alterar["Nome"] = str(input('Digite o novo nome da disciplina:'))
            salvar_arquivo(lista, 'arquivo_lista.json')
            return

    if m1 == 4:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Turma"] == codigo_alt:
                alterar = dicionario
                break
        if alterar is None:
            print('Cadastro não encontrado!')
        else:
            alterar["Codigo Turma"] = int(input('Digite o novo codigo da turma:'))
            alterar["Codigo Professor"] = int(input('Digite o novo codigo do professor:'))
            alterar["Codigo Disciplina"] = int(input('Digite o novo codigo da disciplina:'))
            salvar_arquivo(lista, 'arquivo_lista.json')
            return

    if m1 == 5:
        lista = ler_arquivo("arquivo_lista.json")
        for dicionario in lista:
            if dicionario["Codigo Matricula"] == codigo_alt:
                alterar = dicionario
                break
        if alterar is None:
            print('Cadastro não encontrado!')
        else:
            alterar["Codigo Matricula"] = int(input('Digite o novo codigo de matrícula:'))
            alterar["Codigo Estudante"] = int(input('Digite o novo codigo de estudante:'))
            salvar_arquivo(lista, 'arquivo_lista.json')
            return

m1 = 1
lista = []
lista_estu = []
lista_prof = []
lista_disc = []
lista_tur = []
lista_matri = []

# Mostrando operações
while m1 != 9:
    mostrar_menu_princi()
    m1 = int(input('Digite uma opção válida:'))
    opcaocad = ""
    if m1 == 1:
        opcaocad = "Estudantes"
    elif m1 == 2:
        opcaocad = "Professores"
    elif m1 == 3:
        opcaocad = "Disciplinas"
    elif m1 == 4:
        opcaocad = "Turmas"
    elif m1 == 5:
        opcaocad = "Matrículas"
    elif m1 == 0:
        print('Você selecionou a opção sair')
        break
    else:
        print('Opção INVÁLIDA!')
        input('Pressione ENTER para continuar')
        continue

    # Mostrando Menu secundario
    m2 = 1
    while m2 != 5:
        mostrar_menu_opera()
        m2 = int(input('Digite uma opção válida:'))


    # Mostrando Menu Incluir
        if m2 == 1:
            print('............................')
            menuincluir()

    # Mostrando Menu Listar
        elif m2 == 2:
            print('............................')
            menu_listar()


    # Mostrando Menu Excluir
        elif m2 == 3:
            print('............................')
            menu_excluir()


    # Mostrando Menu Alterar
        elif m2 == 4:
            print('............................')
            menu_alterar()

        elif m2 == 5:
            salvar_arquivo(lista, "arquivo_lista.json")
            break

        else:
            print('Opção INVÁLIDA!')
            input('Pressione ENTER para continuar')
            continue




















