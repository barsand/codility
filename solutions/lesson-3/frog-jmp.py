def solution(X, Y, D):
    if X == Y:
        return 0

    jump_distance = Y - X
    num_jumps = int(jump_distance/D)

    if jump_distance % D:
        num_jumps += 1

    return num_jumps
