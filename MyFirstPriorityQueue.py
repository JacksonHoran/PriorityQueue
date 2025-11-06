class MyFirstPriorityQueue:
    """A heap-based priority queue implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, capacity:int = DEFAULT_CAPACITY):
        """Initialize an empty priority queue."""
        # The underlying data structure is a list that will be maintained as a
        # heap.
        self._capacity = capacity
        self._underlying = list[int] = [None] * self._capacity
        self._size = 0

    def __bool__(self) -> bool:
        """Returns False if the queue is empty.  """
        return not self.is_empty()

    def __str__(self) -> str:
        """Return a user-friendly string representaiton of the class using
        f-strings."""
        pass

    def __len__(self) -> int:
        """Return a non-negative integer with the number of items stored in the
        object."""
        return self.size()

    def is_empty(self) -> bool:
        """Returns True if priority queue is empty, false otherwise

        Returns:
            bool: true if size attribute equal to 0, false otherwise
        """
        return (self._size) == 0


    def size(self) -> int:
        """Getter method for size attribute. Size is the number of elements in
        the underlying array.

        Returns:
            int: _description_
        """
        return self._size

    def add(self, value: int):
        """Adds item to the priority queue. 

        Uses sift up algorithm to move the new item to the correct location in
        the max heap.

        Args:
            value (int): The value to be added to the priority queue.

        Raises:
            Exception: If the queue is full.
        """
        if self._size >= self._capacity:
            raise Exception("Priority queue is full.")
        self._underlying[self._size] = value
        self._size += 1
        self._sift_up()


    def extract(self) -> int:
        """Remove and return the most important item in the queue.

        Raises:
            Exception: If priority queue is empty.

        Returns:
            int: The most important item in the priority queue.
        """
        if self.is_empty():
            raise Exception("Priority queue is empty")
        most_imp = self._underlying[0]
        self._underlying[0] = self._underlying[self._size - 1]
        self._size -= 1
        self._sift_down(0)
        # if self._size < (self._capacity // 2):
        #     temp = [item for item in self._underlying if item is not None]
        #     self._underlying = temp
        return most_imp

    def peek(self) -> int:
        """Return but not remove the most important value in the maximum heap
        priority queue.

        Raises:
            IndexError: If underlying array is empty.

        Returns:
            int: Most important value in priority queue.
        """
        if self.is_empty():
            raise IndexError("Priority Queue is empty.")
        return self._underlying[0]

    def peek_next(self) -> int:
        """Return but not remove the second most important value in the maximum
        heap priority queue.

        Raises:
            IndexError: If underlying array is empty.

        Returns:
            int: Second most important value in priority queue.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty.")
        left = self._left_child(0)
        right = self._right_child(0)
        return max(self._underlying[left], self._underlying[right])

    def _swap(self, position, with_position):
        """Swaps positions between two elements in the list.

        Args:
            position (int): index of list item you want to swap
            with_position (int): index of list item you want to swap
        """
        temp = self._underlying[position]
        self._underlying[position] = self._underlying[with_position]
        self._underlying[with_position] = temp

    def _left_child(self, parent: int) -> int:
        """Compute and return the array index of a parent's left child.

        Uses the array-based heap property that a parent at index 'i' has a 
        right child located at (2 * i + 1)

        Args:
            parent (int): index of parent node

        Returns:
            int | None: returns the array index of left child node
        """
        return 2 * parent + 1

    def _right_child(self, parent: int) -> int:
        """Compute and return the array index of a parent's right child.

        Uses the array-based heap property that a parent at index 'i' has a 
        right child located at (2 * i + 2)

        Args:
            parent (int): index of parent node

        Returns:
            int: returns the array index of right child node
        """
        return 2 * parent + 2
    
    def _parent(self, child: int) -> int:
        """Compute and return the array index of a child's parent

        Uses the array-based heap property that a child at index 'i' has a 
        parent located at (i - 1) // 2

        
        Args:
            child (int): index of a node in the array-based heap

        Raises:
            ValueError: if child argument is less than or equal to 0, since the
            root node does not have a parent

        Returns:
            int: index of a child's parent node
        """
        if child <= 0:
            raise ValueError("Cannot get parent of root node.")
        parentIndex = (child - 1) // 2
        return parentIndex

    def _sift_down(self, parent: int):
        """Move a node downward to restore the max heap property.

        This method is called when the root node is removed or is replaced with 
        the last element in the array. The method compares the value of the 
        parent with its children swapping as needed when the max-heap propert is
        violated. The method operates in O(Log(n)) time complexity. 

        Args:
            parent (int): index of the parent node to start at, typically the
            root node.
        """
        left = self._left_child(parent)
        if self._underlying[left] is not None:
            largest = left
            right = self._right_child(parent)
            if (self._underlying[right] is not None and self._underlying[right]
                > self._underlying[left]):
                largest = right
            self._swap(parent, largest)
            self._sift_down(largest)
    
    def _sift_up(self, child: int):
        """Move a node upward to restore the max heap property.

        This method is called when an element is placed at the end of the array.
        The method compares the value of the parent with its children swapping
        as needed when the max-heap property is violated. The method operates 
        in O(log(n)) time complexity.

        Args:
            child (int): Index of the node to start at, typically the last item
            in the array.
        """
        parent = self._parent(child)
        if parent is not None and self._underlying[parent] is not None:
            if self._underlying[parent] < self._underlying[child]:
                self._swap(child, parent)
                self._sift_up(parent)