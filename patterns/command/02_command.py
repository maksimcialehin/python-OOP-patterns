from abc import ABC, abstractmethod


class VDSession:
    def __init__(self) -> None:
        self.questions_asked = 0
        self.empathy_score = 1.0

    def ask_question(self, intensity: int) -> None:
        self.questions_asked += 1
        self.empathy_score -= intensity * 0.1

    def to_dict(self):
        return {'questions': self.questions_asked, 'empathy': round(self.empathy_score, 2)}


class Command(ABC):
    @abstractmethod
    def execute(self): ...

    @abstractmethod
    def undo(self): ...


class AskQuestionCommand(Command):
    def __init__(self, session: VDSession, intensity: int, prev_questions: int = 0, prev_empathy: float = 1.0) -> None:
        self._session = session
        self._intensity = intensity
        self._prev_questions = prev_questions
        self._prev_empathy = prev_empathy

    def execute(self) -> None:
        self._prev_questions_asked = self._session.questions_asked
        self._prev_empathy_score = self._session.empathy_score
        self._session.questions_asked += 1
        self._session.empathy_score = max(0, self._session.empathy_score - self._intensity * 0.1)

    def undo(self) -> None:
        self._session.questions_asked = self._prev_questions_asked
        self._session.empathy_score = self._prev_empathy_score


class VDHistory:
    def __init__(self, session: VDSession) -> None:
        self._session = session
        self._history = []

    def execute(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo(self, count: int) -> None:
        count = min(count, len(self._history))
        for _ in range(count):
            command: Command = self._history.pop()
            command.undo()


def run_commands(session: VDSession, history: VDHistory, intensities: list[int], undo_count: int) -> dict:
    for intensity in intensities:
        cmd = AskQuestionCommand(
            session=session,
            intensity=intensity,
        )
        history.execute(cmd)
    history.undo(count=undo_count)
    return session.to_dict()


session = VDSession()
history = VDHistory(session)
intensities = [3, 1]
undo_count = 1

print(run_commands(session, history, intensities, undo_count))
