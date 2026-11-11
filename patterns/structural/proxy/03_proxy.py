# Smart Reference


class Archive:
    def get_memory(self, memory_id: str) -> str:
        print('FETCHING FROM SERVER')
        return f'MEMORY-{memory_id}'


class ArchiveProxy:
    def __init__(self) -> None:
        self._archive = Archive()
        self._cache = {}

    def get_memory(self, memory_id: str) -> str:
        if memory_id not in self._cache:
            self._cache[memory_id] = self._archive.get_memory(memory_id)
        return self._cache[memory_id]
