class MyFirstPriorityQueue:
    """A heap-based priority queue implementation."""

    def __init__(self):
        """Initialize an empty priority queue."""
        # The underlying data structure is a list
        # that will be maintained as a heap.
        self._underlying = []

    def __bool__(self) -> bool:
        """Return False when the queue is empty."""
        return bool(self._underlying)

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"MyFirstPriorityQueue: {self._underlying}"

    def __len__(self) -> int:
        """Return a non-negative integer with the number"""
        return len(self._underlying)

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False"""
        return not self._underlying

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return len(self._underlying)

    def add(self, value: int) -> None:
        """Add a value to the priority queue."""
        self._underlying.append(value)
        # Restore the heap property
        self._restore_from_top()

    def extract(self) -> int:
        """Remove and return the most important value"""
        if not self._underlying:
            raise IndexError(
                "Cannot extract from an empty queue")
        if len(self._underlying) == 1:
            return self._underlying.pop()
        most_important = self._underlying[0]
        self._underlying[0] = self._underlying.pop()
        self._restore_from_top()
        return most_important

    def peek(self) -> int:
        """Show (without removing) the most important"""
        if not self._underlying:
            raise IndexError(
                "Cannot peek at an empty queue")
        return self._underlying[0]

    def peek_next(self) -> int:
        """Show (without removing) the second most"""
        if len(self._underlying) <= 1:
            raise IndexError(
                "Cannot peek at the second most"
                " element in an empty or"
                " single-element queue")
        return self._underlying[1]

    def _restore_from_top(self) -> int:
        """Restore the heap property at the given"""
        if len(self._underlying) <= 1:
            return 0
        parent = 0
        while parent < len(self._underlying) // 2:
            left_child_index = 2 * parent + 1
            right_child_index = 2 * parent + 2

            if left_child_index < len(
                    self._underlying) and \
                    self._underlying[left_child_index] > \
                    self._underlying[parent]:
                parent = left_child_index
            elif right_child_index < len(
                    self._underlying) and \
                    self._underlying[right_child_index] > \
                    self._underlying[parent]:
                parent = right_child_index

            if parent != 0:
                break
        return parent
