import sys
import randomWalk

def randomWalker(n):
    def visit(coord):
        l,c = coord
        grid[l][c] = True
    def visitedOrOutside(coord):
        if not isValid(coord):
            return True
        l,c = coord
        return grid[l][c]
    def isValid(coord):
        l, c = coord
        return 0<=l<n and 0<=c<n
    grid = [[False]*n for i in range(n)]
    start = (n//2, n//2)
    walkers = [start]*n
    visitedCount = 1
    steps = 0
    visit(start)
    while True:
        for i, walker in enumerate(walkers):
            steps += 1
            walkers[i] = randomWalk.randomStep(walker)
            if not visitedOrOutside(walkers[i]):
                visit(walkers[i])
                visitedCount += 1
            if visitedCount >= n*n:
                return steps

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(randomWalker(n))
