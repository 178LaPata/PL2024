def parser_csv(file):
    with open(file, 'r') as f:
        data = f.read()
    data = data.split('\n')
    data = [i.split(',') for i in data]
    data = data[1:]
    d = {}
    for i in data:
        if len(i) >= 13:
            d[i[0]] = {
                'index': i[1],
                'dataEMD': i[2],
                'nome': i[3] + ' ' + i[4],
                'idade': i[5],
                'genero': i[6],
                'morada': i[7],
                'modalidade': i[8],
                'clube': i[9],
                'email': i[10],
                'federado': i[11],
                'resultado': i[12]
            }
    return d

def modalidades(dados):
    modalidades = []
    for i in dados:
        modalidades.append(dados[i]['modalidade'])
    modalidades = list(set(modalidades))
    modalidades.sort()
    return modalidades

def percentagens(dados):
    aptos = 0
    inaptos = 0
    for i in dados:
        if dados[i]['resultado'] == 'true':
            aptos += 1
        else:
            inaptos += 1
    return (aptos/len(dados))*100, (inaptos/len(dados))*100

def distribuicao(dados):
    distribuicao = {f"[{i*5}-{i*5 + 4}]": 0 for i in range(8)}
    for i in dados:
        idade = int(dados[i]['idade'])
        if 0 <= idade <= 39:
            escalao = (idade // 5) * 5 
            escalao_label = f"[{escalao}-{escalao + 4}]" 
            distribuicao[escalao_label] += 1
    return distribuicao

dados = parser_csv("emd.csv")
dist = distribuicao(dados)

print("A lista de modalidades ordenadas alfabeticamente é: ", modalidades(dados))

print("A percentagem de atletas aptos é de: ", percentagens(dados)[0], "%")
print("A percentagem de atletas inaptos é de: ", percentagens(dados)[1], "%")

print("Distribuição de atletas por escalão etário:")
for escalao, quantidade in sorted(dist.items(), key=lambda item: int(item[0].split('-')[0][1:])):
    print(f"{escalao}: {quantidade} atletas")