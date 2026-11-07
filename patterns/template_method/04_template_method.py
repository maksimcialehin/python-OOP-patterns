from abc import ABC, abstractmethod


class ConsciousnessUploadProtocol(ABC):
    def __init__(self) -> None:
        self.log = []

    def execute(self, subject_id: str) -> str:
        operations = (
            ('scan', lambda: self.scan_neural_pattern(subject_id)),
            ('biometrics', lambda: self.validate_biometrics(subject_id)),
            ('buffer', lambda: self.prepare_quantum_buffer()),
            ('transfer', lambda: self.transfer_consciousness(subject_id)),
            ('integrity', lambda: self.verify_integrity()),
        )

        for name, operation in operations:
            result = operation()
            self.log.append(f'{name}:{result}')
            if 'fail' in result:
                rollback_result = self.emergency_rollback()
                self.log.append(f'rollback:{rollback_result}')
                break
        else:
            post_result = self.post_upload_procedure()
            self.log.append(f'post:{post_result}')

        return '|'.join(self.log)

    def scan_neural_pattern(self, subject_id: str) -> str:
        return f'{subject_id}:scan_complete'

    def validate_biometrics(self, subject_id: str) -> str:
        return f'{subject_id}:biometrics_valid'

    @abstractmethod
    def prepare_quantum_buffer(self) -> str:
        pass

    @abstractmethod
    def transfer_consciousness(self, subject_id: str) -> str:
        pass

    def verify_integrity(self) -> str:
        return 'integrity_verified'

    def post_upload_procedure(self) -> str:
        return 'standard_monitoring'

    def emergency_rollback(self) -> str:
        return 'rollback_initiated'


class EmergencyProtocol(ConsciousnessUploadProtocol):
    def prepare_quantum_buffer(self) -> str:
        return 'emergency_buffer_allocated'

    def transfer_consciousness(self, subject_id) -> str:
        return f'{subject_id}:rapid_transfer'

    def post_upload_procedure(self) -> str:
        return 'intensive_care_monitoring'


class StandardProtocol(ConsciousnessUploadProtocol):
    def prepare_quantum_buffer(self) -> str:
        return 'standard_buffer_allocated'

    def transfer_consciousness(self, subject_id) -> str:
        return f'{subject_id}:gradual_transfer'


class ExperimentalProtocol(ConsciousnessUploadProtocol):
    def prepare_quantum_buffer(self) -> str:
        return 'entangled_buffer_allocated'

    def transfer_consciousness(self, subject_id) -> str:
        return f'{subject_id}:quantum_tunnel'

    def emergency_rollback(self) -> str:
        return 'quantum_decoherence_reversal'

    def post_upload_procedure(self) -> str:
        return 'neural_divergence_watch'
