from django.shortcuts import render # Lib para renderizar o html com ou sem dados
from django.core.paginator import Paginator #Essa lib serve para simplificar a paginação no django

import requests

def index(request):
    users =[]
    # Esse trecho é responsavel por consumir a API
    for x in range(1, 5+1):
        user = {}
        #x vai começar do 1 e ir ate < 6
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{x}')
        data = response.json()
        id = data['id']
        name = data['name']
        username = data['username']
        email = data['email']
        user = {'id':id, 'name':name, 'username':username, 'email':email}

        # Incluindo dentro de um array
        users.append(user)
    
    # Função sorted e lambda para colocar os nomes em ordem alfabetica
    users = sorted(users, key = lambda n: n['name'])


    # Trecho da paginação

    content_page = 2 # 2 registros por pagina
    # Cria um objeto 'paginação'
    obj_paginator = Paginator(users, content_page)
    # Vai retornar o 2 primeiro conteudos ( pagina 1)
    user_page = obj_paginator.page(1).object_list
    # Vai ser o range, vai começar do 1 e no 4-1 (nesse caso) já que é 2 por pagina e sao 5 (3 paginas)
    page_range = obj_paginator.page_range
    # O end é usado para saber se o usuario chegou na ultima pagina, se sim, vai colocar o next como desabilitado
    end = obj_paginator.num_pages

    # Testa se foi feita um requisição ajax
    if request.is_ajax():

        if request.GET.get('search'):
            users_search = []
            for x in users:
                # Nesse trecho vai fazer a comparação, se tiver as letras digitadas naquilo, então vai 
                # retprmar um novo objeto paginação 
                if request.GET.get('search') in x['name']:
                    aux = x
                    users_search.append(aux)
            users_search = sorted(users_search, key = lambda n: n['name'])
            obj_paginator = Paginator(users_search, content_page)
        else:
            # Se nao tiver um shearch no GET, vai continuar normalmente
            obj_paginator = Paginator(users, content_page)
            print(users)

        # Pega o valor por GET vindo do ajax 
        if request.GET.get('page'):
            p = int(request.GET.get('page'))
        else:
            p = 1
        
        # Cria um objeto 'paginação'
        page_range = obj_paginator.page_range


        # Pegar os conteudos da pagina vinda do ajax
        user_page = obj_paginator.page(p).object_list
        end = obj_paginator.num_pages

        # Context é um dicionario que enviarar dados para o template
        context={
            'users':user_page, # Conteudo pendendendo da paginação
            'page_range':page_range, # Quantidade de pagina
            'end':end, # Pagina final
            'page_atual':p, # Pagina atual
            'prox':p+1, # Proximo, vai ser p+1
            'prev':p-1, # Anterior, vai ser p-1
        }

        # Vai usar o .html() do jquery para renderizar um arquivo html com os dados dentro de uma div
        return render(request, 'place/user-list.html', context)
    else:

        # Context é um dicionario que enviarar dados para o template
        context={
            'users':user_page, # Se não tiver paginação, sempre vai ser 1
            'page_range':page_range, # Quantidade de pagina
            'end':end, # Pagina final
            'page_atual':1, # Pagina atual vai ser 1, porque quando clicar na 2, vai entrar na condição ajax
            'prox':2, # Proximo vai ser 2, porque quando clicar no proximo, vai entrar na condição ajax
            'prev':1, # Anterior vai ser 1, porque quando clicar no Anterior, vai entrar na condição ajax
        }
        # So renderizar o arquivo index.html mesmo
        return render(request, 'place/index.html', context)
