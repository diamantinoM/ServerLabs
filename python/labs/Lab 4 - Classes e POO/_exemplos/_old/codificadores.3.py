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

# def encode(encoder, data: bytes):
#     pass

# def decode(encoded_data) -> bytes:  # gerador que faz yield de cada byte
#     pass

# def get_encoded_data(encoder) -> bytes:
#     pass

# msg1 = "Amanhã vai chover fortemente!".encode()
# msg2 = "Depois de amanhã, nem por isso.".encode()
# msg3 = "Hoje é 21/06/2010.".encode()
# msgA = b'RRRR55555abPPPP7L9999'
# msgB = b'7Fc888VVVVVV'

import string
import io
from typing import BinaryIO, Iterable

# ################################################################
# ENCODING SCHEME 1: CAESAR ENCRYPTION METHOD
# ################################################################

def make_encoder_caesar(
        shift: int,
        ascii_printable: bool=False,
        bytes_to_encode: bytes=b'',
):
    if bytes_to_encode and ascii_printable:
        raise ValueError('Use only one of bytes_to_encode or ascii_printable')
    elif ascii_printable:
        bytes_to_encode = string.printable.encode()
    elif not bytes_to_encode:
        bytes_to_encode = bytes(range(0, 256))
    
    return (shift, bytes_to_encode)


def encode_caesar(encoder, data: Iterable[int]):
    shift, bytes_to_encode = encoder
    for byte in data:
        enc_byte = byte
        if byte in bytes_to_encode:
            i = bytes_to_encode.index(byte)
            enc_byte = bytes_to_encode[(i + shift) % len(bytes_to_encode)]
        yield enc_byte


def decode_caesar(encoder, encoded_data: Iterable[int]):
    shift, bytes_to_encode = encoder
    for byte in encoded_data:
        dec_byte = byte
        if byte in bytes_to_encode:
            i = bytes_to_encode.index(byte)
            dec_byte = bytes_to_encode[(i - shift) % len(bytes_to_encode)]
        yield dec_byte

# ################################################################
# ENCODING SCHEME 2: SUBSTITUTION ENCRYPTION METHOD
# ################################################################

def make_encoder_vigenere(
        key: bytes,
        ascii_printable: bool=False,
        bytes_to_encode: bytes=b'',
):
    if bytes_to_encode and ascii_printable:
        raise ValueError('Both bytes_to_encode and ascii_printable were given arguments.')
    elif ascii_printable:
        bytes_to_encode = string.printable.encode()
    elif not bytes_to_encode:
        bytes_to_encode = bytes(range(0, 256))

    return (key, [0], [0], make_tabula_recta(bytes_to_encode))


def encode_vigenere(encoder, data: Iterable[int], reset=False):
    key, enc_key_index, _, tabula_recta = encoder
    enc_key_index[0] = 0 if reset else enc_key_index[0]

    for i, byte in enumerate(data, enc_key_index[0]):
        enc_byte = byte
        if byte in get_bytes_to_encode(tabula_recta):
            row = key[enc_key_index[0]]
            enc_byte = get_tabula_recta_value(tabula_recta, row, enc_byte)
        yield enc_byte
        enc_key_index[0] = (i + 1) % len(key)


def decode_vigenere(encoder, encoded_data: Iterable[int], reset=True):
    key, _, dec_key_index, tabula_recta = encoder
    dec_key_index[0] = 0 if reset else dec_key_index[0]

    for i, byte in enumerate(encoded_data, dec_key_index[0]):
        dec_byte = byte
        if byte in get_bytes_to_encode(tabula_recta):
            row = key[dec_key_index[0]]
            dec_byte = get_tabula_recta_col(tabula_recta, row, byte)
        yield dec_byte
        dec_key_index[0] = (i + 1) % len(key)


def make_tabula_recta(bytes_to_encode: bytes):
    bte = bytes_to_encode
    # Let us suppose that bte is b'ABCD'. Our tabula recta should be (*):
    #   
    #          A    B    C    D 
    #    ------------------------
    #    A  |  A    B    C    D 
    #    B  |  B    C    D    A 
    #    C  |  C    D    A    B  
    #    D  |  D    A    B    C 
    #   
    # (*) Actually, rows and cols will ints with the encoded values for
    # 'A', 'B', 'C' and 'D' (65 to 68). The sames goes for the values.
    #
    # The values for each cell of this table are obtained from bte 
    # according to the following formula:
    #
    #     (bte.index(row) + bte.index(col)) % len(bte)
    #
    # Let's see some examples for the table shown above, where len(bte) 
    # is 4:
    #   row A, col A: (index(A) + index(A)) % 4 = (0 + 0) % 4 = 0 -> A 
    #   row A, col B: (index(A) + index(B)) % 4 = (0 + 1) % 4 = 1 -> B
    #   ...
    #   row C, col D: (index(C) + index(D)) % 4 = (2 + 3) % 4 = 1 -> B
    #   row D, col A: (index(D) + index(A)) % 4 = (3 + 0) % 4 = 3 -> D
    #   ...
    table = {
        (row, col): bte[(bte.index(row) + bte.index(col)) % len(bte)]
        for row in bte for col in bte
    } 
    return (bytes_to_encode, table)


