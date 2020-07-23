def solution(A):
    if not A:
        return 1

    A.sort()
    for a, b in zip(range(1, len(A)+1), A):
        if a != b:
            return a

    return A[-1] + 1
