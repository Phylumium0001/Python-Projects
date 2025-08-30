import random


def generate_user_id():
    # Generate a four letter random user id
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lower_case = [chr(i) for i in range(65, 91)]
    upper_case = [chr(i) for i in range(97, 123)]

    options = [nums, lower_case, upper_case]

    id = ''

    for _ in range(4):
        options_rand = random.randint(0, len(options)-1)
        other_rand = random.randint(0, len(options[options_rand])-1)

        id += str(options[options_rand][other_rand])

    return id
