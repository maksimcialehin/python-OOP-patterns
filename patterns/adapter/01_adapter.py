from abc import ABC, abstractmethod


class ReplicantTester(ABC):
    @abstractmethod
    def test(self, name: str) -> str:
        pass


class LegacyMachine:
    def __init__(self):
        self._database = {
            'Rachael': {'pupil': [0.1, 0.2, 0.1], 'response': [0.5, 0.6, 0.4]},
            'Deckard': {'pupil': [0.8, 0.9, 0.85], 'response': [1.2, 1.1, 1.3]},
            'K': {'pupil': [0.15, 0.1, 0.2], 'response': [0.4, 0.5, 0.3]},
            'Joe': {'pupil': [0.7, 0.8, 0.75], 'response': [1.0, 1.1, 0.9]},
        }

    def run_test(self, subject_id: str, question_count: int) -> dict:
        data = self._database[subject_id]
        return {
            'pupil_dilation': data['pupil'][:question_count],
            'response_time': data['response'][:question_count],
        }

    def calculate_empathy_score(self, raw_data: dict) -> float:
        pupil_avg = sum(raw_data['pupil_dilation']) / len(raw_data['pupil_dilation'])
        response_avg = sum(raw_data['response_time']) / len(raw_data['response_time'])
        return (pupil_avg * 0.3) + (response_avg * 0.7)


class LegacyAdapter(ReplicantTester):
    def __init__(self, machine: LegacyMachine) -> None:
        self.legacy_tester: LegacyMachine = machine

    def test(self, name: str) -> str:
        test_data: dict = self.legacy_tester.run_test(subject_id=name, question_count=10)
        empathy = self.legacy_tester.calculate_empathy_score(test_data)
        return 'HUMAN' if empathy > 0.5 else 'REPLICANT'
