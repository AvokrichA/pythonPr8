class TypeError(Exception):
    pass

b=[]

while True:
    try:
        a = input('Введите число:')
        if a=='stop':
            break

        if not a.isdigit():
            raise TypeError('Введите числовое значение:')
        b.append(int(a))

    except TypeError as e:
        print(e)

print(b)
