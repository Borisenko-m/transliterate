
def FnTranslit(string):
    res = ''

    for char in string:
        if   char == 'А':
            res += 'A'
        elif char == 'а':
            res += 'a'
        elif char == 'Б':
            res += 'B'
        elif char == 'б':
            res += 'b'
        elif char == 'В':
            res += 'V'
        elif char == 'в':
            res += 'v'
        elif char == 'Г':
            res += 'G'
        elif char == 'г':
            res += 'g'
        elif char == 'Д':
            res += 'D'
        elif char == 'д':
            res += 'd'
        elif char == 'Е':
            res += 'E'
        elif char == 'е':
            res += 'e'
        elif char == 'Ё':
            res += 'E'
        elif char == 'ё':
            res += 'e'
        elif char == 'Ж':
            res += 'Zh'
        elif char == 'ж':
            res += 'zh'
        elif char == 'З':
            res += 'Z'
        elif char == 'з':
            res += 'z'
        elif char == 'И':
            res += 'I'
        elif char == 'и':
            res += 'i'
        elif char == 'Й':
            res += 'I'
        elif char == 'й':
            res += 'i'
        elif char == 'К':
            res += 'K'
        elif char == 'к':
            res += 'k'
        elif char == 'Л':
            res += 'L'
        elif char == 'л':
            res += 'l'
        elif char == 'М':
            res += 'M'
        elif char == 'м':
            res += 'm'
        elif char == 'Н':
            res += 'N'
        elif char == 'н':
            res += 'n'
        elif char == 'О':
            res += 'O'
        elif char == 'о':
            res += 'o'
        elif char == 'П':
            res += 'P'
        elif char == 'п':
            res += 'p'
        elif char == 'Р':
            res += 'R'
        elif char == 'р':
            res += 'r'
        elif char == 'С':
            res += 'S'
        elif char == 'с':
            res += 's'
        elif char == 'Т':
            res += 'T'
        elif char == 'т':
            res += 't'
        elif char == 'У':
            res += 'U'
        elif char == 'у':
            res += 'u'
        elif char == 'Ф':
            res += 'F'
        elif char == 'ф':
            res += 'f'
        elif char == 'Х':
            res += 'Kh'
        elif char == 'х':
            res += 'kh'
        elif char == 'Ц':
            res += 'Ts'
        elif char == 'ц':
            res += 'ts'
        elif char == 'Ч':
            res += 'Ch'
        elif char == 'ч':
            res += 'ch'
        elif char == 'Ш':
            res += 'Sh'
        elif char == 'ш':
            res += 'sh'
        elif char == 'Щ':
            res += 'Shch'
        elif char == 'щ':
            res += 'shch'
        elif char == 'Ъ':
            res += 'Ie'
        elif char == 'ъ':
            res += 'ie'
        elif char == 'Ы':
            res += 'Y'
        elif char == 'ы':
            res += 'y'
        elif char == 'Э':
            res += 'E'
        elif char == 'э':
            res += 'E'
        elif char == 'Ю':
            res += 'Iu'
        elif char == 'ю':
            res += 'iu'
        elif char == 'Я':
            res += 'Ia'
        elif char == 'я':
            res += 'ia'
        elif char == 'Ь':
            res += ''
        elif char == 'ь':
            res += ''
        else:
            res += char
            
    return str(res)
