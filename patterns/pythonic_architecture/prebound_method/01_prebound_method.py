class EnergyGrid:
    def __init__(self, reactors: dict | None = None) -> None:
        if reactors is None:
            reactors = {}
        self.reactors = reactors

    def toggle_reactor(self, rid: str) -> bool:
        self.reactors[rid] = not self.reactors.get(rid, False)
        return self.reactors.get(rid)


_grid = EnergyGrid()
toggle_reactor = _grid.toggle_reactor
