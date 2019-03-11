def distance(strand_a, strand_b):
    if(len(strand_a) != len(strand_b)):
        raise ValueError("The two inputs to distance must be of the same length!")

    distance = 0
    for i, val in enumerate(strand_a):
        if strand_a[i] != strand_b[i]:
            distance += 1 
    return distance
