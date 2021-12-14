class Data:
    def __init__(self, dd_mm_year):
        self.dd_mm_year = str(dd_mm_year)

    @classmethod
    def date_1(cls, dd_mm_year):
        data = []

        for i in dd_mm_year.split():
            if i != '-': data.append(i)

        return int(data[0]), int(data[1]), int(data[2])

    @staticmethod
    def date_2(dd, mm, year):
        if (1 <= dd <= 31) and (1 <= mm <= 12) and (year >= 0):
            return True
        else:
            return False

    def __str__(self):
        return f'Дата {Data.date_1(self.dd_mm_year)}'

my_day = Data('13 - 12 - 2021')

print(my_day)
print(Data.date_2(11, 11, 2022))
print(my_day.date_2(11, 13, 2021))
print(my_day.date_1('4 - 11 - 2021'))
print(my_day.date_2(15, 11, 2000))