def get_table(tabula_recta):
    return tabula_recta[1]


def get_bytes_to_encode(tabula_recta):
    return tabula_recta[0]


def get_tabula_recta_value(tabula_recta, row: int, col: int):
    _validate_tabula_recta_indexes(row, col)
    table = get_table(tabula_recta)
    return table[row, col]


def get_tabula_recta_col(tabula_recta, row: int, value: int):
    _validate_tabula_recta_indexes(row, 0)
    bytes_to_encode, table = tabula_recta
    for byte in bytes_to_encode:
        if table[row, byte] == value:
            return byte
    raise ValueError(f'Byte <{value}> not in table')


def _validate_tabula_recta_indexes(row: int=None, col: int=None):
    if not 0 <= row <= 255:
        raise ValueError(f'Invalid row <{row}> index')
    if not 0 <= col <= 255:
        raise ValueError(f'Invalid col <{col}> index')
    
# ################################################################
# ENCODING SCHEME 3: RUN-LENGTH ENCODING
# ################################################################

METHOD_A = b'\x21'   # 33 or b'!'
METHOD_B = b'\x8a'   # 138

def make_encoder_rle(
        method: bytes=b'', 
): 
    if method not in (METHOD_A, METHOD_B):
        raise ValueError(f'Invalid encoding method: {method}')

    return (
        encode_m1 if method == METHOD_A else encode_m2,
        decode_m1 if method == METHOD_B else decode_m2,
        method,
    )


def encode_rle(encoder, data: Iterable[int], tag_method: bool=False):
    enc_method, _, method = encoder
    if tag_method:
        yield method
    yield from enc_method(data)


def decode_rle(encoder, encoded_data: Iterable[int]):
    _, dec_method, method = encoder


def encode_m1(data: Iterable[int]):
    def write_fn(byte: int, count: int):
        yield count
        yield byte
    yield from _do_encode(data, write_fn)


def encode_m2(data: Iterable[int]):
    def write_fn(byte: int, count: int):
        yield byte
        if count > 1:
            yield byte
            yield count
    yield from _do_encode(data, write_fn)


def _do_encode(data: Iterable[int], write_fn):
    curr_b = -1
    count = 0
    for b in data:
        if b == curr_b:
            count += 1
            if count == 255:
                yield from write_fn(curr_b, count)
                count = 0
        else:
            if count != 0:
                yield from write_fn(curr_b, count)
            count = 1
            curr_b = b
    if curr_b:
        yield from write_fn(curr_b, count)


def decode_m1(encoded_data: Iterable[int]):
    for count, byte in iter_by_group(encoded_data, 2):
        yield from (byte for _ in range(count))


def decode_m2(encoded_data: Iterable[int]):
    while True:
        b1, b2 = in_.read(1), in_.read(1)  # note that 2 x read(1) != read(2)
        if not b1:                         # read(2) reads _at most_ 2 bytes  
            break                          # and returns a byte string with 3 
                                           # possible lengths
        if b1 == b2:
            b3 = in_.read(1)
            # if there are duplicates, then a third byte with the 
            # count must be present
            assert b3
            count = b3[0]
        else:
            count = 1
            if b2:
                in_.seek(-1, io.SEEK_CUR)

        out.write(count * b1)


def _int_to_byte(num: int) -> bytes:
    return bytes((num,))


def iter_by_group(iterable, n: int):
    """
    If n == 2, yields
        s -> (s0,s1), (s2,s3), (s4, s5), ...
    """    
    it = iter(iterable)
    while True:
        group = []
        for _ in range(n):
            try:
                group.append(next(it))
            except StopIteration:
                break
        if not group:
            return  # return on an generator raises StopIteration
        yield group

# More elegant, but if the number of elements in the iterable isn't a 
# multiple of n, the last remaining elements are not yielded back.
# Besides, this costs more in terms of memory requirements because tee
# needs more space to hold n copies of iterable.
#
# def by_groups(iterable, n: int):
#     "s -> (s0,s1), (s2,s3), (s4, s5), ..."
#     iters = itertools.tee(iterable, n)    
#     return zip(*[itertools.islice(it, i, None, n) for i, it in enumerate(iters)])


    
