import hashlib
import time

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Nascita della mucca", "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), time.time(), transactions, previous_block.hash)
        self.chain.append(new_block)

# Simulazione del processo di produzione del Gorgonzola utilizzando la blockchain
def simulate_gorgonzola_production():
    blockchain = Blockchain()

    # Fase 1: Mungitura
    blockchain.add_block("Mungitura della mucca e raccolta del latte.")

    # Fase 2: Produzione del Formaggio
    blockchain.add_block("Produzione del formaggio Gorgonzola.")

    # Fase 3: Affinamento nelle Grotte
    blockchain.add_block("Affinamento del formaggio nelle grotte.")

    # Fase 4: Distribuzione
    blockchain.add_block("Formaggio Gorgonzola pronto per la distribuzione.")

    return blockchain

# Esecuzione della simulazione
if __name__ == "__main__":
    gorgonzola_blockchain = simulate_gorgonzola_production()

    # Stampa della blockchain simulata
    for block in gorgonzola_blockchain.chain:
        print(f"Blocco #{block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Transazione: {block.transactions}")
        print(f"Hash: {block.hash}")
        print(f"Hash Precedente: {block.previous_hash}")
        print("-" * 30)