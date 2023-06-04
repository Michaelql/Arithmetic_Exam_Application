# write your code here
import random


def level_1() -> bool:
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    op = random.choice(['+', '-', '*'])
    out_dict = {'+': a + b, '-': a - b, '*': a * b}
    print(a, op, b)
    while True:
        try:
            user_answer = int(input())
            if out_dict.get(op) == user_answer:
                return True
            return False
        except:
            print('Incorrect format.')


def level_2() -> bool:
    a = random.randint(11, 29)
    print(a)
    while True:
        try:
            user_answer = int(input())
            if user_answer == a ** 2:
                return True
            return False
        except:
            print('Incorrect format.')


while True:
    print('Which level do you want? Enter a number:\n'
          '1 - simple operations with numbers 2-9\n'
          '2 - integral squares of 11-29')
    level = int(input())
    if level in (1, 2):
        break
    else:
        print('Incorrect format')
right_num = 0
for _ in range(5):
    if level_1() if level == 1 else level_2():
        print('Right!')
        right_num += 1
    else:
        print('Wrong!')
print(f'Your mark is {right_num}/5. Would you like to save the result? Enter yes or no.')
if input() in ('yes', 'YES', 'y', 'Yes'):
    user_name = input('What is your name?')
    description_1 = 'simple operations with numbers 2-9'
    description_2 = 'integral squares of 11-29'
    with open('results.txt', 'a') as f:
        f.write(f'{user_name}: {right_num}/5 in level {level} ({description_1 if level == 1 else description_2}).')
    print('The results are saved in "results.txt".')
