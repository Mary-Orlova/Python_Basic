def read_line(line):
    split_text = line.split(' ', 2)
    if len(split_text) == 3:
        name, mail, age = split_text
    else:
        raise ValueError('НЕ присутствуют все три поля')
    try:
        age = int(age)
    except ValueError:
        raise ValueError('Ошибка в значении возраста')
    if age < 10 or age > 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99\n')
    if name.isalpha() == False:
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    if '@' not in mail or '.' not in mail:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и.(точку)')
    return True

good = []
bad = []
text = open('registrations.txt', 'r', encoding="utf-8")
for line in text.read().splitlines():
    try:
        if read_line(line):
            good.append(line)
    except Exception as error:
        bad.append(f'{line} | {error}')

with open('registrations_good.log', 'w', encoding='utf-8') as good_log:
    good_log.write('\n'.join(good))
with open('registrations_bad.log', 'w', encoding='utf-8') as bad_log:
    bad_log.write('\n'.join(bad))
