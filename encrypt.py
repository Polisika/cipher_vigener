# По варианту задания задан алфавит A-Z и ключ длиной 5.
X = 26
bias = 65


def encrypt_vigenere(text: str, key: str):
    """Зашифровать по алгоритму Виженера"""
    l_key = len(key)
    res = ""

    for i in range(len(text)):
        res += chr((ord(text[i]) + ord(key[i % l_key])) % X + bias)

    return res


def decrypt_vigenere(encrypted_text: str, key: str):
    """Расшифровать текст, зашифрованный алгоритмом Виженера"""
    l_key = len(key)
    res = ""

    for i in range(len(encrypted_text)):
        res += chr((ord(encrypted_text[i]) - ord(key[i % l_key]) + X) % X + bias)

    return res


# Тестирование функций
assert decrypt_vigenere('LXFOPVEFRNHR', 'LEMON') == 'ATTACKATDAWN'
assert encrypt_vigenere('ATTACKATDAWN', 'LEMON') == 'LXFOPVEFRNHR'
