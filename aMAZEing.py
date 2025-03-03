from collections import deque

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'v' or maze[i][j] == '^' or maze[i][j] == '>' or maze[i][j] == '<':
                start = (i, j)
                break
        if start: break
    queue = deque([(start[0], start[1], 1)])
    visited = set()
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) in visited: continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 'v' or maze[nx][ny] == '^' or maze[nx][ny] == '>' or maze[nx][ny] == '<':
                    return steps + 1
                if maze[nx][ny] == ' ':
                    queue.append((nx, ny, steps + 1))
    return -1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        H, W = map(int, data[idx].split())
        idx += 1
        maze = [data[idx + i] for i in range(H)]
        idx += H
        print(solve_maze(maze))

if __name__ == "__main__":
    main()