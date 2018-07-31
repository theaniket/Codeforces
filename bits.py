class Main:

    def __init__(self, name, age, date_of_birth):
        self.__name = name
        self.__age = age
        self.__date_of_birth = date_of_birth

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


def main():
    d = dict()
    d["integer_values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for key, value in d.items():
        if type(value) == list:
            print(x for x in value)
    test_cases = int(input())
    answer = 0
    while test_cases > 0:
        operation = input()
        if operation.startswith('++') or operation.endswith('++'):
            answer += 1
        else:
            answer -= 1
        test_cases -= 1
    print(answer)
    # new part


if __name__ == '__main__':
    main()