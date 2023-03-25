class Cliente:
    def __init__(self, nm, fone):
        self._nome = nm
        self._telefone = fone

    ### método GET
    def get_nome(self):
        return self._nome
    
    ### método SET
    def set_nome(self, nome):
        self._nome = nome