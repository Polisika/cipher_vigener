# По варианту задания задан алфавит A-Z и ключ длиной 5.
X = 27
alphabet_rev = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, '_': 26}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


def encrypt_vigenere(text: str, key: str):
    """Зашифровать по алгоритму Виженера"""
    l_key = len(key)
    res = ""

    for i in range(len(text)):
        res += alphabet[(alphabet_rev[text[i]] + alphabet_rev[key[i % l_key]]) % X]

    return res


def decrypt_vigenere(encrypted_text: str, key: str):
    """Расшифровать текст, зашифрованный алгоритмом Виженера"""
    l_key = len(key)
    res = ""

    for i in range(len(encrypted_text)):
        res += alphabet[(alphabet_rev[encrypted_text[i]] - alphabet_rev[key[i % l_key]] + X) % X]

    return res

