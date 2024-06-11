# TPC5: Vending Machine
## 2024-03-12

## Autor:
- a95454
- Lara Beatriz Pinto Ferreira

## Resumo
Programa que simula uma máquina de vending.
Temos o stock.json com o nome do produto, quantidade e preço.

O utilizador pode recorrer às seguintes operações:

- LISTAR -> apresenta os produtos disponiveis

- MOEDA seguido de um conjunto de moedas separadas por vírgulas (MOEDA 1e, 20c) -> carrega o saldo que vai ser correspondente à soma das moedas 

- SELECIONAR seguido do id de um produto -> caso tenha saldo suficiente para a compra do produto selecionado, retira esse valor ao saldo e devolve o troco caso contrário dá erro

- SAIR -> termina a execução do programa

## Funcionamento
```bash
>> LISTAR
cod        | nome                 | quantidade | preço     
------------------------------------------------------------
A23        | Àgua 0.5L            | 7          | 1.00      
A13        | Batatas Fritas       | 10         | 1.20      
A31        | Barra de Chocolate   | 5          | 1.00      
A05        | Refrigerante         | 15         | 1.80      
A18        | Sandes de Frango     | 3          | 3.50      
A15        | Sandes Vegetariana   | 2          | 3.20      
A02        | Pacote de Bolachas   | 8          | 0.80      
A20        | Gomas                | 7          | 1.70      
A12        | Lenços               | 11         | 0.30      
A09        | Amendoins            | 1          | 0.90      
>> MOEDA 1e, 20c
maq: Saldo 1e20c
>> SELECIONAR A13
Pode retirar o produto: Batatas Fritas
Retire o troco: 0e00c
>> MOEDA 1e
maq: Saldo 1e00c
>> SELECIONAR A12
Pode retirar o produto: Lenços
Retire o troco: 0e70c
>> SAIR
```