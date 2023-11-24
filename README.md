# README

Este README documenta as etapas necessárias para colocar seu aplicativo em funcionamento.

### Para que serve este repositório?

* Este repositorio serve para armazenar e gerenciar as versoes do projeto desenvolvido no ambito ca Unidade Curricular Ambiente de Desenvolvimento Colaborativo. Permite a vizualização das alteracoes realizadas pelos colabradores sendo tambem possivel reverte-las
  facilitando assim o trabalho em equipa e a manutencao do codigo.
  

### Como faço para configurar?

* Configuração

     É necessario ter instalado a versão 3.10 do python e criar um ambiente virtual
  
* Dependências

    Para criar um ambiente virtual

    ```
    $ python -m venv .venv
	```
	
	Depois, é necessário ativar o ambiente virtual
	
	```
    $ .venv\Scripts\activate
    ```

    e depois instalar as livrarias necessárias

    ```
    $ pip install -r requirements.txt
    ```

* Configuração de banco de dados
  
     É necessario executar o ficheiro script_base_dados.py e de seguida executar também o ficheiro script_base_dados.py. Ambos os ficheiros estão inseridos no dieretorio base_dados do projeto.

#### Documentação

Para gerar a configuração para o sphinx, crie uma pasta com o nome `doc`, e mude para essa pasta

```
$ mkdir doc
$ cd doc
```

e depois escreva o comando abaixo, alterando o nome do(s) autor(es), e o nome da aplicação:

```
$ sphinx-apidoc -F -f -A "nome do autor" -V 0 -R 0.1 -H "nome da aplicação" -e -P -a --ext-autodoc --ext-viewcode --ext-todo -o . ./../src/
```

Posteriormente deve configurar o ficheiro `doc\config.py` com as alterações que entenda necessárias


### Com quem devo falar?

* Tomás Anastácio, Diogo Rodrigues, Bernardo Freitas
