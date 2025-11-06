"""
Extensive test script for MyFirstPriorityQueue.
Run directly or step through using pdb for debugging.

Example:
    python3 -m pdb test_priority_queue.py
"""

from math import log
from MyFirstPriorityQueue import MyFirstPriorityQueue


def print_section(title: str):
    print(f"\n{'=' * 20} {title} {'=' * 20}\n")


def main():
    print_section("CREATE PRIORITY QUEUE")
    pq = MyFirstPriorityQueue(15)
    print(pq)
    print(f"Empty? {pq.is_empty()}")
    print(f"Size: {pq.size()}\n")

    print_section("ADD ELEMENTS")
    elements = [10, 9, 6, 8, 3, 2, 5, 1, 4]
    for val in elements:
        print(f"Adding {val}...")
        pq.add(val)
        pq.print_heap()

    print_section("CHECK HEAP STRUCTURE")
    pq.print_heap()
    print(f"Underlying array: {pq._underlying[:pq._size]}")
    print(f"Peek max: {pq.peek()}")
    print(f"Peek next: {pq.peek_next()}")
    print(f"Size: {len(pq)}")
    print(f"Bool check: {bool(pq)}")

    print_section("TEST EXTRACT MAX")
    while not pq.is_empty():
        max_val = pq.extract()
        print(f"Extracted: {max_val}")
        pq.print_heap()
        print(f"Current size: {pq.size()}")
        print("---------------------------")

    print_section("EXCEPTION TESTS")
    try:
        pq.extract()
    except Exception as e:
        print("Extract from empty queue:", repr(e))

    try:
        pq.peek()
    except Exception as e:
        print("Peek from empty queue:", repr(e))

    print_section("TEST ADD + SIFT UP ORDER")
    new_pq = MyFirstPriorityQueue(10)
    for val in [1, 2, 3, 4, 5, 6, 7]:
        new_pq.add(val)
        print(f"Added {val}")
        new_pq.print_heap()

    print_section("TEST _PARENT / _CHILD RELATIONS")
    for i in range(new_pq.size()):
        p = new_pq._parent(i)
        l = new_pq._left_child(i)
        r = new_pq._right_child(i)
        print(f"Index {i}: parent={p}, left={l}, right={r}")

    print_section("OVERFILL QUEUE TEST")
    limited = MyFirstPriorityQueue(capacity=3)
    try:
        for x in [100, 200, 300, 400]:
            limited.add(x)
            print(limited)
    except Exception as e:
        print("Caught expected overfill exception:", repr(e))

    print_section("DONE — ALL TESTS COMPLETE")


if __name__ == "__main__":
    main()
