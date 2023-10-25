import hashlib
import time

# Definizione della classe Block
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Funzione per calcolare l'hash di un blocco
def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

# Creazione del blocco genesi
def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

# Creazione di un nuovo blocco
def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Creazione della blockchain
blockchain = [create_genesis_block()]

# Creazione dei blocchi successivi
for i in range(1, 5):  # Creiamo 4 blocchi (da 1 a 4)
    new_block_data = f"Dati del blocco {i}"
    new_block = create_new_block(blockchain[-1], new_block_data)
    blockchain.append(new_block)

    # Stampa delle informazioni del blocco
    print(f"Blocco #{new_block.index} creato.")
    print(f"Hash: {new_block.hash}")
    print("-" * 30)

# Verifica della blockchain
def is_valid_chain(chain):
    for i in range(1, len(chain)):
        if chain[i].previous_hash != chain[i - 1].hash:
            return False
    return True

# Verifica se la blockchain è valida
if is_valid_chain(blockchain):
    print("La blockchain è valida.")
else:
    print("La blockchain non è valida.")