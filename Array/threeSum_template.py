def threeSum(self, nums):
    res = set()
    p, n, z = [], [], []
    # 1. Split nums into three lists: negative numbers,
    # positive numbers, and zeros
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # Create a separate set for negatives and positives
    # for O(1) look-up times
    N, P = list(set(n)), list(set(p))
    #3. If there is at least 1 zero in the list, add 
    # all cases where -num exists in N and num exists in P
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))
    
    #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0,0,0))

    # 4.For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
    for i in range(len(N)-1):
        for j in range(i+1, len(N)):
            target = -1 * (N[i] + N[j])
            if target in P:
                res.add(tuple(sorted(N[i], N[j], target)))
    
    # 5.For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
    for i in range(len(P)-1):
        for j in range(i+1, len(P)):
            target = -1 * (P[i] + P[j])
            if target in N:
                res.add(tuple(sorted([P[i],P[j], target])))
    
    return res


