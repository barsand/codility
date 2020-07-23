def solution(N):
    '''Find longest sequence of zeros in binary representation of an integer.
    '''
    # ignoring leading and trailing sequences of zeroes
    bin_str = bin(N)[2:].strip('0')

    return len(sorted(bin_str.split('1'))[-1])
