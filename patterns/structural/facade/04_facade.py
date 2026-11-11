class MemoryExtractor:
    def extract(self, patient: str) -> str:
        return f'raw_{patient}_memory'


class DataCompressor:
    def compress(self, data: str) -> str:
        return f'compressed_{data}'


class VaultWriter:
    def write(self, data: str) -> str:
        return f'vault_{data}_stored'


class ArchiveFacade:
    def __init__(self) -> None:
        self._extractor = MemoryExtractor()
        self._compressor = DataCompressor()
        self._vault = VaultWriter()
        self._history = []

    def backup(self, patient: str) -> str:
        raw = self._extractor.extract(patient)
        compressed = self._compressor.compress(raw)
        stored = self._vault.write(compressed)

        record = {
            'patient': patient,
            'raw': raw,
            'compressed': compressed,
            'stored': stored,
        }
        self._history.append(record)

    def undo_last(self) -> str:
        if not self._history:
            return 'NOTHING_TO_UNDO'
        record = self._history.pop()
        return f'UNDONE: {record["patient"]}'
