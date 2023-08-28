import random

# создаем константные переменные
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
off_simb = 'il1Lo0O'
chars = ''

# запрашиваем пользовательский ввод
num_pass = int(input('Введите количество требуемых паролей'))
len_pass = int(input('Введите требуемую длинну пароля'))

# функция запроса предпочтений пользователя по созданию пароля


def pass_input():
    global chars
    use_digits = input('Использовать цифры? Ответь да/нет')
    if use_digits.lower() == 'да':
        chars += digits
    use_up = input('Использовать заглавные буквы? Ответь да/нет')
    if use_up.lower() == 'да':
        chars += uppercase_letters
    use_low = input('Использовать строчные буквы? Ответь да/нет')
    if use_low.lower() == 'да':
        chars += lowercase_letters
    use_punctuation = input('Использовать знаки препинания? Ответь да/нет')
    if use_punctuation.lower() == 'да':
        chars += punctuation
    common_simb = input('Ислючить похожие символы il1Lo0O? Ответь да/нет')
    if common_simb.lower() == 'да':
        chars = chars.replace('il1Lo0O', '')


pass_input()

# генерируем пароль, основываясь на данных пользовательского ввода


def generate_password():
    passwords = []
    for _ in range(num_pass):
        password = ''.join(random.choice(chars) for _ in range(len_pass))
        passwords.append(password)
    return passwords


# выводим пароли
passwords = generate_password()
for password in passwords:
    print(password)
