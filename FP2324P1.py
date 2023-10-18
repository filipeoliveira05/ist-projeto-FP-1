def eh_territorio(t):
    """
    Recebe um argumento de qualquer tipo.
    Devolve True se o seu argumento corresponde a um território e False caso contrário.
    Nunca gera erros.

    :param t: Add Type
    :return: Add Type
    """

    if not isinstance(t, tuple):
        return False
    elif isinstance(t, tuple):
        for i in t:
            if not isinstance(i, tuple):
                return False
    
    if len(t) == 0 or len(t) > 26:
        return False
    
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

    :param t: Tuple
    :return: Tuple
    """

    Nv = min(26, len(t))
    Nh = min(99, len(t[0]))

    i_vertical = chr(ord("A") + Nv - 1)

    return (i_vertical, Nh)



def eh_intersecao(arg):
    """
    Recebe um argumento de qualquer tipo.
    Devolve True se o argumento corresponde a uma interseção e False caso contrário.
    Nunca gera erros.

    :param arg: Add Type
    :return: Add Type
    """

    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
    
    letter, number = arg

    if not isinstance(letter,str) or len(letter) != 1 or not ord('A') <= ord(letter) <= ord('Z'):
        return False
    if not isinstance(number, int) or not 1 <= number <= 99:
        return False
    return True



def eh_intersecao_valida(t, i):
    """
    Recebe um território e uma interseção.
    Devolve True se a interseção corresponde a uma interseção do território, e False caso contrário.

    :param t: Add Type
    :param i: Add Type
    :return: Add Type
    """

    letter, number = i
    Nv = len(t)
    Nh = len(t[0])

    if not ord('A') <= ord(letter) <= (ord('A') + Nv - 1) or not 1 <= number <= Nh:
        return False
    return True



def eh_intersecao_livre(t, i):
    """
    Recebe um território e uma interseção do território.
    Devolve True se a interseção corresponde a uma interseção livre (não ocupada por montanhas) dentro do território e False caso contrário.

    :param t: Add Type
    :param i: Add Type
    :return: Add Type
    """

    letter, number = i
    column = ord(letter) - ord('A')
    row = number

    if 0 <= column < len(t) and 1 <= row <= len(t[0]):
        if t[column][row - 1] == 0:
            return True
    return False



def obtem_intersecoes_adjacentes(t, i):
    """
    Recebe um território e uma interseção do território.
    Devolve o tuplo formado pelas interseções válidas adjacentes da interseção em ordem de leitura de um território.

    :param t: Add Type
    :param i: Add Type
    :return: Add Type
    """

    letter, number = i
    Nv = len(t)
    Nh = len(t[0])
    i_adjacents = []
    
    i_adjacents_possible = [
        (chr(ord(letter)), number - 1),
        (chr(ord(letter) - 1), number),
        (chr(ord(letter) + 1), number),
        (chr(ord(letter)), number + 1),
    ]
    
    for v in i_adjacents_possible:
        if (ord('A') <= ord(v[0]) <= ord('A') + Nv - 1) and 1 <= v[1] <= Nh:
            i_adjacents.append(v)

    return tuple(i_adjacents)



def ordena_intersecoes(tup):
    """
    Recebe um tuplo de interseções (potencialmente vazio).
    Devolve um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura do território.

    :param tup: Add Type
    :return: Add Type
    """

    if len(tup) == 0:
        return ()
    
    letters_sorted = []
    for counter_letters in range(26):
        for i in tup:
            if ord(i[0]) == ord('A') + counter_letters:
                letters_sorted.append(i)

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

    :param t: Add Type
    :return: Add Type
    """

    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')
    
    Nv = len(t)
    Nh = len(t[0])
    t_formatted = ''

    letters = ' '.join([chr(65 + i) for i in range(Nv)])
    t_formatted += '   ' + letters + '\n'

    for row in range(Nh - 1, -1, -1):
        t_formatted += str(row + 1).rjust(2) + ' '
        for column in range(Nv):
            element = t[column][row]
            if element == 0:
                t_formatted += '. '
            else:
                t_formatted += 'X '
        t_formatted += str(row + 1).rjust(2) + '\n'
    t_formatted += '   ' + letters
    
    return t_formatted



def obtem_cadeia(t, i):
    """
    Recebe um território e uma interseção do território (ocupada por uma montanha ou livre).
    Devolve o tuplo formado por todas as interseções que estão conetadas a essa interseção ordenadas (incluída si própria) de acordo com a ordem de leitura de um território.
    Se algum dos argumentos dado for inválido, gera um erro.

    :param t: Add Type
    :param i: Add Type
    :return: Add Type
    """

    if not eh_territorio(t) or not eh_intersecao(i) or not eh_intersecao_valida(t, i):
        raise ValueError('obtem_cadeia: argumentos invalidos')

    list_final = []
    queue = [i]

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

    :param t: Add Type
    :param i: Add Type
    :return: Add Type
    """

    if not eh_territorio(t) or not eh_intersecao_valida(t, i) or eh_intersecao_livre(t, i):
        raise ValueError('obtem_vale: argumentos invalidos')

    all = list(obtem_cadeia(t, i))
    result = []

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

    :param t: Add Type
    :param i1: Add Type
    :param i2: Add Type
    :return: Add Type
    """

    if not eh_territorio(t) or not eh_intersecao_valida(t, i1) or not eh_intersecao_valida(t, i2):
        raise ValueError('verifica_conexao: argumentos invalidos')
    
    chain1 = obtem_cadeia(t, i1)
    chain2 = obtem_cadeia(t, i2)

    if i1 in chain2 and i2 in chain1:
        return True
    return False



def calcula_numero_montanhas(t):
    """
    Recebe um território.
    Devolve o número de interseções ocupadas por montanhas no território.
    Se o argumento dado for inválido, gera um erro.

    :param t: Add Type
    :return: Add Type
    """

    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    
    Nv = len(t)
    Nh = len(t[0])
    number_mountains = 0

    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1:
                number_mountains += 1
    
    return number_mountains



def calcula_numero_cadeias_montanhas(t):
    """
    Recebe um território.
    Devolve o número de cadeias de montanhas contidas no território.
    Se o argumento dado for inválido, gera um erro.

    :param t: Add Type
    :return: Add Type
    """

    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    
    Nv = len(t)
    Nh = len(t[0])

    mountains_coordinates = []
    for v in range(Nv):
        for h in range(Nh):
            if t[v][h] == 1:
                coordinates = ()
                coordinates += (chr(ord('A') + v), h + 1)
                mountains_coordinates.append(coordinates)

    chains = []
    for i in mountains_coordinates:
        if obtem_cadeia(t, i) not in chains:
            chains.append(obtem_cadeia(t, i))
    return len(chains)



def calcula_tamanho_vales(t):
    """
    Recebe um território.
    Devolve o número total de interseções diferentes que formam todos os vales do território.
    Se o argumento dado for inválido, gera um erro.

    :param t: Add Type
    :return: Add Type
    """

    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    
    Nv = len(t)
    Nh = len(t[0])

    coordinates = []
    for number in range(1, Nh + 1):
        for letter in range(ord('A'), ord('A') + Nv):
            coordinates.append((chr(letter), number))
    
    valleys = []
    for i in coordinates:
        if not eh_intersecao_livre(t, i):
            adjacents = obtem_intersecoes_adjacentes(t, i)
            for adjacent in adjacents:
                if eh_intersecao_livre(t, adjacent) and adjacent not in valleys:
                    valleys.append(adjacent)
    
    return(len(valleys))

