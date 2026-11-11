class CyberneticModule:
    UNINITIALIZED = object()

    def __init__(self):
        self._power_source = self.UNINITIALIZED

    def get_power_source(self):
        if self._power_source is self.UNINITIALIZED:
            self._power_source = 'Солнечная батарея МегаКорп™'
        return self._power_source
