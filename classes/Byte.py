class Byte:

    def __init__(self, id=-1, idx_ini=-1, tam=-1):
        self.id = id
        self.idx_ini = idx_ini
        self.tam = tam
    
    def reset(self):
        self.id = -1
        self.idx_ini = -1
        self.tam = -1