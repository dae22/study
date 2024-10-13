N = 500
A = [True] * N # Создается список из N значений True, в данной вариации мы рассматриваем индексы как числа (то есть предварительно все числа простые)
for k in range(2, N): # Так как 0 и 1 условно простые, цикл начинаем с 2
    if A[k]: # Если значение текущей ячейки до этого не было обнулено (False), значит в этой ячейке содержится простое число
        for i in range(k*k, N, k): # Первое кратное ему будет в два раза больше и так далее с шагом k
            A[i] = False # Это уже составное число и поэтому заменяем его на False

for i in range(N):
    if A[i]: print(i, end=' ')
