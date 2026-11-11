from dataclasses import dataclass


@dataclass
class NeuralAgentDTO:
    id: int = 0
    codename: str = ''
    synchronization_rate: float = 0.0


class AgentRepository:
    _vault: dict[int, NeuralAgentDTO]
    _sequence: int

    def __init__(self):
        self._vault = {}
        self._sequence = 0

    def register(self, agent: NeuralAgentDTO) -> NeuralAgentDTO:
        agent_id = self._sequence + 1
        self._vault[agent_id] = agent
        agent.id = agent_id
        self._sequence = agent_id
        return agent

    def locate(self, agent_id: int) -> NeuralAgentDTO | None:
        return self._vault.get(agent_id)

    def active_roster(self) -> list[NeuralAgentDTO]:
        return list(self._vault.values())


repo = AgentRepository()
repo.register(NeuralAgentDTO(codename='Ghost_7', synchronization_rate=87.5))
print(repo.active_roster())
repo.register(NeuralAgentDTO(codename='Specter', synchronization_rate=92.1))
print(repo.active_roster())
repo.register(NeuralAgentDTO(codename='Null_Pointer', synchronization_rate=64.3))
print(repo.active_roster())
