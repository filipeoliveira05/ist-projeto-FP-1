def eh_territorio(t):
    """
    Recebe um argumento de qualquer tipo.
    Devolve True se o seu argumento corresponde a um território e False caso contrário.
    Nunca gera erros.

    :param t: tuple
    :return: bool
    """
    #verifica se o argumento é constituído por tuplos dentro de um tuplo.
    if not isinstance(t, tuple): 
        return False
    elif isinstance(t, tuple):
        for i in t:
            if not isinstance(i, tuple):
                return False

    #verifica se o número de caminhos verticais está fora do intervalo válido.
    if len(t) == 0 or len(t) > 26:
        return False
    
    #verifica se o número de caminhos horizontais está fora do intervalo válido, ou se algum dos elementos não é válido.
    for v in range(len(t)):
        if len(t[v]) != len(t[0]) or len(t[v]) > 99 or not isinstance(t[v], tuple):
            return False
        for h in range(len(t[v])):
            if (t[v][h] != 0 and t[v][h] != 1) or not isinstance(t[v][h], int):
                return False
    
    return True



def obtem_ultima_intersecao(t):
    """
    Recebe um territorio.
    Devolve a interseção do extremo superior direito do território.

    :param t: tuple
    :return: tuple
    """

    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    #obtém o string correspondente ao código numérico da letra do último caminho vertical.
    i_vertical = chr(ord("A") + Nv - 1)

    return (i_vertical, Nh)



def eh_intersecao(arg):
    """
    Recebe um argumento de qualquer tipo.
    Devolve True se o argumento corresponde a uma interseção e False caso contrário.
    Nunca gera erros.

    :param arg: any type
    :return: bool
    """
    #verifica se o argumento é válido.
    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
    
    #definição do argumento (tuplo, onde o primeiro elemento corresponde à variável letter e o segundo à variável number).
    letter, number = arg

    #verifica se as variáveis letter e number são válidas.
    if not isinstance(letter,str) or len(letter) != 1 or not ord('A') <= ord(letter) <= ord('Z'):
        return False
    if not isinstance(number, int) or not 1 <= number <= 99:
        return False
    return True



def eh_intersecao_valida(t, i):
    """
    Recebe um território e uma interseção.
    Devolve True se a interseção corresponde a uma interseção do território, e False caso contrário.

    :param t: tuple
    :param i: tuple
    :return: bool
    """

    #definição do argumento (tuplo, onde o primeiro elemento corresponde à variável letter e o segundo à variável number).
    letter, number = i

    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    #verifica se as variáveis letter e number são válidas.
    if not ord('A') <= ord(letter) <= (ord('A') + Nv - 1) or not 1 <= number <= Nh:
        return False
    
    return True



def eh_intersecao_livre(t, i):
    """
    Recebe um território e uma interseção do território.
    Devolve True se a interseção corresponde a uma interseção livre (não ocupada por montanhas) dentro do território e False caso contrário.

    :param t: tuple
    :param i: tuple
    :return: bool
    """

    #definição do argumento (tuplo, onde o primeiro elemento corresponde à variável letter e o segundo à variável number).
    letter, number = i

    #definição de coluna e linha específica do território.
    column = ord(letter) - ord('A')
    row = number

    #verifica se as variáveis column e row são válidas.
    if 0 <= column < len(t) and 1 <= row <= len(t[0]):
        if t[column][row - 1] == 0:
            return True

    return False



def obtem_intersecoes_adjacentes(t, i):
    """
    Recebe um território e uma interseção do território.
    Devolve o tuplo formado pelas interseções válidas adjacentes da interseção em ordem de leitura de um território.

    :param t: tuple
    :param i: tuple
    :return: tuple
    """

    #definição do argumento (tuplo, onde o primeiro elemento corresponde à variável letter e o segundo à variável number).
    letter, number = i

    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    #definição da lista final com as interseções adjacentes.
    i_adjacents = []
    
    #obtém as quatro interseções adjacentes possíveis, independentemente de serem válidas no território em questão.
    i_adjacents_possible = [
        (chr(ord(letter)), number - 1),
        (chr(ord(letter) - 1), number),
        (chr(ord(letter) + 1), number),
        (chr(ord(letter)), number + 1),
    ]
    
    #verifica, entre as quatro interseções adjacentes possíveis, quais delas são válidas no território em questão.
    for v in i_adjacents_possible:
        if (ord('A') <= ord(v[0]) <= ord('A') + Nv - 1) and 1 <= v[1] <= Nh:
            i_adjacents.append(v)

    return tuple(i_adjacents)



