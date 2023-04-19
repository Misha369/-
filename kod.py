# Создаем словарь для кодирования букв и символов в цифры
import time
import os
os.system('clear')
banner = """
───────╔╗─╔╗──────────────────╔╗─╔╗
───────║║─║║──────────────────║║─║║
╔╗╔╦╦══╣╚═╣║╔╦══╦══╦══╦═╦══╦══╣╚═╣║╔╦══╗
║╚╝╠╣══╣╔╗║╚╝╣╔╗║╔╗║╔╗║╔╣╔╗║══╣╔╗║╚╝╣╔╗║
║║║║╠══║║║║╔╗╣╔╗║╚╝║╚╝║║║╚╝╠══║║║║╔╗╣╚╝║
╚╩╩╩╩══╩╝╚╩╝╚╩╝╚╩═╗╠══╩╝╚══╩══╩╝╚╩╝╚╩══╝
────────────────╔═╝║
────────────────╚══╝
Telegram @Litvin46"""
for char in banner:
    print(char, end='', flush=True)
    time.sleep(0.01)
encoding_dict = {'А': '1', 'Б': '2', 'В': '3', 'Г': '4', 'Д': '5', 'Е': '6', 'Ё': '7', 'Ж': '8', 'З': '9', 'И': '10', 'Й': '11', 'К': '12', 'Л': '13', 'М': '14', 'Н': '15', 'О': '16', 'П': '17', 'Р': '18', 'С': '19', 'Т': '20', 'У': '21', 'Ф': '22', 'Х': '23', 'Ц': '24', 'Ч': '25', 'Ш': '26', 'Щ': '27', 'Ъ': '28', 'Ы': '29', 'Ь': '30', 'Э': '31', 'Ю': '32', 'Я': '33', 'а': '34', 'б': '35', 'в': '36', 'г': '37', 'д': '38', 'е': '39', 'ё': '40', 'ж': '41', 'з': '42', 'и': '43', 'й': '44', 'к': '45', 'л': '46', 'м': '47', 'н': '48', 'о': '49', 'п': '50', 'р': '51', 'с': '52', 'т': '53', 'у': '54', 'ф': '55', 'х': '56', 'ц': '57', 'ч': '58', 'ш': '59', 'щ': '60', 'ъ': '61', 'ы': '62', 'ь': '63', 'э': '64', 'ю': '65', 'я': '66', ' ': '67', '.': '68', ',': '69', '!': '70', '?': '71', '-': '72', ':': '73', ';': '74', '(': '75', ')': '76', '@': '77', '#': '78', '$': '79', '%': '80', '^': '81', '&': '82', '*': '83', '+': '84', '=': '85', '<': '86', '>': '87', '/': '88', '\\': '89', '|': '90', '_': '149', '~': '91', '`': '92', '{': '93', '}': '94', '[': '95', ']': '96', 'A': '97', 'B': '98', 'C': '99', 'D': '100', 'E': '101', 'F': '102', 'G': '103', 'H': '104', 'I': '105', 'J': '106', 'K': '107', 'L': '108', 'M': '109', 'N': '110', 'O': '111', 'P': '112', 'Q': '113', 'R': '114', 'S': '115', 'T': '116', 'U': '117', 'V': '118', 'W': '119', 'X': '120', 'Y': '121', 'Z': '122', 'a': '123', 'b': '124', 'c': '125', 'd': '126', 'e': '127', 'f': '128', 'g': '129', 'h': '130', 'i': '131', 'j': '132', 'k': '133', 'l': '134', 'm': '135', 'n': '136', 'o': '137', 'p': '138', 'q': '139', 'r': '140', 's': '141', 't': '142', 'u': '143', 'v': '144', 'w': '145', 'x': '146', 'y': '147', 'z': '148'}

# Создаем словарь для декодирования цифр в буквы и символы
decoding_dict = {v: k for k, v in encoding_dict.items()}

# Создаем словарь для кодирования цифр в другие цифры
encoding_dict2 = {'0': '500', '1': '999', '2': '330', '3': '777', '4': '280', '5': '170', '6': '880', '7': '990', '8': '444', '9': '678'}

# Создаем словарь для декодирования цифр в другие цифры
decoding_dict2 = {v: k for k, v in encoding_dict2.items()}

# Функция для кодирования текста в цифры
def encode_text(text):
    encoded_text = ''
    for char in text:
        if char in encoding_dict:
            encoded_text += encoding_dict[char] + ' '
        elif char.isdigit():
            encoded_text += encoding_dict2[char] + ' '
        else:
            encoded_text += str(ord(char)) + ' '
    return encoded_text.strip()

# Функция для декодирования цифр в текст
def decode_text(text):
    decoded_text = ''
    for code in text.split():
        if code in decoding_dict:
            decoded_text += decoding_dict[code]
        elif code.isdigit():
            decoded_text += decoding_dict2[code]
        else:
            decoded_text += chr(int(code))
        decoded_text += '' if code in ['67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96'] else ''
    return decoded_text

# Функция для ввода текста и выбора режима работы
def main():
    while True:
        print('\nВыберите режим работы:')
        print('1. Кодирование текста в цифры')
        print('2. Декодирование цифр в текст')
        print('3. Выход')
        choice = input('Введите номер режима: ')
        if choice == '1':
            text = input('Введите текст для кодирования: ')
            encoded_text = encode_text(text)
            print('Закодированный текст:', encoded_text)
        elif choice == '2':
            text = input('Введите цифры для декодирования: ')
            decoded_text = decode_text(text)
            print('Раскодированный текст:', decoded_text)
        elif choice == '3':
            break
        else:
            print('Неверный номер режима, попробуйте еще раз.')

# Запускаем программ
if __name__ == '__main__':
    main()