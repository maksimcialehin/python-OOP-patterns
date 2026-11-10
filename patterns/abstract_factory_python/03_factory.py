# Registry Pattern


class Nexus6:
    def voice(self):
        return 'Do androids dream of electric sheep?'


class Nexus8:
    def voice(self):
        return 'Time to die!'


class ReplicantRegistry:
    def __init__(self) -> None:
        self.replicants = {}

    def register(self, model: str, cls) -> None:
        self.replicants[model] = cls

    def create(self, model: str):
        return self.replicants.get(model)()


registry = ReplicantRegistry()
registry.register('Nexus-6', Nexus6)
registry.register('Nexus-8', Nexus8)
print(registry.create('Nexus-6').voice())
