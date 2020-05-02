class Fizzbuzz():

    def __init__(self):
        self.value = 0

    def calculate(self, number:int):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'

        return number



