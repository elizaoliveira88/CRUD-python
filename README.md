# CRUD-python 

## O que deve ser feito?

>O objetivo é que você desenvolva um sistema web de adição, atualização, filtro e remoção de produtos de determinada empresa. Esse serviço deve atender os seguintes requisitos:

## Requisitos funcionais
* [ ] Adicionar empresas;
* [ ] Adicionar produtos das empresas cadastradas;
* [ ] Remover um produto da empresa;
* [ ] Consultar todos os produtos disponíveis que tal empresa possui;
* [ ] Consultar a lista de empresas cadastradas e trazer os produtos cadastrados


## Entregas obrigatórias
* [ ] README do projeto explicando como configurar o ambiente e rodar o projeto.
* [ ] Deploy da aplicação em Kubernetes
* [ ] API contendo os seguintes endpoints:
* [ ] Listar produtos
* [ ] Listar empresas
* [ ] Cadastrar produto e empresa
* [ ] Adicionar um produto na lista da empresa;
* [ ] Remover um produto da lista da empresa; 
* [ ] Consultar todos os produtos e empresas cadastradas.



> Comando para atualizar pip: python -m pip install --upgrade pip



# Comandos

> Comando pra criar uma vm pro projeto ficar só aqui e não de forma global no PC 
    python -m venv ambiente_virtual 
    
> Comando para ativar a VM. Toda vez que vcs desligarem a máquina, deve repetir esse comando. VÁ ATÉ A PASTA QUE TÁ O PROJETO
    
    # Em windows
    
    ambiente_virtual\Scripts\activate    
    ambiente_virtual\Scripts\activate.bat
    
    # Unix ou MacOS
    
    source tutorial-env/bin/activate
    
> Instalar DJango no ambiente virtual

    python -m pip install Django
    
> Iniciar uma aplicação devidamente usando Python: O ponto é para não criar outra pasta dentro de project

    django-admin startproject project .
    
> Iniciar a aplicação com o nome de app

    python manage.py startapp app
    

# Comando para por o servidor para rodar

    python3 manage.py runserver
    
### Começando o LAYOUT da aplicação

> Crie a pasta TEMPLATE dentro de APP

> Crie o index.html dentro de template

> Modifique o arquivo views.py

> Copie e cole o CDN do bootstrap dentro de index.html

> Pesquise table bootstrap no google

> Mudei a classe padrão thead-dark pra table-dark

#### Como podem ver tudo começa com a rota, chama a função e depois ela renderiza a view que você quer






    








