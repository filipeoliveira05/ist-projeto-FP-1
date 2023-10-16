def eh_territorio(tuplo):
    if not isinstance(tuplo, tuple): #verifica se o argumento é do tipo tuplo, se não for retorna Falso
        return False
    elif isinstance(tuplo, tuple): #verifica se cada tuplo dentro do argumento é um tuplo, se pelo menos um deles não for, retorna Falso
        for i in tuplo:
            if not isinstance(i, tuple):
                return False
    
    if len(tuplo) == 0 or len(tuplo) > 26: #verifica se o tamanho do tuplo está dentro dos requisitos (maior que 0 e menor ou igual a 26, uma vez que só há 26 letras no alfabeto. Caso não aconteça, retorna Falso)
        return False
    
    for v in range(len(tuplo)):
        if len(tuplo[v]) != len(tuplo[0]) or len(tuplo[v]) > 99 or not isinstance(tuplo[v], tuple):
            return False
        for h in range(len(tuplo[v])):
            if (tuplo[v][h] != 0 and tuplo[v][h] != 1) or not type(tuplo[v][h], int):
                return False
    return True



def obtem_ultima_intersecao(tuplo):
    Nv = min(26, len(tuplo))
    Nh = min(99, len(tuplo[0]))
    intersecao_vertical = chr(ord("A") + Nv - 1)
    return (intersecao_vertical, Nh)



def eh_intersecao(arg):
    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
    
    letra, numero = arg

    if not isinstance(letra,str) or len(letra) != 1 or not ord('A') <= ord(letra) <= ord('Z'):
        return False
    if not isinstance(numero, int) or not 1 <= numero <= 99:
        return False
    return True



def eh_intersecao_valida(tuplo, intersecao):
    letra, numero = intersecao
    Nv = len(tuplo)
    Nh = len(tuplo[0])
    if not ord('A') <= ord(letra) <= (ord('A') + Nv - 1) or not 1 <= numero <= Nh:
        return False
    return True



def eh_intersecao_livre(tuplo, intersecao):
    letra, numero = intersecao
    coluna = ord(letra) - ord('A')
    linha = numero

    if 0 <= coluna < len(tuplo) and 1 <= linha <= len(tuplo[0]):
        if tuplo[coluna][linha - 1] == 0:
            return True
    return False



def obtem_intersecoes_adjacentes(tuplo, intersecao):
    letra, numero = intersecao
    Nv = len(tuplo)
    Nh = len(tuplo[0])
    intersecoes_adjacentes = []
    
    intersecoes_adjacentes_possíveis = [
        (chr(ord(letra)), numero - 1),
        (chr(ord(letra) - 1), numero),
        (chr(ord(letra) + 1), numero),
        (chr(ord(letra)), numero + 1),
    ]
    
    for v in intersecoes_adjacentes_possíveis:
        if (ord('A') <= ord(v[0]) <= ord('A') + Nv - 1) and 1 <= v[1] <= Nh:
            intersecoes_adjacentes.append(v)

    return tuple(intersecoes_adjacentes)



def ordena_intersecoes(tup):
    if len(tup) == 0:
        return ()
    
    letras_ordenadas = []
    for counter_letras in range(26):
        for i in tup:
            if ord(i[0]) == ord('A') + counter_letras:
                letras_ordenadas.append(i)

    numeros_ordenados = []
    for counter_num in range(100):
        for i in letras_ordenadas:
            if i[1] == counter_num:
                numeros_ordenados.append(i)
    
    return tuple(numeros_ordenados)
    


