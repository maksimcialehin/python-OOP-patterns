from abc import ABC, abstractmethod


class HeroState(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def on_attack(self, hero: 'Hero', target: str) -> int:
        pass

    @abstractmethod
    def on_damage_taken(self, hero: 'Hero', amount: int) -> int:
        """Возвращает фактический урон."""
        pass


class NormalState(HeroState):
    name = 'NORMAL'

    def on_attack(self, hero: 'Hero', target: str) -> int:
        return hero.base_damage

    def on_damage_taken(self, hero: 'Hero', amount: int) -> int:
        return amount


class CoverState(HeroState):
    name = 'COVER'
    DAMAGE_REDUCTION = 0.5

    def on_attack(self, hero: 'Hero', target: str) -> int:
        return int(hero.base_damage * 0.8)

    def on_damage_taken(self, hero: 'Hero', amount: int) -> int:
        reduced = int(amount * self.DAMAGE_REDUCTION)
        return reduced


class OverwatchState(HeroState):
    name = 'OVERWATCH'

    def on_attack(self, hero: 'Hero', target: str) -> int:
        return int(hero.base_damage * 1.3)

    def on_damage_taken(self, hero: 'Hero', amount: int) -> int:
        return amount


class Command(ABC):
    @abstractmethod
    def execute(self, hero: 'Hero') -> str:
        pass


class AttackCommand(Command):
    def __init__(self, target: str = 'враг'):
        self._target = target

    def execute(self, hero: 'Hero') -> str:
        damage = hero.state.on_attack(hero, 'target')
        hero.last_damage_dealt = damage
        hero.transition_to(NormalState())
        return f'ATTACK: {damage} урона'


class TakeCoverCommand(Command):
    def execute(self, hero: 'Hero') -> str:
        hero.transition_to(CoverState())
        return 'COVER: В укрытии'


class OverwatchCommand(Command):
    def execute(self, hero: 'Hero') -> str:
        hero.transition_to(OverwatchState())
        return 'OVERWATCH: Готов к контратаке'


class Hero:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.base_damage = 30
        self._state: HeroState = NormalState()
        self.last_damage_dealt = 0

    @property
    def state(self) -> HeroState:
        return self._state

    def transition_to(self, state: HeroState) -> None:
        print(f'{self.name}: {self._state.name} → {state.name}')
        self._state = state

    def take_damage(self, amount: int) -> None:
        actual = self._state.on_damage_taken(self, amount)
        self.hp -= actual
        self.hp = max(0, self.hp)

    def process_command(self, cmd: Command) -> str:
        return cmd.execute(self)


class BattleSystem:
    def __init__(self, hero: Hero):
        self._hero = hero
        self._log: list[str] = []

    def execute(self, cmd: Command) -> None:
        result = self._hero.process_command(cmd)
        self._log.append(result)
        print(result)

    def enemy_attack(self, damage: int) -> None:
        self._hero.take_damage(damage)

    def get_state(self) -> dict:
        return {
            'hp': self._hero.hp,
            'state': self._hero.state.name,
            'last_damage': self._hero.last_damage_dealt,
        }


COMMAND_REGISTRY = {
    'attack': AttackCommand,
    'cover': TakeCoverCommand,
    'overwatch': OverwatchCommand,
}

if __name__ == '__main__':
    hero = Hero('Декард')
    battle = BattleSystem(hero)

    actions = open(0).read().split('\n')
    for action in actions:
        act, *args = action.split()
        if act in COMMAND_REGISTRY:
            battle.execute(COMMAND_REGISTRY[act]())
        elif act == 'enemy_attack':
            battle.enemy_attack(int(args[0]))
