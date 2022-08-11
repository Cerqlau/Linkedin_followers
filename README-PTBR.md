# Linkedin Followers

Este projeto foi desenvolvido em Python para efetuar o gerenciamento e expansão da rede Linkedin, possui gerenciador de licensas através do banco de dados Mongo DB. Possibilita efetuar a programação de solcitação e exclusão de solicitação de pessoas em períodos programados. A ferramenta faz uso do Selenium e Mozil webdriver para que se possa efetuar a manipulação dos navegador.
O projeto conta com interface para usuário gerado do QT Designer e utiliza a biblioteca PyQT5 para que a UI se torne responsiva. 

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

```
=> Pyton 3.8 ou superior instalado;
=> Instalar o arquivo "requeriments.txt": pip install -r /path/to/requirements.txt
```

### 🔧 Pré-configurações

CONEXÃO COM O MONGODB

Será necessário a criação de uma conta de usuário. Efetuar criação de banco de dados para verficação de MACADRESS e LICENSAS distribuidas;
1- Efetuar a criação de um Banco de dados. EX:  "myFirstDatabase";
2- Efetuar a criação de arquivos JSON para armazenamento dos dados EX: 'clients', 'licensa';
2.2- Como exemplo poderá ser feito o upload dos arquivos "id_disponível.json" para 'clients' e 'licensa.json' para 'licensa'


3- Crie o link de para conexão com o MongoDB conforme a versão de utilização

4- Utilizar o arquivo "client_connection.py" para inserir os dados para acesso ao banco de dados

```
def __init__(self,login='email_de_login_no_mongo_DB',password='password',database='myFirstDatabase') -> None:
    self.password = password
    self.login = login
    self.database = database
    self.client = MongoClient(f"mongodb+srv://{self.login}:{self.password}@cluster0.3rdov.mongodb.net/test") #Inserir o link de conexão com o banco de dados
    self.db =self.client['myFirstDatabase']  #Nome do Banco de Dados 
    self.data_status = self.db['clients']    #DB onde ficarão o dados de MAC Adress e atividade do cliente
    self.data_licensa= self.db['licensa']    #DB onde deverão se encontrar as licensas já liberadas para os clientes

```

CONFIGURAÇÃO / DISTRIBUIÇÃO DE LICENSAS 

1- As licensas devem ser inseridas  no campo "productkey" do arquvio "exemplo.json". Esta deve ser igual a uma das licensas que foram inseridas no banco de dados previamente. 

Nota: O campo "headless" é responsável por mostrar a manipulação do navegador, para habilitar esta função insira o parâmetro "True"


```
{
"Login": "email_de_login_do_usuário",
"Password": "senha",
"Horario_de_execucao": "",
"id": "link_de_perfil_do_usuário",
"headless": "False", 
"lastcheckbox": "True",
"productkey": "Ms215yNTil7920gwxdNA"
}

```

### ⚙️ Executando o programa

O código executa um processo de comparação entre a licensa no arquivo o código no servidor. A fim de adicionar mais segurança na verificação do usuário, existe a captura do MACadress para cada licensa no primeiro uso. O cruzamento e verificação destas informações permite a utilização do programa. 


A GUI é interativa e possui as opções de adicionar perfis baseados nas sugestões enviadas pela própria rede do Linkedin. Também é possivel remover solicitações antigas, pois o código mantém uma lista atualizada com as solicitações enviadas ("followed.json") e removidas ("unfollowed.json")

"followed.json"
```
[
[
"BELTRANO",
"01/01/1900"
],
[
"FULANO",
"01/01/1900"
]
]

```

"unfollowed.json"
```
[
[
"CICLANO",
"01/01/1900"
]
]

```
### 📨 Distribuição

É possivel efetuar a distribuição para usuários que não possuem pyton instalados em suas máquinas através da biblioteca pyinstaller. 

```
pip install pyinstaller 

```

O arquivo utilizado "linkedin-automation-exe.spec" foi criado através do exemplo de código abaixo

```
pyi-makespec main.py --onefile --icon=icon.ico --add-binary "driver\geckodriver.exe;driver\" --add-data "example.json;." --add-data "example.ini;." --add-data "followed.json;." --add-data "unfollowed.json;." --name linkedin-automation-exe

```

A compilação poderá ser fetuada conforme código abaixo

```
pyinstaller --clean linkedin-automation-exe.spec

```


## 📦 Desenvolvimento

Lauro Cerqueira
* [LinkedIn:](https://www.linkedin.com/in/lauro-cerqueira-70473568/)
* [Instagram:](laurorcerqueira)

## 🛠️ Construído com

* [Selenium](https://www.selenium.dev/documentation/webdriver/)
* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [Gecko Webdriver](https://github.com/mozilla/geckodriver/releases) 
* [Mongo DB](https://www.mongodb.com/)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 

* Conte a outras pessoas sobre este projeto 📢
* Convide alguém da equipe para uma cerveja 🍺 
* Obrigado publicamente 🤓.

