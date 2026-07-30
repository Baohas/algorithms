#region -------FIND ONE LARGEST NUMBER FROM ARRAY----------
def find_max(A : list):
    for v in A: #перебор всех элементов в массиве (если они есть)
        for x in A: #перебор остальных элементов
            if v < x: break #если нашелся элемент больше - переходим к след элементу
        else:
            return v #если не нашлось эл-тов больше - возврат этого элемента
    return None #возврат None если нет элементов
# endregion

#region -------FIND TWO LARGEST FROM ARRAY------------
def sort_two(A: list): #создаем новый кортеж, сортируем по убыванию и возвращаем первые два эл-та
    return tuple(sorted(A, reverse=True)[:2])

def double_two(A: list):
    max_first = max(A) #ищем макс из ориг. массива
    copy = list(A) #дублируем массив
    copy.remove(max_first) #выбрасываем из него найденный максимум
    return (max_first, max(copy)) #возврат найденного макс. и макс из дублиров. массива

def mutable_two(A: list):
    idx = max(range(len(A)), key=A.__getitem__) #ловим индекс макс эл-та
    first_max = A[idx]
    del A[idx]
    second_max = max(A)
    A.insert(idx, first_max)
    return first_max, second_max

def tournament_two(A: list): #применимо для четного кол-ва элементов
    N = len(A)
    #будем хранить индексы победителей и проигравших
    winner = [None] * (N - 1)
    loser = [None] * (N - 1)
    prior = [-1] * (N - 1)
    idx = 0
    for i in range(0, N, 2): #первый тур
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx+=1
        #игры победителей во всех последующих турах с записью позиции победителей
    m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
            winner[idx] = winner[m + 1]
            loser[idx] = winner[m]
            prior[idx] = m + 1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m+1]
            prior[idx] = m
        m += 2 #игра двух след победителей
        idx += 1
    largest = winner[m] #первый кандидат
    second = loser[m] #два кандидата на второе место
    m = prior[m]
    while m >= 0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]
    return largest, second
#endregion
