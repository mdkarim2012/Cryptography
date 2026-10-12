def encrypt(pt, key):
    enc = ""
    for ch in pt:
        if ch.isupper():
            enc += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif ch.islower():
            enc += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            enc += ch
    return enc


def decrypt(enc, key):
    dec = ""
    for ch in enc:
        if ch.isupper():
            dec += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        elif ch.islower():
            dec += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            dec += ch
    return dec


# Main Program
pt = input("Plain Text: ")
key = int(input("Key: "))

enc = encrypt(pt, key)
dec = decrypt(enc, key)

print("Encrypted Text:", enc)
print("Decrypted Text:", dec)
