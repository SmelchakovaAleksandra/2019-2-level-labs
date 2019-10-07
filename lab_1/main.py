def calculate_frequences(text: str) -> dict:
    dict = {}
    punc = """'!"?$:;/-=+<>^()*&^#№@%,.~`«»[]"""       #объявляются знаки пунктуации
    if (not text) or (type(text) != str):   #проверяется, пустая ли переменная text или является ли она вообще строкой
        return dict
    text = text.lower()
    for i in text:
        if i in punc:
            text = text.replace(i, ' ')     #все знаки пунктуации заменяются пробелами, чтобы потом разделить текст на слова
    text = text.split(' ')
    count = 0       #подсчёт количества упоминаний слова в тексте
    for i in text:
        count = 1
        if (i.isdigit()) or (i.isspace()) or (i in punc) or ('\\n' in i):       #слово пропускается, если оно является цифрой, пробелом или знаком пунктуации
            continue
        if i in dict:
            count = dict[i] + 1     #если слово есть в словаре, то его счётчик увеличивается на 1
            dict.update({i: count})
        dict.update({i: count})
    return dict

def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    new_dict = {}
    if not frequencies:     #проверка, пустой ли словарь
        return new_dict
    if not stop_words:      #проверка, пустой ли список запрещённых слов; если да, то возвращается словарь без изменений
        return frequencies
    for word in stop_words:
        if (type(word) != str) or (word.isdigit()):     #проверка, является ли слово из списка цифрой или отличным от строки; если да, то пропускаем
            continue
        else:
            for key in frequencies:
                if type(key) == str:        #проверка, является ли ключ из словаря строчным
                    if key not in stop_words:       #проверка, входит ли слово-ключ в список запрещённых слов
                        new_dict.update({key: frequencies[key]})    #если нет, то пополняем словарь этим ключом и его значением
                else:
                    continue        #если не является строчным, то пропускаем
    return new_dict

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    top_n_list = []     #создаём пустой список самых частых слов
    sorted_dict = []        #переменная-список для отсортированного по частоте словаря
    if not frequencies:
        return tuple(top_n_list)
    for key, value in frequencies.items():
        sorted_dict.append([key, value])        #пополняем список ключами и значениями словаря
    for i in sorted_dict:
        sorted_dict.sort(key=lambda i: i[1], reverse=True)      #проводим сортировку по количеству через лямбда-функцию, порядок по убыванию
    if top_n > len(frequencies):        #проверяем, если N больше, чем слов в словаре
        top_n = len(frequencies)        #если да, то уменьшаем до максимального количества слов в словаре
    for i in range(top_n):
        top_n_list.extend(sorted_dict[i])       #пополняем список частотных слов значениями из отсортированного списка до top_n
        for j in top_n_list:
            if type(j) == int:
                top_n_list.remove(j)        #убираем количество упоминаний из списка, оставляя только слова
    return tuple(top_n_list)        #возвращаем как кортеж

def read_from_file(path_to_file: str, lines_limit: int) -> str:
    file = open(path_to_file, 'r')
    text = ''
    for i in range(lines_limit):
        text += str(file.readlines())      #чтение до того номера слова, значение которого указано в lines_limit
    file.close()
    return text

def write_to_file(path_to_file: str, content: tuple):
    file = open(path_to_file, 'w')
    for i in content:
        file.write(str(i) + '\n')
    file.close()