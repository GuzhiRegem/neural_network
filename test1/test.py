
def get_value(inp, weights):
    got = 0.0
    for a in range(len(inp)):
        got += inp[a]*weights[a]
    return got

def get_weights(inp, out):
    wei = inp[:]
    bias = 0.0
    for a in range(len(wei)):
        wei[a] = 0.0
    dif = out - get_value(inp, wei)
    print("-------", wei)
    while(abs(dif) > 0.00000000001):
        difs = []
        chan = []
        for a in range(len(wei)):
            cpy = list(wei)
            cpy[a] = wei[a] + dif
            max_v = out - get_value(inp, cpy)
            cpy[a] = wei[a] - dif
            min_v = out - get_value(inp, cpy)
            if abs(max_v) < abs(min_v):
                chan.append(1)
                difs.append(max_v)
            else:
                chan.append(-1)
                difs.append(min_v)
        max_dif = abs(min(difs, key=abs))
        for a in range(len(wei)):
            wei[a] += (dif * chan[a]) * abs(difs[a]) / max_dif
            if wei[a] > 2.0:
                wei[a] = 2.0
            if wei[a] < -2.0:
                wei[a] = -2.0
        max_v = out - get_value(inp, cpy, bias + (dif / 2))
        min_v = out - get_value(inp, cpy, bias - (dif / 2))
        dif = out - get_value(inp, wei)
        print(wei, bias)
    return(wei, bias)

out = get_weights([1.0, 0.5, 0.3, 0.3], 0.5)
out = get_weights([1.0, 0.8, 0.3, 0.6], 0.5)
print(out)