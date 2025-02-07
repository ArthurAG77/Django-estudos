## Arquivos de um projeto Django

- **core:** Este é basicamente o nosso projeto, pasta raiz de todas as seguintes
- **__init__.py:** Indica que o diretório é um pacote de codigo
- **Manage.py:** Tem as mesmas funções que django-admin, contudo antes de executar importa todas as configurações feitas em seu projeto 
- **settings.py:** Como o nome diz, esse arquivo é composto por todas as configurações do seu projeto django tal como, conexão com banco de dados, diretório que contenha os templates e afins
- **urls.py:** Serve para declarar as rotas (URL) da sua aplicação
- **asgi.py e wsgi.py:** Não tenho certeza ainda, mas tem relação com a configuração do aplication server quando o projeto está em produção 
- **db.sqlite3:** Banco de dados padrão do django, bom pra estudos. Mas por ser local não serve pra produção

---
## Reformulando oque é um app?
A grosso modo um app é uma função logica da sua aplicação, ou seja um projeto é composto por varias apps pois possui varios processos logicos.<br>
Ex: em um sistema de homologação de fornecedores, haverá um app responsavel pelo cadastro de fornecedores está app será responsavel apenas por essa etapa logica <br>
Apps são divisões logicas de funções dentro de um sistema web<br>

**para criar uma app execute**
`manage.py startapp nome_do_app`<br>
Após criar um app devemos indicar ao django a existencia do mesmo para que ele o execute, então vamos até os arquivos de configuração do nosso projeto django em **settings.py** e devemos adicionar na lista **INSTALLED_APPS** o nome do nosso APP
