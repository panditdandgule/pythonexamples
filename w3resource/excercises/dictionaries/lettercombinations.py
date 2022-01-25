import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

d1 = {'1': ['a', 'b'], '2': ['c', 'd'],'3':['d','e']}
for combo in itertools.product(*[d1[k] for k in sorted(d1.keys())]):
    print(''.join(combo))

for combo in itertools.product(*[d1[k] for k in sorted(d1.keys())]):
    print(''.join(combo))


d2={1:['p','q'],2:['r','s']}
for combo in itertools.product(*[d2[k] for k in sorted(d2.keys()) ]):
    print(''.join(combo))

for combo in itertools.product(*[d2[k] for k in sorted(d2.keys())]):
    print(''.join(combo))