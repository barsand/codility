def solution(A):
    if not A:
        return 0

    left = sum(A[:1])
    right = sum(A[1:])

    min_difference = abs(left - right)
    for p in A[1:]:
        curr_difference = abs(left - right)
        if curr_difference < min_difference:
            min_difference = curr_difference

        left += p
        right -= p

    return min_difference
