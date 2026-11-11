basic_checkup = lambda: 'Стандартный медосмотр'
repair_func = lambda: 'Ремонт брони'

DOC_REGISTRY = {
    'repair': repair_func,
}


class AutoDoc:
    def __init__(self, procedure=None):
        self.procedure = procedure

    @property
    def procedure(self):
        return self._procedure

    @procedure.setter
    def procedure(self, value):
        self._procedure = DOC_REGISTRY.get(value, basic_checkup)

    def execute(self):
        return self._procedure()
