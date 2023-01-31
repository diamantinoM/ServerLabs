"""
LABORATÓRIO 4

Exemplo ilustrativo da metodologia de abstracção de dados (data abstraction).

Encoding   -> Provide a 'physical' representation for data. This can be
              motivated by the fact that there is no such 
              representation available yet. But it can also be done in 
              order to obtain different representations for the same 
              data with the purpose of gaining efficiency in processing 
              the data, or reducing the size (compression), or 
              obscuring the data (encryption), etc.
Encryption -> The process of encoding (obscuring) data to make it unreadable.
Decryption -> The process of making data readable again.
Cipher     -> Algorithm for performing encryption and decryption.
Plaintext  -> The original data.
Ciphertext -> The encrypted data.

Caeser Cipher: The idea of the Caesar Cipher is to pick an integer and 
shift every letter of your message by that integer. Suppose the shift is k.
Then, all instances of the ​ith​ letter of the alphabet that appear in the 
plaintext should become the (​i + k) letter of the alphabet in the ciphertext. 
You will need to be careful with the case in which i + k > 26 (the length of 
the alphabet).

Vigenère Cipher: The Vigenère cipher (French pronunciation: ​[viʒnɛːʁ]) 
is a method of encrypting alphabetic text by using a series of 
interwoven Caesar ciphers based on the letters of a keyword. It is a 
form of polyalphabetic substitution.[1][2]
"""

# TODO: Utilizar facilidades do módulo typing para definir tipos (eg, para o encoder) 
# TODO: Redefinir funções em função desses tipos 2) Utilizar namedtuples ou algo similar.

# def make_encoder(*args):
#     pass

# def encode(encoder, data: str):
#     pass

# def get_encoded_data(encoder) -> str:
#     pass

# def decode(encoded_data) -> str:
#     pass

# msg1 = "Amanhã vai chover fortemente!"
# msg2 = "Depois de amanhã, nem por isso."
# msg3 = "Hoje é 21/06/2010."
# msgA = 'RRRR55555abPPPP7L9999'
# msgB = '7Fc888VVVVVV'

import string

# ################################################################
# ENCODING SCHEME 1: CAESAR ENCRYPTION METHOD
# ################################################################

def make_encoder_caesar(
        shift: int, 
        encoded_data: str='', 
):
    return (shift, list(encoded_data))


def encode_caesar(encoder, data: str):
    shift, *_, enc_data = encoder
    for char in data:
        enc_char = char
        chars_to_encode = _CAESAR_CHARS_TO_ENCODE
        if char in chars_to_encode:
            i = chars_to_encode.index(char)
            enc_char = chars_to_encode[(i + shift) % len(chars_to_encode)]
        enc_data.append(enc_char)


def decode_caesar(encoder) -> str:
    shift, *_, enc_data = encoder
    dec_msg = []
    for char in enc_data:
        dec_char = char
        chars_to_encode = _CAESAR_CHARS_TO_ENCODE
        if char in chars_to_encode:
            i = chars_to_encode.index(char)
            dec_char = chars_to_encode[(i - shift) % len(chars_to_encode)]
        dec_msg.append(dec_char)
    return ''.join(dec_msg)


def get_caesar_encoded_data(encoder) -> str:
    *_, enc_data = encoder
    return "".join(enc_data)


_CAESAR_CHARS_TO_ENCODE = string.ascii_letters + string.punctuation + string.digits

# ################################################################
# ENCODING SCHEME 2: SUBSTITUTION ENCRYPTION METHOD
# ################################################################

def make_encoder_vigenere(
        key: str,
        encoded_data: str='', 
):
    return (key, [0], list(encoded_data))


def encode_vigenere(encoder, data: str):
    key, key_index, enc_data = encoder
    for i, char in enumerate(data, key_index[0]):
        enc_char = char
        if char in get_chars_to_encode(TABULA_RECTA):
            row = key[key_index[0]]
            enc_char = get_tabula_recta_value(TABULA_RECTA, row, enc_char)
        enc_data.append(enc_char)
        key_index[0] = (i + 1) % len(key)


def decode_vigenere(encoder) -> str:
    key, _, enc_data = encoder
    key_index = 0
    dec_msg = []
    for i, char in enumerate(enc_data):
        dec_char = char
        if char in get_chars_to_encode(TABULA_RECTA):
            row = key[key_index]
            dec_char = get_tabula_recta_col(TABULA_RECTA, row, char)
        dec_msg.append(dec_char)
        key_index = (i + 1) % len(key)
    return ''.join(dec_msg)


def get_vigenere_encoded_data(encoder) -> str:
    *_, enc_data = encoder
    return "".join(enc_data)


