def solution(commands):
    answer = []
    table = [["" for _ in range(51)] for _ in range(51)]
    
    def find_ancestor(r, c):
        if type(table[r][c]) != type(tuple()):
            return r, c
        return find_ancestor(*table[r][c])

    def unmerge(r, c):
        anc_r, anc_c = find_ancestor(r, c)
        val = table[anc_r][anc_c]

        q = []
        for i in range(51):
            for j in range(51):
                if (anc_r, anc_c) == find_ancestor(i, j):
                    q.append((i, j))

        for i, j in q:
            table[i][j] = ""

        table[r][c] = val
    
    for command in commands:
        command = command.split()
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, val = command[1:]
                anc_r, anc_c = find_ancestor(int(r), int(c))
                table[anc_r][anc_c] = val
            elif len(command) == 3:
                val1, val2 = command[1:]
                for i in range(51):
                    for j in range(51):
                        if table[i][j] == val1:
                            table[i][j] = val2
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, command[1:])
            r1, c1 = find_ancestor(r1, c1)
            r2, c2 = find_ancestor(r2, c2)
            if (r1, c1) != (r2, c2):
                if table[r1][c1]:
                    table[r2][c2] = (r1, c1)
                else:
                    table[r1][c1] = (r2, c2)
        elif command[0] == "UNMERGE":
            r, c = map(int, command[1:])
            unmerge(r, c)
        elif command[0] == "PRINT":
            r, c = map(int, command[1:])
            anc_r, anc_c = find_ancestor(r, c)
            answer.append(table[anc_r][anc_c] if table[anc_r][anc_c] else "EMPTY")
    return answer
