# Barber System

- Programa web para agendamento de horários em barbearias.

# Requisitos Mínimos:

01 - Instalar o Visual Studio Code (https://code.visualstudio.com/download)

02 - Instalar o Python no windows (https://www.python.org/downloads/)

03 - Instalar o MYSQL no windowns (https://dev.mysql.com/downloads/installer/)

04 - Instalar o Git no windows (https://git-scm.com/)

# Preparando ambiente no Visual Code Studio:

01 - Instalar extensão do Python

02 - Instalar extensão do Live Server

03 - Instalar extensão do Material Icon Theme

04 - Instalar extensão do Bracket Pair Colorize

05 - Instalar extensão do Portuguese (Brazil) Language Pack for Visual Studio Code

# Clonando o projeto do GitHub:

- No terminal do Visual Studio Code executar os códigos:

01 - git clone https://github.com/DanielBelorini22/barber_system_professional.git

02 - cd barber_system_professional

03 - python -m venv venv

04 - .\venv\Scripts\activate

Obs - (No Visual Studio Code selecione o interpretador venv criado prescionando a tecla F1 e marcando a opção venv recomendada)

05 - Com o venv ativado... python -m pip install --upgrade pip

06 - pip install -r requirements.txt

# Configurando o banco de dados no MySQL Workbench:

- Criando banco de dados

01 - create database barber_system;

02 - use barber_system;

03 - show tables;

# Aplicando no Django o banco de dados recém criado

01 - Abra o arquivo 'settings' no diretório: barber_system_professional -> barber_system -> barber_system -> settings.py

02 - No arquivo 'settings' aberto localize 'DATABASES'. (CTRL+F para abrir a busca no código)

03 - A configuração do 'DATABASES' será parecida com essa:

obs: Em Password deverá ser digitada a mesma senha de quando instalou o MySQL na máquina.

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'barber_system',
        'USER': 'root',
        'PASSWORD': 'DigiteAquiSuaSenha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

- Após digitar sua senha, pressione CTRL+S para salvar as alterações no arquivo.

# Rodando o projeto localmente

- Após clonar o projeto do Git e criar e configurar o banco de dados, execute os seguintes códigos no terminal do Visual Studio Code:

01 - Verifique o diretório atual na linha do terminal, deverá estar em 'barber_system_professional/barber_system'. Caso não tiver digite cd 
barber_system_professional/barber_system

02 - digite python manage.py migrate

03 - digite python manage.py runserver

04 - Ao digitar o 'runserver' será executado o servidor local com um link para abrir no navegador o projeto (Starting development server at http://127.0.0.1:8000/). Clique no link ou copie e cole no navegador.
