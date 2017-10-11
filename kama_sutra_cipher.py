def kama_sutra_cipher(key1, key2, message):
    assert len(key1) == len(key2)
    return convert(key1+key2, key2+key1, message)


def convert(frm, to, text):
    conv_table = ''.maketrans(frm, to)
    return text.translate(conv_table)

if __name__ == "__main__":
    message='MEET AT ELEVEN'
    key1 = 'THEQUICKBROWN'
    key2 = 'FXJMPSVLAZYDG'
    crypted = kama_sutra_cipher(key1, key2, message)
    print(crypted)
    decrypted = kama_sutra_cipher(key1,key2, crypted)
    print(decrypted)
