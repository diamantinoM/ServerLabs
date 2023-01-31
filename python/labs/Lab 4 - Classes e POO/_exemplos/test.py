from importlib import reload


def doit(vers=0):
    if vers in (0, 1):
        import numeros
        reload(numeros)

        from numeros import (
            rat, add_rat, sub_rat, mul_rat, div_rat, 
            add_complex, sub_complex, mul_complex, div_complex
        )
        r1 = rat(1, 2)
        r2 = rat(1, 4)
        r3 = rat(2, 3)
        r4 = rat(3, 4)

    if vers in (0, 2):
        import numeros2
        reload(numeros2)

        from numeros2 import (
            attach_type, type_of, contents_of,
            is_rectangular, is_polar,
            ComplexType,
            complex_from_mag_angle, complex_from_real_imag, 
            real_part, imag_part, magnitude, angle,
            make_dispatch_table,  dispatch_operation_names, dispatch_types, 
            dispatch_operations, dispatch_table, 
            get_operation, put_operation, 
            operate1, ComplexOperation,
            install_rectangular, install_polar,
            add_complex, sub_complex, mul_complex, div_complex, pow_complex,
            complex_to_str,

            operate2, AritmOperation, NumberType,
            add, sub, mul, div, pow_,
            install_python_number, python_number, 
            install_rational,  rational, 
            install_complex,
        )

    if vers in (0, 1):
        import codificadores
        reload(codificadores)

        from codificadores import (
            make_encoder_caesar, make_encoder_vigenere, make_encoder_rle, 
            make_tabula_recta, 
            encode_caesar, encode_vigenere, encode_rle, 
            decode_caesar, decode_vigenere, decode_rle, 
            METHOD_A, METHOD_B,
        )

    msg1 = "Amanhã vai chover fortemente!".encode()
    msg2 = "Depois de amanhã, nem por isso.".encode()
    msg3 = "Hoje é 21/06/2010.".encode()
    msgA = b'RRRR55555abPPPP7L9999'
    msgB = b'7Fc888VVVVVV'


    globs = globals()
    for name, obj in locals().items():
        globs[name] = obj

    install_rectangular()
    install_polar()
    install_python_number()
    install_rational()
    install_complex()
    

# pylint: disable=R0194
# pylint: disable=W0612

doit()