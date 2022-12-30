from dataclasses import dataclass
from itertools import product


@dataclass
class Coordinate:

    x: int
    y: int

    def update(self, new: tuple[int, int]):
        self.x += new[0]
        self.y += new[1]


def tail_in_vicinity(head: Coordinate, tail: Coordinate):
    # Get every combination of 1, -1, and 0
    p = product([-1, 1, 0], [-1, 1, 0])

    return any((head.x + x, head.y + y) == (tail.x, tail.y) for x, y in p)


def update_tail_location(head: Coordinate, tail: Coordinate) -> None:

    """
    Tail will always be moved either left, right, above, or below the head

    This will the "opposite" the heads relative postion from the tail
    if the head is to the right of the tail, the tail will end up to the head's left

    first, check if tail needs to move vertically or horizontally
    vert means that head's y position is more than 1 unit from tail's y
    horizontal means that head's x position is more than 1 unit from tail's x
    """

    # Check vert
    if abs(head.y - tail.y) > 1:
        if head.y - tail.y < 0:  # Head is below tail
            tail.x = head.x
            tail.y = head.y + 1
        else:  # Head is above tail
            tail.x = head.x
            tail.y = head.y - 1
    else:
        if head.x - tail.x < 0:  # Head is to the left of tail
            tail.x = head.x + 1
            tail.y = head.y
        else:  # Head is above tail
            tail.x = head.x - 1
            tail.y = head.y


def main():
    head = Coordinate(0, 0)
    tail = Coordinate(0, 0)
    tail_positions = {(0, 0)}
    with open("input.txt") as f:
        for line in f.readlines():
            match line.split():
                case "R", amt:
                    instructions = [(1, 0) for _ in range(int(amt))]
                case "L", amt:
                    instructions = [(-1, 0) for _ in range(int(amt))]
                case "U", amt:
                    instructions = [(0, 1) for _ in range(int(amt))]
                case "D", amt:
                    instructions = [(0, -1) for _ in range(int(amt))]

            for step in instructions:
                # Move head one space
                head.update(step)

                if not tail_in_vicinity(head, tail):
                    update_tail_location(head, tail)
                    tail_positions.add((tail.x, tail.y))  # type: ignore

    print(len(tail_positions))


if __name__ == "__main__":
    main()
