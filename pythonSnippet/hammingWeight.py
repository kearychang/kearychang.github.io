def hammingWeight(n: int) -> int:
    s = str(n)
    count = 0
    for c in s:
        if c == '1':
            count += 1
    return count

print(hammingWeight(int('00000000000000000000000000001011',10)))