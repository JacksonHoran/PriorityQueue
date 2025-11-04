class MyFirstPriorityQueue:
    """A heap-based priority queue implementation."""

    def __init__(self):
        """Initialize an empty priority queue."""
        # The underlying data structure is a list that will be maintained as a heap.
        self._underlying = []

    def __bool__(self) -> bool:
        """Return False when the queue is empty

        Returns:
            bool: _description_
        """
        pass

    def __str__(self) -> str:
        """Return a user-friendly string representaiton fo the class using f-strings.

        Returns:
            str: _description_
        """
        pass

    def __len__(self) -> int:
        """Return a non-negative integer with the number of items stored in the object.

        Returns:
            int: _description_
        """
        pass

    def is_empty(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        pass

    def size(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        pass

    def add(self, value: int) -> int:
        """Add an element to the priority queue.

        Args:
            value (int): _description_

        Returns:
            int: _description_
        """
        pass

    def extract(self) -> int:
        """Remove and return the most important value in the heap given the maximum heap prioprity queue.

        Returns:
            int: _description_
        """
        pass

    def peek(self) -> int:
        """Return but not remove the most important value in the maximum heap priority queue.

        Returns:
            int: _description_
        """
        pass

    def peek_next(self) -> int:
        """Return but not remove the second most important value in the maximum heap priority queue.

        Returns:
            int: _description_
        """
        pass
