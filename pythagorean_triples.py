

def pythagorean_triples(p, q):
    x = q**2 - p**2
    y = 2*q*p
    z = q**2 + p**2
    return x, y, z

def test_triples(limit):
    for i in range(1, limit-1):
        p, q = i, i+1
        x, y, z = pythagorean_triples(p, q)
        print("##################################")
        print('p={}, q={}'.format(p, q))
        print('x={}, y={}, z={}'.format(x, y, z))
        print('x**2 + y**2 = {}, z**2 = {}'.format(x**2 + y**2, z**2))

test_triples(100)