
def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    text = ""
    for ch in key:
        if ch in alphabet and ch not in text:
            text += ch

    for ch in alphabet:
        if ch not in text:
            text += ch

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(text[i:i+5]))
    return matrix


def find_position(matrix, ch):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    pairs, i = [], 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    return pairs


def encrypt(text, matrix):
    encrypted = ""

    for a, b in prepare_text(text):
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            encrypted += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            encrypted += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            encrypted += matrix[r1][c2] + matrix[r2][c1]

    return encrypted


def decrypt(text, matrix):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    if len(text) % 2 != 0:
        raise ValueError("Ciphertext must have an even number of letters.")

    decrypted = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            decrypted += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            decrypted += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            decrypted += matrix[r1][c2] + matrix[r2][c1]

    return decrypted


# Main Program
key = input("Enter Key: ")
text = input("Enter Plain Text: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))

print("\nPrepared Text:", " ".join(prepare_text(text)))

ciphertext = encrypt(text, matrix)
print("Encrypted Text:", ciphertext)

decrypted = decrypt(ciphertext, matrix)
print("Decrypted Text:", decrypted)
