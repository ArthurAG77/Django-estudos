## **OQUE EU APRENDI COM ISSO?**

### Qual a diferença entre "Project" e "Apps"?  

A filosofia do Django é baseada na modularidade e reutilização de código, o que torna mais fácil entender a distinção entre **project** (vou chamar de **projeto** daqui para frente) e **apps**.  

Um **projeto** representa toda a aplicação web, enquanto um **app** funciona como um módulo independente dentro desse projeto, servindo a um propósito específico.  

Um app pode ser, por exemplo:  
- Um sistema de autenticação de usuários  
- Um blog  
- Qualquer outra funcionalidade autônoma  


### Criando Projetos e Apps

O primeiro passo para começar um projeto em Django é configurar o ambiente de desenvolvimento. Abaixo, você encontrará os comandos essenciais para iniciar um projeto e criar apps:

#### 1. Configurando o Ambiente Virtual
Antes de instalar o Django, é recomendável criar e ativar um ambiente virtual para isolar as dependências do projeto.
- **Criando o ambiente virtual:**
 `python -m venv meu_ambiente_virtual`
 - - -
- **Ativando o ambiente virtual**
 No Windows
 `meu_ambiente_virtual\Scripts\activate.bat`
 No Linux/MacOS
 `source meu_ambiente_virtual\bin\activate`
 - - -
 ####  2. Instalando o Django 
 `pip install django`
 #### 3. Criando um projeto
 Agora, com django instalado você pode criar um novo projeto
 
 `django-admin startproject nome_do_projeto .`
 
 isso criará a estrutura base de diretórios e arquivos de um projeto
 #### 4. Criando Apps dentro de um projeto
 Dentro de um projeto você pode criar apps<br>
 `python manage.py startapp nome_do_app`