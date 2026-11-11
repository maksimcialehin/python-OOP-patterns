class Spaceship:
    def __init__(self):
        self.hull_type = None
        self.engine_class = None
        self.crew_capacity = 0
        self.installed_systems = []
        self.construction_stage = 'frame'

    def __repr__(self):
        return (
            f'Spaceship({self.hull_type}, {self.engine_class}, '
            f'crew={self.crew_capacity}, stage={self.construction_stage})'
        )


class SpaceshipBuilder:
    def __init__(self):
        self.spaceship = Spaceship()

    def set_hull(self, hull: str) -> 'SpaceshipBuilder':
        self.spaceship.hull_type = hull
        self.spaceship.construction_stage = 'frame'
        return self

    def set_engine(self, engine: str) -> 'SpaceshipBuilder':
        if not self.spaceship.hull_type:
            raise ValueError
        self.spaceship.engine_class = engine
        self.spaceship.construction_stage = 'engine'
        return self

    def set_crew(self, capacity: int) -> 'SpaceshipBuilder':
        self.spaceship.crew_capacity = capacity
        self.spaceship.construction_stage = 'systems'
        return self

    def add_system(self, system: str) -> 'SpaceshipBuilder':
        self.spaceship.installed_systems.append(system)
        self.spaceship.construction_stage = 'systems'
        return self

    def get_stage(self) -> str:
        return self.spaceship.construction_stage

    def build(self) -> Spaceship:
        if self.spaceship.hull_type is None or self.spaceship.engine_class is None:
            raise ValueError
        self.spaceship.construction_stage = 'complete'
        return self.spaceship


if __name__ == '__main__':
    hull = input()
    engine = input()
    crew_capacity = int(input())
    system_01 = input()
    system_02 = input()

    result_ship = (
        SpaceshipBuilder()
        .set_hull(hull)
        .set_engine(engine)
        .set_crew(crew_capacity)
        .add_system(system_01)
        .add_system(system_02)
        .build()
    )
