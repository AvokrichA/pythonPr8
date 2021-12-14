class MyException(Exception):
    def __init__(self, text):
        self.text = text

try:
    a = float(input('Введите делимое:'))
    b = float(input('Введите делитель: b = '))
    if b==0:
        raise MyException('На 0 делить нельзя!')
    else:
        result = a/b
        print(result)
except MyException as e:
    print(e)
    print('Program does not stopped')
