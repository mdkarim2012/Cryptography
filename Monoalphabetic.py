def encrypt(text, pa, ca):
    enc = ""
    for ch in text:
        if ch.isupper():
            index = pa.index(ch)
            enc += ca[index]
        elif ch.islower():
            index = pa.index(ch.upper())
            enc += ca[index].lower()
        else:
            enc += ch

    return enc


def decrypt(text, pa, ca):
    dec = ""
    for ch in text:
        if ch.isupper():
            index = ca.index(ch)
            dec += pa[index]
        elif ch.islower():
            index = ca.index(ch.upper())
            dec += pa[index].lower()
        else:
            dec += ch

    return dec


# Main Program
pa = input("Enter Plain Alphabet: ").upper()
ca = input("Enter Cipher Alphabet: ").upper()
text = input("Enter Plain Text: ")

enc = encrypt(text, pa, ca)
print("Encrypted Text:", enc)

dec = decrypt(enc, pa, ca)
print("Decrypted Text:", dec)
