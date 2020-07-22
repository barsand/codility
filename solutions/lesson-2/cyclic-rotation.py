def solution(A, K):
    if not A or not K:
        return A

    # avoiding full-cycle rotations
    num_rotations = K % len(A)

    while num_rotations:
        num_rotations -= 1
        A.insert(0, A.pop())

    return A
