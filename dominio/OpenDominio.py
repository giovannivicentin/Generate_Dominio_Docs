class OpenDominio:
    def __init__(self):
        self.module = None
        self.path = None

    def open_dominio(self):
        self.path = f'C:\\Dominio\\{self.module}'
        try:
            with open(self.path, 'r') as file:
                opened = file.read()
                return opened
        except FileNotFoundError:
            print(f'File {self.path} not found.')
            return None

    def open_folha(self):
        self.module = 'Folha.rdp'
        return self.open_dominio()

    def open_fiscal(self):
        self.module = 'Fiscal.rdp'
        return self.open_dominio()

    def open_contabil(self):
        self.module = 'Contabil.rdp'
        return self.open_dominio()