def territorio_para_str(tuplo):
    if not eh_territorio(tuplo):
        raise ValueError('territorio_para_str: argumento invalido')
    
    Nv = len(tuplo)
    Nh = len(tuplo[0])
    tuplo_formatado = ''

    letras = ' '.join([chr(65 + i) for i in range(Nv)])
    tuplo_formatado += '   ' + letras + '\n'

    for linha in range(Nh - 1, -1, -1):
        tuplo_formatado += str(linha + 1).rjust(2) + ' '
        for coluna in range(Nv):
            elemento = tuplo[coluna][linha]
            if elemento == 0:
                tuplo_formatado += '. '
            else:
                tuplo_formatado += 'X '
        tuplo_formatado += str(linha + 1).rjust(2) + '\n'
    tuplo_formatado += '   ' + letras
    
    return tuplo_formatado



def obtem_cadeia(tuplo, intersecao):
    if not eh_territorio(tuplo) or not eh_intersecao(intersecao) or not eh_intersecao_valida(tuplo, intersecao):
        raise ValueError('obtem_cadeia: argumentos invalidos')

    lista_final = []
    queue = [intersecao]

    while queue:
        current = queue.pop(0)
        if current not in lista_final:
            lista_final.append(current)
            adjacentes = obtem_intersecoes_adjacentes(tuplo, current)
            for adjacente in adjacentes:
                if eh_intersecao_livre(tuplo, adjacente) == eh_intersecao_livre(tuplo, current) and adjacente not in queue:
                    queue.append(adjacente)

    return ordena_intersecoes(tuple(lista_final))



def obtem_vale(tuplo, intersecao):
    if not eh_territorio(tuplo) or not eh_intersecao_valida(tuplo, intersecao) or eh_intersecao_livre(tuplo, intersecao):
        raise ValueError('obtem_vale: argumentos invalidos')

    todos = list(obtem_cadeia(tuplo, intersecao))
    resultado = []

    for i in todos:
        adjacent = obtem_intersecoes_adjacentes(tuplo, i)
        for adjacentes in adjacent:
            if eh_intersecao_livre(tuplo, adjacentes) and adjacentes not in resultado:
                resultado.append(adjacentes)
    return ordena_intersecoes(tuple(resultado))
    


def verifica_conexao(tuplo, intersecao1, intersecao2):
    if not eh_territorio(tuplo) or not eh_intersecao_valida(tuplo, intersecao1) or not eh_intersecao_valida(tuplo, intersecao2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    cadeia1 = obtem_cadeia(tuplo, intersecao1)
    cadeia2 = obtem_cadeia(tuplo, intersecao2)

    if intersecao1 in cadeia2 and intersecao2 in cadeia1:
        return True
    return False



def calcula_numero_montanhas(tuplo):
    if not eh_territorio(tuplo):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    
    Nv = len(tuplo)
    Nh = len(tuplo[0])
    numero_montanhas = 0

    for v in range(Nv):
        for h in range(Nh):
            if tuplo[v][h] == 1:
                numero_montanhas += 1
    return numero_montanhas



def calcula_numero_cadeias_montanhas(tuplo):
    if not eh_territorio(tuplo):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    Nv = len(tuplo)
    Nh = len(tuplo[0])

    coordenadas = []
    for numero in range(1, Nh + 1):
        for letra in range(ord('A'), ord('A') + Nv):
            coordenadas.append((chr(letra), numero))
    
    cadeias = []
    for i in coordenadas:
        if not eh_intersecao_livre(tuplo, i) and obtem_cadeia(tuplo, i) not in cadeias:
            cadeias.append(obtem_cadeia(tuplo, i))
    return len(cadeias)



def calcula_tamanho_vales(tuplo):
    if not eh_territorio(tuplo):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    Nv = len(tuplo)
    Nh = len(tuplo[0])

    coordenadas = []
    for numero in range(1, Nh + 1):
        for letra in range(ord('A'), ord('A') + Nv):
            coordenadas.append((chr(letra), numero))
    
    vales = []
    for i in coordenadas:
        if not eh_intersecao_livre(tuplo, i):
            adjacent = obtem_intersecoes_adjacentes(tuplo, i)
            for adjacentes in adjacent:
                if eh_intersecao_livre(tuplo, adjacentes) and adjacentes not in vales:
                    vales.append(adjacentes)
    return(len(vales))