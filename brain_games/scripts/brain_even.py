from random import randint

import prompt


def greeting():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question():
    rand_int = randint(1, 1000)
    print(f'Question: {rand_int}')
    return rand_int


def answer():
    answer = prompt.string('Your answer: ')
    return answer


def check(answer, rand_int):
    if answer == "yes" and rand_int % 2 == 0:
        return True
    elif answer == "no" and rand_int % 2 == 1:
        return True
    else:
        return False
    

def main():
    greeting()
    user_name = welcome_user()
    game_rules()
    counter = 0
    while counter < 3:
        rand_int = question()
        user_answer = answer()
        if check(user_answer, rand_int):
            print('Correct')
            counter += 1
        else:
            if rand_int % 2 == 0:
                print(f"'{user_answer}' is wrong answer :(.Correct answer was 'yes'")
            else:
                print(f"'{user_answer}' is wrong answer :(.Correct answer was 'no'")
            print(f"Let's try again, {user_name}!")
            break
    if counter == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
