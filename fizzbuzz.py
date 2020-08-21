class FizzNum:
    def __init__(self, num, string):
        nums.append(self)
        self.num = num
        self.string = string
    def check(self, num):
        return self.string if (num % self.num == 0) else ''
nums = []
FizzNum(3, "Fizz")
FizzNum(5, "Buzz")

for i in range(100 + 1):
    fizzString = ''
    for obj in nums:
        fizzString += obj.check(i)
    if fizzString == '':
        print(i)
    else:
        print(fizzString)