def ordena_intersecoes(tup):
    """
    Recebe um tuplo de interseções (potencialmente vazio).
    Devolve um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do território.

    :param tup: tuple
    :return: tuple
    """
    #caso em que o tuplo de interseções dado como argumento seja vazio.
    if len(tup) == 0:
        return ()
    
    #ordena as interseções dentro do tuplo dado por ordem crescente de letras (caminhos verticais da esquerda para a direita).
    letters_sorted = []
    for counter_letters in range(26):
        for i in tup:
            if ord(i[0]) == ord('A') + counter_letters:
                letters_sorted.append(i)

    #ordena as interseções dentro do tuplo de interseções ordenadas por letras, por ordem crescente de número (caminhos horizontais de baixo para cima)
    numbers_sorted = []
    for counter_num in range(100):
        for i in letters_sorted:
            if i[1] == counter_num:
                numbers_sorted.append(i)
    
    return tuple(numbers_sorted)
    


def territorio_para_str(t):
    """
    Recebe um território.
    Devolve a cadeia de caracteres que o representa (a representação externa ou representação "para os nossos olhos").
    Se o argumento dado for inválido, gera um erro.

    :param t: tuple
    :return: str
    """
    #caso o território dado como argumento seja inválido, a função gera um erro.
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')
    
    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    #definição da variável que irá armazenar a representação visual do território.
    t_formatted = ''

    #definição da variável letters que representa os 'rótulos' das colunas (de 'A' a 'Z', dependendo do número de caminhos verticais)
    letters = ' '.join([chr(65 + i) for i in range(Nv)])
    
    #adiciona 'rótulos' das colunas com espaço de avanço à esquerda na primeira linha de representação.
    t_formatted += '   ' + letters + '\n'

    #iteração pelos caminhos horizontais do território de cima para baixo
    for row in range(Nh - 1, -1, -1):
        #adiciona o número do caminho horizontal com espaço de avanço à esquerda. 
        t_formatted += str(row + 1).rjust(2) + ' '
        for column in range(Nv):
            element = t[column][row]
            #verifica o valor de cada interseção (se for 0, adiciona um ponto, '.', à string de formatação, e um 'X' se for 1).
            if element == 0:
                t_formatted += '. '
            else:
                t_formatted += 'X '
        #repete o número do caminho horizontal à direita.
        t_formatted += str(row + 1).rjust(2) + '\n'
    #adiciona 'rótulos' das colunas com espaço de avanço à esquerda na última linha de representação.
    t_formatted += '   ' + letters
    
    return t_formatted



def obtem_cadeia(t, i):
    """
    Recebe um território e uma interseção do território (ocupada por uma montanha ou livre).
    Devolve o tuplo formado por todas as interseções que estão conetadas a essa interseção ordenadas (incluída si própria) de acordo com a ordem de leitura de um território.
    Se algum dos argumentos dado for inválido, gera um erro.

    :param t: tuple
    :param i: tuple
    :return: tuple
    """

    #caso algum dos argumentos dado for inválido, a função gera um erro.
    if not eh_territorio(t) or not eh_intersecao(i) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')

    #variável que armazena os resultados finais
    list_final = []

    #lista com as interseções por 'validar', antes de poder entrar na lista final
    queue = [i]

    #'current' é a variável com a interseção que está a ser analisada no momento.
    #'adjacents' é a variável com as interseções adjacentes da interseção do 'current'.

    #Lógica: 
    #1 - retirar o primeiro elemento do 'queue' e atribuir ao 'current'.
    #2 - se o 'current' não estiver na lista final, é adicionado.
    #3 - obtem-se as interseções adjacentes e são atribuídas à 'adjacent'.
    #4 - por cada elemento no 'adjacent', caso não esteja já no 'queue' e seja do mesmo tipo (livre ou não livre) da 'current', adicionar ao 'queue'.
    #5 - processo repete-se até a 'queue' não ter nenhum elemento.
    while queue:
        current = queue.pop(0)
        if current not in list_final:
            list_final.append(current)
            adjacents = obtem_intersecoes_adjacentes(t, current)
            for adjacent in adjacents:
                if eh_intersecao_livre(t, adjacent) == eh_intersecao_livre(t, current) and adjacent not in queue:
                    queue.append(adjacent)

    return ordena_intersecoes(tuple(list_final))



