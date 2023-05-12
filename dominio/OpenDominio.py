import subprocess


class OpenDominio:
    MODULES = {
        'folha': 'Folha.rdp',
        'fiscal': 'Fiscal.rdp',
        'contabil': 'Contabil.rdp'
    }

    def __init__(self):
        pass

    def open_module(self, module):
        if module not in self.MODULES:
            raise ValueError("Invalid module name")
        path = f"C:\\Dominio\\{self.MODULES[module]}"
        try:
            subprocess.run(["mstsc", path])
        except FileNotFoundError:
            print("Rdp file not found. Verify the path.")
        except Exception as e:
            print("Error occurred while opening the .rdp file:", e)
