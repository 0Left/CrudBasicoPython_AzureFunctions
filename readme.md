# Me teste
(no bom sentido)
https://pyhttpcrud.azurewebsites.net

# Anotações para quando eu copiar isso no futuro:
* __init__.py é o script central, ele vai ser o "main", ele vai centralizar o roteamento
* pip install -r requirements.txt
* vou usar:
    * FastApi - Pra base de tudo
    * Pydantic - pra verificação de modelo Json (pelo que entendi(pelo visto n entendi))
    * Pymongo - Conecta com o azureMongoDB
--
* Bota na .env a string de conexão com o DB
* Dentro da function.json atualizar o route pra "/{*route}"
* Dentro do host.json adicionar:
    * "extensions":{"http":{"routePrefix":""}}

* E incluir o methods necessários (GET,POST,PUT,DELETE)
    

# objetivo:
* Fazer um crud
    * Read registros
    * Read registro 
    * Create/Update registro
    * Delete registro

# Resultado:
* Fiz um crud
![Alt text](https://i.imgur.com/0L2i2gW.png)
# ToDo:
* separar o put em 2 (1 put, 1 post), para ter caminho de registro e update separado.