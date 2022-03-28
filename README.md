# Bem vindo a API de Alunos e Responsáveis!

Olá, este é o repositório da API REST de Alunos e Responsáveis, desenvolvida em **Python** utilizando o framework **Django/RestFramework**. Esta API foi desenvolvida como forma de estudos da disciplina de **Tópicos Avançados Em Programação Para Web** (PW26S) da **UTFPR**.
Esta foi a primeira experiência com a linguagem Python que tive, portanto provavelmente haverá pontos no código que poderiam ser feitos de outra forma.

# Como realizar a configuração inicial para desenvolver uma aplicação como esta

 1. Realizar o download do Python no [link](https://www.python.org/downloads/).
 2. Após realizar o download, o ideal é criarmos um virtual environment do python, que conterá todas as bibliotecas e uma cópia dos executáveis necessários para trabalhar com o python, para isso, primeiro precisamos instalar de forma global o virtual env executando o comando **pip install virtualenv**.
 3. Agora com o virtualenv instalado, vamos executar o comando para "startar" um novo virtualenv na pasta que iremos criar nosso novo projeto "virtualenv env"
 4. Vamos executar o comando para ativar o terminal dentro do virtual env: **source env/bin/activate**
 5. Próximo passo, instalar a dependência do **Django**, **postgres** e do **restframework** do Django ao projeto: **pip install django djangorestframework psycopg2**
 6. Agora vamos criar o novo projeto django executando o comando **django-admin startproject nome_projeto_admin**
 7. No arquivo **settings.py** do nosso projeto admin iremos adicionar a dependência do rest_framework.
```
INSTALLED_APPS = [
   ...
    'rest_framework'
]
```
 8. Também será neste arquivo que você irá configurar o banco de dados pgsql
 ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
 9. Agora iremos criar nosso projeto de api: **python manage.py startapp nome_api**
 10. Vamos referenciar nosso projeto da api no settings.py
 ```
INSTALLED_APPS = [
   ...
    'rest_framework',
    'pw26s', #novo projeto
]
``` 
 11. Agora podemos executar a criação das migrations iniciais do Django
 ```
python manage.py makemigrations
```
 12. E agora vamos aplicar no banco de dados a migration
 ```
python manage.py migrate
```
 13. Agora já devemos estar com a aplicação pronta para executar, bastando rodar o seguinte comando, por padrão a aplicação roda no [localhost:8000/admin](localhost:8000/admin)
 ```
python manage.py runserver
```

 
# Deploy Heroku

Para fazer o deploy no Heroku foi utilizado o [este guia](https://www.treinaweb.com.br/blog/deploy-de-uma-aplicacao-django-no-heroku) para deploy de aplicações Django.

 1. Vamos executar o comando para logar no heroku
```shell
heroku login
```
 2. Será necessário importar e adicionar as seguintes linhas no settings.py
 ```python
import django_heroku
django_heroku.settings(locals())
```
 3. Após isso, adicione na raiz do projeto o arquivo Procfile e adicione a seguinte linha, que será a linha a ser executada para startar nosso servidor web gunicorn.
 ```tex
web: gunicorn nome_aplicacao.wsgi
```
### Observação: Caso tenha dúvida em qual nome colocar para o servidor web, será o mesmo nome que deu para sua aplicação admin, pode ser verificado dentro do arquivo wsgi.py, conforme o print abaixo:

![Onde encontrar o nome do projeto] - ![image](https://user-images.githubusercontent.com/54125357/160323058-11a4e7a3-ee63-47ba-9d8a-c64b43e7edd6.png)

 4. Agora você deve extrair as depedências do projeto para um txt, utilizando o comando abaixo
 ```shell
pip freeze > requirements.txt
```
 5. Agora vamos utilizar o heroku cli para deploy
 ```shell
heroku git:remote -a nome-projeto
```
```shell
git add .
git commit -m "Deploy da aplicação"
git push -u heroku master
```
 6. Agora você deve adicionar ao seu projeto no heroku o add-on do postgres
 ![Print com o Heroku Postgres]![image](https://user-images.githubusercontent.com/54125357/160323085-42e30b7c-9014-40e0-9cf3-10f109bf9077.png)
 7. Após configurar as credenciais de banco de dados em sua aplicação, pode executar o comando para executar as migrations remotamente:
 ```shell
heroku run python manage.py migrate
```
