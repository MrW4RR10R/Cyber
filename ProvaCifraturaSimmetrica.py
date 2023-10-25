from cryptography.fernet import Fernet

# Genera una chiave segreta per AES
def generate_key():
    return Fernet.generate_key()

# Cifra il messaggio utilizzando AES
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decifra il messaggio utilizzando AES
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Esempio di utilizzo
if __name__ == "__main__":
    # Genera una chiave segreta
    secret_key = generate_key()
    print("Chiave segreta generata:", secret_key)

    # Messaggio da cifrare
    message_to_encrypt = "Questo è un messaggio segreto!"

    # Cifra il messaggio
    encrypted_message = encrypt_message(secret_key, message_to_encrypt)
    print("Messaggio cifrato:", encrypted_message)

    # Decifra il messaggio
    decrypted_message = decrypt_message(secret_key, encrypted_message)
    print("Messaggio decifrato:", decrypted_message)