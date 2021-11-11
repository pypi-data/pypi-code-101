from pathlib import Path

from pabui.lib.utils import SimpleJsonFileHandler


class ContractsLoadError(Exception):
    pass 


class ContractsLoader:
    def __init__(self, directory: Path) -> None:
        self.abis_directory = directory / "abis"
        self.contracts_file = directory / "contracts.json"
        self.contracts = SimpleJsonFileHandler(self.contracts_file)

    def get_contracts_data(self):
        self.check_valid_contracts_dir()
        contracts_def = self.contracts.read()
        return self.add_abis_to_def(contracts_def)

    def add_abis_to_def(self, contracts_def: dict) -> dict:
        abis = self.load_contracts_abis(contracts_def)
        for contract, abi in abis.items():
            contracts_def[contract]['abi'] = abi
        return contracts_def

    def load_contracts_abis(self, contracts_def: dict) -> dict:
        abis = {}
        for name, data in contracts_def.items():
            abis[name] = None
            if data.get('abifile', None):
                path = Path(data['abifile'])
                abis[name] = self.load_abi(path)
        return abis

    def load_abi(self, abifile: Path):
        with open(self.abis_directory / abifile, "r") as fp:
            return fp.read()

    def check_valid_contracts_dir(self):
        if not self.abis_directory.is_dir():
            raise ContractsLoadError("abis/ directory not found")
