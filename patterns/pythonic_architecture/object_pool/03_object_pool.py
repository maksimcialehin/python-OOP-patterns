class MemoryCell:
    def __init__(self, cell_id: int, is_dynamic: bool = False) -> None:
        self.cell_id = cell_id
        self.is_dynamic = is_dynamic


class DynamicMemoryPool:
    def __init__(self, base_size: int, max_size: int) -> None:
        self.base_size = base_size
        self.max_size = max_size
        self.free_cells: list[MemoryCell] = [MemoryCell(i) for i in range(self.base_size)]
        self.allocated_count: int = 0
        self._current_dynamic_id: int = base_size

    def allocate(self) -> MemoryCell:
        if self.free_cells:
            cell = self.free_cells.pop(0)
        elif self.allocated_count < self.max_size:
            cell = MemoryCell(self._current_dynamic_id, True)
            self._current_dynamic_id += 1
        else:
            raise OverflowError('Лимит памяти достигнут')
        self.allocated_count += 1
        return cell

    def free(self, cell: MemoryCell) -> None:
        self.allocated_count -= 1
        if cell.is_dynamic and len(self.free_cells) >= self.base_size:
            del cell
            return
        self.free_cells.append(cell)
