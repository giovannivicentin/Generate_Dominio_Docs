import subprocess

class OpenDominio:
    def __init__(self):
        self.module = None
        self.path = None

    def open_dominio(self):
        self.path = f'C:\\Dominio\\{self.module}'
        try:
            subprocess.run(["mstsc", self.path])
        except FileNotFoundError:
            print("Rdp file not found. Verify the path.")
        except Exception as e:
            print("Error occurred while opening the .rdp file:", e)

    def open_folha(self):
        self.module = 'Folha.rdp'
        return self.open_dominio()

    def open_fiscal(self):
        self.module = 'Fiscal.rdp'
        return self.open_dominio()

    def open_contabil(self):
        self.module = 'Contabil.rdp'
        return self.open_dominio()

    def open_contabil(self):
        self.module = 'Contabil.rdp'
        return self.open_dominio()

