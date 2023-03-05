# triplets_with_sum(n) returns a list of all the pythagorean triplets that add up to n

def triplets_with_sum(number):
    # filters empty lists from lists of triplets
    l = [triple for triple in solve(number) if len(triple) != 0]
    if len(l) == 0:
        return []
    else:
        # converts any float values to integer values
        l = [[int(value) for value in triple] for triple in l]
        # sorts each triplet
        for triple in l:
            triple.sort()
        return l

# implements matrix multiplication
def mul(vector,matrix):
    result = []
    for i in range(len(matrix)):
        result.append(0)
        for j in range(len(vector)):
            result[i] += matrix[i][j]*vector[j]
    return result

# recursively generates Pythagorean triples using tree of primitive pythagorean triples
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
def solve(n, triple = [3, 4, 5]):
    # takes absolute value of each value in triple before comparing sum to n
    triple = list(map(abs,triple))
    # matrices to find new primitive triples 
    t1 = [[1,-2,2],[2,-1,2],[2,-2,3]]
    t2 = [[1,2,2],[2,1,2],[2,2,3]]
    t3 = [[-1,2,2],[-2,1,2],[-2,2,3]]
    # returns list of triple if sum of triple is equal to n
    # this node ends because sum of following triples will be larger than n
    if sum(triple) == n:
        return [triple]
    # returns empty list if triples too big -- again, following triples will be too large
    elif sum(triple) > n:
        return []
    
    elif sum(triple) < n:
        # checks (larger) triples following triple that's too small
        return (solve(n, mul(triple, t1))
                + solve(n, mul(triple, t2))
                + solve(n, mul(triple, t3))
                # tree only returns primitive triples -- lambda function checks if sum triple that's a multiple of the primitive triple 
                # equals n
                + [(lambda: [i*(n/sum(triple)) for i in triple] if n%sum(triple)==0 else [])()]
        )
