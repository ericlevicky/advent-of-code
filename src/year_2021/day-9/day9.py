from collections import OrderedDict
from dataclasses import dataclass
from typing import List


@dataclass
class coordinates:
    r: int = -1
    c: int = -1
    fromDirection: str = "A"

spotsChecked: List[coordinates] = []

def isLowSpot(target: int, surroundingSpots: List[int]):
    if target == 9:
        return False
    
    for surroundingSpot in surroundingSpots:
        if surroundingSpot == -1:
            continue
        if target > surroundingSpot:
            return False
    
    return True


def getSurroundingSpots(grid: List[List[int]], r:int, c:int, asCoordinates:bool = False) -> List:
    toReturn = []

    if len(grid) == 0 or r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
        return toReturn

    # top
    if r-1 >= 0:
        coord = coordinates(r-1, c)
        value = grid[r-1][c]
        toReturn.append(coord if asCoordinates else value)
    
    # bottom
    if r+1 < len(grid):
        coord = coordinates(r+1, c)
        value = grid[r+1][c]
        toReturn.append(coord if asCoordinates else value)

    # left
    if c-1 >= 0:
        coord = coordinates(r, c-1)
        value = grid[r][c-1]
        toReturn.append(coord if asCoordinates else value)
    
    # right
    if c+1 < len(grid[0]):
        coord = coordinates(r, c+1)
        value = grid[r][c+1]
        toReturn.append(coord if asCoordinates else value)

    return toReturn


def getBasinChildrenCount(grid: List[List[int]], r: int, c: int):
    print(f"r: {r}, c: {c}")
    childrenOfBasin = 0
    currSpot = grid[r][c]
    if currSpot == 9:
        return childrenOfBasin
    for coord in getSurroundingSpots(grid=grid, r=r, c=c, asCoordinates=True):
        if coord in spotsChecked:
            continue
        spotsChecked.append(coord)
        spotsChecked
        childSpot = grid[coord.r][coord.c]
        if childSpot != 9:
            childrenOfBasin += 1
            childrenOfBasin += getBasinChildrenCount(grid, coord.r, coord.c)
    return childrenOfBasin


def getBasinSizeForLowSpot(grid: List[List[int]], r:int, c:int) -> int:
    global spotsChecked
    size = 0
    if len(grid) == 0 or r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
        return size
    spotsChecked = []

    # north
    if r-1 >= 0:
        size += getBasinChildrenCount(grid=grid, r=r-1, c=c)
    
    # south
    if r+1 < len(grid):
        size += getBasinChildrenCount(grid=grid, r=r+1, c=c)

    # east
    if c-1 >= 0:
        size += getBasinChildrenCount(grid=grid, r=r, c=c-1)
    
    # west
    if c+1 < len(grid[0]):
        size += getBasinChildrenCount(grid=grid, r=r, c=c+1)
    print(size)
    return size


def day9(fileName: str):
    file = open(fileName, "r")
    allLines = file.read().splitlines()

    grid: List[List[int]]  = []
    for index, line in enumerate(allLines):
        grid.append([])
        grid[index] = []
        for c in range(0, len(line)):
            grid[index].append(-1)
            grid[index][c] = int(line[c])

    lowSpots = []
    sizesOfLowSpots = []
    for rIndex, r in enumerate(grid):
        for cIndex, c in enumerate(r):
            surroundingSpots = getSurroundingSpots(grid, rIndex, cIndex)
            if isLowSpot(target=c, surroundingSpots=surroundingSpots):
                sizesOfLowSpots.append(getBasinSizeForLowSpot(grid, rIndex, cIndex))
                lowSpots.append(c+1)

    print(sizesOfLowSpots)
    sizesOfLowSpots.sort(reverse=True)
    sizesOfLowSpots = sizesOfLowSpots[:3]
    print(sizesOfLowSpots)
    # print(lowSpots)
    return f"Result is {sizesOfLowSpots[0] * sizesOfLowSpots[1] * sizesOfLowSpots[2]}"


print(day9("input.txt"))