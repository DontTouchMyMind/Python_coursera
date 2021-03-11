import re


def check_username(nicknames: list):
    """
    Функция проверяет ники на соответствие с формой.
    Ник должен содержать только буквы лат. алфавита, цифры и символ '_'.
    :param nickname: Список ников.
    :return: Выводит Valid, если ник соответствует, Invalid - если нет.
    """
    # Начиная с начала строки ^ и до конца $, идут буквы, цифры и подчеркивания \w (в том числе и национальный алфавит)
    # re.ASCII - уберет национальный алфавит
    reg = re.compile(r'^\w+$', re.ASCII)
    for nick in nicknames:
        print('{} nickname: "{}"'.format(
            'Valid' if reg.match(nick) else 'Invalid', nick
        ))


def find_female_names(input_text: str):
    """Функция ищет женские имена в тексте.  Они начинаются с заглавной и закачиваются на 'на'."""
    # \b - в начале и конце говорит, что мы ищем слово.
    # (на|НА) - группа, в которую входит "на" и "НА"
    # ?: - то что находится группируется, но не запоминается.
    result = re.findall(r'\b[А-Я]\w*(?:на|НА)\b', input_text)
    print(result)


def find_double_letters(input_text: str):
    """Функция ищет в тексте буквы, которые повторяются и идут подряд."""
    result = re.findall(r'(\w)\1', input_text)
    print(result)


def replace_letters(input_text):
    """Функция заменяет все буквы 'a' знаком '?'."""
    result = re.sub(r'а', '?', input_text)
    print(result)


def replace_double_letters(input_text):
    """Функция переводит в верхний регистр буквы, повторяющиеся и идущие подряд."""
    result = re.sub(r'(\w)\1', lambda r: r.group(0).upper(), input_text)
    print(result)


def replace_words(input_text):
    """Функция выделяет слова, имеющие повторяющиеся и идущие подряд буквы."""
    result = re.sub(r'\b(\w*(\w)\2\w*)\b', r'[\1]', input_text)
    print(result)


if __name__ == '__main__':

    nicknames_list = ['sU3r_h4XX0r', 'alёna', 'ivan ivanovich']
    check_username(nicknames_list)

    text = (
        'Анна и Лена загорали на берегу, '
        'когда к ним подошли Яна, ПОЛИНА и Ильнар'
    )
    find_female_names(text)

    text = 'Как защитить металл от процесса коррозии?'
    find_double_letters(text)
    replace_letters(text)
    replace_double_letters(text)
    replace_words(text)
