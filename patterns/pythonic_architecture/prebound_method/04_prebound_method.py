class OracleNet:
    def __init__(self) -> None:
        self._storage = []

    def train(self, num: float) -> None:
        self._storage.append(num)

    def predict(self) -> float:
        last = self._storage[-3:]
        if len(last) < 3:
            return -1
        return round(sum(last) / 3, 2)

    def reset(self) -> None:
        self._storage = []


_oracle = OracleNet()
train = _oracle.train
predict = _oracle.predict
reset = _oracle.reset
