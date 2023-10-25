from Crypto.PublicKey import RSA

# Genera una nuova coppia di chiavi RSA per Bob
bob_key = RSA.generate(2048)

# Ottieni la chiave pubblica e privata di Bob
bob_public_key = bob_key.publickey().export_key()
bob_private_key = bob_key.export_key()

# Salva le chiavi pubbliche e private di Bob in file (opzionale)
with open("bob_public_key.pem", "wb") as file:
    file.write(bob_public_key)

with open("bob_private_key.pem", "wb") as file:
    file.write(bob_private_key)
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP

    # Lisa carica la chiave pubblica di Bob
    with open("bob_public_key.pem", "rb") as file:
        bob_public_key = RSA.import_key(file.read())

    # Messaggio che Lisa vuole inviare a Bob
    message = "Ciao Bob, questo è un messaggio segreto!"

    # Cifra il messaggio utilizzando la chiave pubblica di Bob
    cipher = PKCS1_OAEP.new(bob_public_key)
    ciphertext = cipher.encrypt(message.encode())

    # Stampa il messaggio cifrato (puoi inviarlo a Bob)
    print("Messaggio cifrato:", ciphertext)

