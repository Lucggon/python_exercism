class YearValidation:
    @staticmethod
    def isLeapYear(year):
        lista = {year%x for x in [4,100,400]}
        print(sum(lista) > 0 and "not leap year" or "leap year")

    