import json
import ply.lex as lex


with open('stock.json') as stock_json:
    bd = json.load(stock_json)


moedas =[("2e",2.00),("1e",1.00),("50c",0.50),("20c",0.20),("10c",0.10),("5c",0.05),("2c",0.02),("1c",0.01)]
saldo = 0

def moeda_to_Num(d):
    r = None
    for (m, n) in moedas:
        if m == d:
            r = n
    return round(r, 2) if r is not None else None

def num_to_moeda (d):
    inteiro, decimal = str("{:.2f}".format(d)).split('.')
    return f"{inteiro}e{decimal}c"



tokens = (
    'LISTAR',
    'MOEDA',
    'DINHEIRO',
    'SELECIONAR',
    'PRODUTO',
    'VIRGULA',
    'PONTO',
    'SAIR'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_DINHEIRO = r'\d{1,2}[ec]'
t_SELECIONAR = r'SELECIONAR'
t_PRODUTO = r'A\d{2}'
t_VIRGULA = r','
t_PONTO = r'\.'
t_SAIR = r'SAIR'


t_ignore = " \t"

def t_error(t):
    print("Caracter ilegal '%s'" + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

ligada = True

while ligada==True:
    comando = input('>> ')
    lexer.input(comando)
    tok = lexer.token()
    if tok.type=="MOEDA":
        for tok in lexer:
            if(tok.type == "DINHEIRO"):
                saldo += moeda_to_Num(tok.value)
        saldo_str = f'maq: Saldo {num_to_moeda(saldo)}'
        print(saldo_str)
    elif tok.type=="LISTAR":
        print (f"{'cod':<10} | {'nome':<20} | {'quantidade':<10} | {'preço':<10}")
        print ('-' * 60)
        for p in bd["stock"]:
            print(f"{p['cod']:<10} | {p['nome']:<20} | {p['quant']:<10} | {p['preco']:<10.2f}")
    elif tok.type=="SELECIONAR":
        tok = lex.token()
        id = tok.value
        for prod in bd['stock']: 
            if prod['cod'] == id:
                if prod['preco'] <= saldo:
                    if prod['quant'] > 0:
                        troco = saldo - prod['preco']
                        prod['quant'] -= 1
                        print(f"Pode retirar o produto: {prod['nome']}")
                        if troco >= 0:
                            print(f"Retire o troco: {num_to_moeda(troco)}")
                        saldo = 0
                        troco = 0
                    else:
                        print("Produto sem stock")
                else:
                    print(f"Saldo insuficiente: \nSaldo: {saldo}\nPreço do produto: {prod['preco']}")
    elif tok.type=="SAIR":
        ligada = False
    else:
        print("Comando não suportado")

with open('stock.json', 'w') as stock_json:
    json.dump(bd, stock_json, indent=4)
