





def unload(input):
    res = []
    luggages = []
    for i in xrange(len(input)):
        if sum(luggages) + input[i] > 40:
            res.append(luggages[:])
            luggages = [input[i]]
        else:
            luggages.append(input[i])
    if luggages:
        res.append(luggages)
    output = []
    while res:
        output.append(res.pop())

    return output

input = [30, 6, 5]
unload(input)