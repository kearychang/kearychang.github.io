import math

def kthGrammarRecur(N, K, inverse):
    if K == 1:
        if not inverse:
            return 0
        else:
            return 1
    elif K == 2:
        if not inverse:
            return 1
        else:
            return 0
    elif K <= 2**(N-2):
        return kthGrammarRecur(N-1, K, inverse)
    else:
        return kthGrammarRecur(N-1, K - 2**(N-2), not inverse)    
    # CANNOT FIND LOG runtime version
    # elif N%2 == 0:
    #     if K <= 2**(N-2):
    #         return kthGrammarRecur(N-1, K, inverse)
    #     else:
    #         return kthGrammarRecur(N-1, K - 2**(N-2), not inverse)
    # else:
    #     root_N = math.sqrt(2**(N-1))
    #     divisor = math.ceil(K/root_N)
    #     dividend = K%root_N
    #     if dividend == 0:
    #         if divisor%2 == 1:
    #             return kthGrammarRecur((N+1)//2, root_N, inverse)
    #         else:
    #             return kthGrammarRecur((N+1)//2, root_N, not inverse)
    #     else:
    #         if divisor%2 == 1:
    #             return kthGrammarRecur((N+1)//2, dividend, inverse)
    #         else:
    #             return kthGrammarRecur((N+1)//2, dividend, not inverse)

print(kthGrammarRecur(4,5,False))