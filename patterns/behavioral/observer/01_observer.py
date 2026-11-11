from typing import Any


class Scanner:
    def scan(self, target: str, synthetics_perc: int) -> dict[str, Any]:
        confidence = synthetics_perc * 0.5
        status = 'human' if confidence < 50 else 'replicant'
        return {'target': target, 'status': status, 'confidence': confidence}


class NexusScanner(Scanner):
    def scan(self, target: str, synthetics_perc: int) -> str:
        confidence = synthetics_perc * 0.9
        status = 'human' if confidence < 50 else 'replicant'
        confidence = 100.0 - confidence if status == 'human' else confidence
        return {'target': target, 'status': status, 'confidence': confidence}
