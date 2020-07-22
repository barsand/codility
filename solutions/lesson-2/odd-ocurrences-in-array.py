import collections


def solution(A):
    ocurrences = collections.defaultdict(lambda: 0)
    for element in A:
        ocurrences[element] += 1

    for element, num_ocurrences in ocurrences.items():
        if num_ocurrences % 2:
            return element
