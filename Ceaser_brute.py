def decrypt(ct, key):
    dec = ""
    for ch in ct:
        if ch.isupper():
            dec += chr((ord(ch)-ord('A')-key)%26+ord('A'))
        elif ch.islower():
            dec += chr((ord(ch)-ord('a')-key)%26+ord('a'))
        else:
            dec += ch

    return dec


ct = input("Cipher Text: ")

for key in range(1, 26):
    print("Key", key, ":", decrypt(ct, key))
