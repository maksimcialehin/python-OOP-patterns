class BasicImplant:
    def vision(self):
        return 'Normal'

    def hearing(self):
        return 'Standard'

    def durability(self):
        return '95%'


class AdvancedImplant:
    def vision(self):
        return 'Thermal'

    def hearing(self):
        return 'Echo-location'

    def durability(self):
        return '95%'


implant_factories = {
    'basic': BasicImplant,
    'advanced': AdvancedImplant,
}


def create_implant(implant_type):
    return implant_factories.get(implant_type, 'basic')()
