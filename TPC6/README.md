# TPC6: Gramática independente de contexto
## 2024-04-28

## Autor
- A95454
- Lara Beatriz Pinto Ferreira

## Resumo
Programa que simula uma gramática independente de contexto, para os seguintes casos:
- `?a`
- `b=a*2/(27-3)`
- `!a+b`
- `c=a*b/(a/b)`

Ter em comta:
- Prioridade dos operadores
- Garantir que é LL(1)
- Calcular os Look Ahead para todas as regras de produção

## Gramática

### Símbolos Terminais
```
T = {'?', '!', '=', '+', '-', '*', '/', '(', ')', var, num}
```
### Símbolos Não Terminais
```
N = {S, exp1, op1, exp2, op2, exp3}
```
### Símbolo Inicial
```
S = S
```

### Regras de Produção
```
P = {
    S -> '?' var           LA = {'?'}
       | var '=' exp1      LA = {var}
       | '!' exp1          LA = {'!'}

    exp1 -> exp2 op1       LA = {'(', var, num}

    op1 -> '+' exp1        LA = {'+'}
         | '-' exp1        LA = {'-'}
         | ε               LA = {')', $}

    exp2 -> exp3 op2       LA = {'(', var, num}

    op2 -> '*' exp1        LA = {'*'}
         | '/' exp1        LA = {'/'}
         | ε               LA = {')', $}

    exp3 -> '(' exp1 ')'   LA = {'('}
          | var            LA = {var}
          | num            LA = {num}
}
```

