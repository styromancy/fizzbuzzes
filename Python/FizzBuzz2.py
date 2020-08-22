'''
Another Python example. I tried to do it in as few lines of code as possible.
It's not particularly readable, manageable, or stylish, but it was a
fun challenge.
'''
for i in range(1, 101):
    print("FizzBuzz" if i % 15 == 0 else ("Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else i)))