def make_tabula_recta(chars_to_encode: str):
    chars = chars_to_encode
    # Let us suppose chars is 'ABCD'. Our tabula recta should be:
    #   
    #          A    B    C    D 
    #    ------------------------
    #    A  |  A    B    C    D 
    #    B  |  B    C    D    A 
    #    C  |  C    D    A    B  
    #    D  |  D    A    B    C 
    #   
    # The values for each cell of this table are obtained from chars 
    # according to the following formula:
    #
    #     (chars.index(row) + chars.index(col)) % len(chars)
    #
    # Given that len of 'ABCD' is 4, here are some examples:
    #   row A, col A: (index(A) + index(A)) % 4 = (0 + 0) % 4 = 0 -> A 
    #   row A, col B: (index(A) + index(B)) % 4 = (0 + 1) % 4 = 1 -> B
    #   ...
    #   row C, col D: (index(C) + index(D)) % 4 = (2 + 3) % 4 = 1 -> B
    #   row D, col A: (index(D) + index(A)) % 4 = (3 + 0) % 4 = 3 -> D
    #   ...
    table = {
        (row, col): chars[(chars.index(row) + chars.index(col)) % len(chars)]
        for row in chars for col in chars
    } 
    return (chars_to_encode, table)


def get_table(tabula_recta):
    return tabula_recta[1]


def get_chars_to_encode(tabula_recta):
    return tabula_recta[0]


def get_tabula_recta_value(tabula_recta, row: str, col: str):
    table = get_table(tabula_recta)
    return table[row, col]


def get_tabula_recta_col(tabula_recta, row: str, value: str):
    chars_to_encode, table = tabula_recta
    for ch in chars_to_encode:
        if table[row, ch] == value:
            return ch
    raise ValueError(f'Unknown character: {value}')


TABULA_RECTA = make_tabula_recta(
    string.ascii_letters + string.punctuation + string.digits
)

# ################################################################
# ENCODING SCHEME 3: RUN-LENGTH ENCODING
# ################################################################

def make_rle(method: int=-1, encoded_data: str=''):
    if encoded_data:
        method = int(encoded_data[0])
    if method not in (1, 2):
        raise ValueError(f'Invalid encoding method: {method}')

    return (
        encode_m1 if method == 1 else encode_m2,
        decode_m1 if method == 1 else decode_m2,
        list(encoded_data) if encoded_data else [str(method)]
    )


def encode_rle(encoder, data: str):
    enc_method = encoder[0]
    enc_method(encoder, data)


def decode_rle(encoder) -> str:
    dec_method = encoder[1]
    out = []
    dec_method(encoder, out)
    return ''.join(out)


def get_rle_encoded_data(encoder) -> str:
    dest = encoder[-1]
    return ''.join(dest)


def encode_m1(encoder, in_: str):
    dest = encoder[-1]
    def write_fn(char: str, count: int):
        dest.append(_int_to_char(count))
        dest.append(char)
    _do_encode(in_, write_fn)


def encode_m2(encoder, in_: str):
    dest = encoder[-1]
    def write_fn(char: str, count: int):
        dest.append(char)
        if count > 1:
            dest.append(char)
            dest.append(_int_to_char(count))
    _do_encode(in_, write_fn)


def _do_encode(in_: str, write_fn):
    curr_char = ''
    count = 0
    for char in in_:
        if char == curr_char:
            count += 1
            if count == 127:
                write_fn(curr_char, count)
                count = 0
        else:
            if count != 0:
                write_fn(curr_char, count)
            count = 1
            curr_char = char
    if curr_char:
        write_fn(curr_char, count)


def decode_m1(encoder, out: list):
    dest = encoder[-1]
    for count, char in zip(dest[::2], dest[1::2]):
        out.append(_char_to_int(count) * char)
    # for i in range(1, len(dest), 2):
    #     count, char = dest[i], dest[i+1]
    #     out.append(_char_to_int(count) * char)


def decode_m2(encoder, out: list):
    dest = encoder[-1]
    i = 1  
    while i < len(dest):
        char1, char2 = dest[i], dest[i+1] if i + 1 < len(dest) else ''
        if char1 == char2:
            # if there are duplicates, then a third char with the count
            # must be present
            assert i + 2 < len(dest)
            count = _char_to_int(dest[i+2])
            i += 3
        else:
            count = 1
            i += 1
        out.append(count * char1)


def _int_to_char(num: int) -> str:
    if num > 127:
        raise ValueError('Number not between 0 and 127.')
    return chr(num)


def _char_to_int(char: str) -> int:
    num = ord(char)
    if num > 127:
        raise ValueError('Number not between 0 and 127.')
    return num