def obtem_vale(t, i):
    """
    Recebe um território e uma interseção do território ocupada por uma montanha.
    Devolve o tuplo (potencialmente vazio) formado por todas as interseções que formam parte do vale da montanha da interseção fornecia como argumento ordenadas de acordo à ordem de leitura de um território.
    Se algum dos argumentos dado for inválido, gera um erro.

    :param t: tuple
    :param i: tuple
    :return: tuple
    """

    #caso algum dos argumentos dado for inválido, a função gera um erro.
    if not eh_territorio(t) or not eh_intersecao_valida(t, i) or eh_intersecao_livre(t, i):
        raise ValueError('obtem_vale: argumentos invalidos')

    #obtém a lista com as interseções da cadeia que contém a interseção dada.
    all = list(obtem_cadeia(t, i))

    result = []

    #Lógica:
    #1 - por cada interseção em 'all', obter as suas interseções adjacentes.
    #2 - por cada interseção nesse grupo de adjacentes, caso esta seja livre e não esteja já no resultado final, adicionar ao resultado.
    for i in all:
        adjacents = obtem_intersecoes_adjacentes(t, i)
        for adjacent in adjacents:
            if eh_intersecao_livre(t, adjacent) and adjacent not in result:
                result.append(adjacent)
    
    return ordena_intersecoes(tuple(result))
    


def verifica_conexao(t, i1, i2):
    """
    Recebe um território e duas interseções do território.
    Devolve True se as duas interseções estão conectadas e False caso contrário.
    Se algum dos argumentos dado for inválido, gera um erro.

    :param t: tuple
    :param i1: tuple
    :param i2: tuple
    :return: bool
    """

    #caso algum dos argumentos dado for inválido, a função gera um erro.
    if not eh_territorio(t) or not eh_intersecao_valida(t, i1) or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    #variáveis que armazenam as cadeias das interseções dadas como argumento.
    chain1 = obtem_cadeia(t, i1)
    chain2 = obtem_cadeia(t, i2)

    #caso a interseção1 esteja na cadeia da interseção2 e caso a interseção2 esteja na cadeia da interseção1, retorna True.
    if i1 in chain2 and i2 in chain1:
        return True
    return False



def calcula_numero_montanhas(t):
    """
    Recebe um território.
    Devolve o número de interseções ocupadas por montanhas no território.
    Se o argumento dado for inválido, gera um erro.

    :param t: tuple
    :return: int
    """
    #caso o argumento dado seja inválido, a função gera um erro.
    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    
    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    number_mountains = 0

    #iteração pelos caminhos verticais e horizontais do território para verificar quais interseções são ocupadas por montanhas.
    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1:
                number_mountains += 1
    
    return number_mountains



def obtem_coordenadas(t):
    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])
    
    #obtém as "coordenadas" das interseções do território dado.
    coordinates = []
    for number in range(1, Nh + 1):
        for letter in range(ord('A'), ord('A') + Nv):
            coordinates.append((chr(letter), number))
    
    return coordinates



def calcula_numero_cadeias_montanhas(t):
    """
    Recebe um território.
    Devolve o número de cadeias de montanhas contidas no território.
    Se o argumento dado for inválido, gera um erro.

    :param t: tuple
    :return: int
    """
    
    #caso o argumento dado seja inválido, a função gera um erro.
    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    #obtém as "coordenadas" das interseções do território dado.
    coordinates = obtem_coordenadas(t)
    
    #itera pelas coordenadas e, caso seja não seja uma interseção livre e a cadeia dela não estiver no reusltado final, adicionar a cadeia ao resultado
    chains = []
    for i in coordinates:
        if not eh_intersecao_livre(t, i) and obtem_cadeia(t, i) not in chains:
            chains.append(obtem_cadeia(t, i))
    
    return len(chains)



def calcula_tamanho_vales(t):
    """
    Recebe um território.
    Devolve o número total de interseções diferentes que formam todos os vales do território.
    Se o argumento dado for inválido, gera um erro.

    :param t: tuple
    :return: bool
    """

    #caso o argumento dado seja inválido, a função gera um erro.
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    #definição de número de caminhos verticais e horizontais.
    Nv = len(t)
    Nh = len(t[0])

    #obtém as "coordenadas" das interseções do território dado.
    coordinates = []
    for number in range(1, Nh + 1):
        for letter in range(ord('A'), ord('A') + Nv):
            coordinates.append((chr(letter), number))
    
    #Lógica:
    #1 - itera pelas coordenadas, e caso não corresponda a uma interseção livre, obtem-se as suas adjacentes
    #2 - itera pelas adjacentes, e caso estas sejam interseções livres e não estejam no resultado final, adiciona-as ao resultado
    valleys = []
    for i in coordinates:
        if not eh_intersecao_livre(t, i):
            adjacents = obtem_intersecoes_adjacentes(t, i)
            for adjacent in adjacents:
                if eh_intersecao_livre(t, adjacent) and adjacent not in valleys:
                    valleys.append(adjacent)
    
    return(len(valleys))