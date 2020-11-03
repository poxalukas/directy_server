o projeto possui 4 arquivos, sendo eles:
====================================================================================================================================
directory.py
Servidor de diretorio:
	implementa a classe Directory que usa a tabela registry;

	implementa um servidor rpc e possui 2 metodos, usando o metodo de servidor thread
	
	register: recebe 3 parametros, nome do servidor, numero de ip e numero de porta;
	as 3 sao armazenados na tabela registry, usando o nome como chave, e faz uma tupla com o numero de ip e porta

	na linha print(self.registry) imprimi oque foi salvo e o retorno, informa que a registraçao esta ok;

	lookup:	metodo de decoberta de servidor, onde e passado somente o nome do servidor, e o servidor de diretorio retorna
	a entrada do registro associado ao nome, retornando a tupla de ip e porta;
====================================================================================================================================
server.py
Servidor da aplicaçao:

	Class DBList: e a base de dados

	possui dois metodos, e usa o metodo forking server;

	append: faz um append de um valor da lista do DBList;
	
	value: obtem o valor da lista;

	na var conn ele conecta ao diretorio do servidor e em
	my_addr: obtem o endereço de ip da maquina que esta rodando

	e registra ele mesmo no diretorio do servidor
====================================================================================================================================
constRPYC.py

	arquivo de controle do diretorio do servidor, e porta
	====================================================================================================================================
cliente.py
	conn =  ele conecta ao diretorio do servidor
	em (addr,port) ele faz um loockup

	ja recebido o end de ip e porta,

	ele faz uma conexao com o servidor de aplicaçao
	
	e depois faz a chamada do apend e a quantidade de elementos do apend
	
	e imprimi o resultado





























