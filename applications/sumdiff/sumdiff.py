"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
results = {}
totals = {}
sums = {}
differences = {}
q_list = list(q)
for num in q:
    results[num] = f(num)
for elem_one in q_list:
    for elem_two in q_list:
        s = results[elem_one] + results[elem_two]
        d = results[elem_one] - results[elem_two]
        if s in sums:
            sums[s].append((elem_one, elem_two))
        else:
            sums[s] = [(elem_one, elem_two)]
        if d in differences:
            differences[d].append((elem_one, elem_two))
        else:
            differences[d] = [(elem_one, elem_two)]
    s = results[elem_one] * 2

    # if s in sums:
    #     sums[s].append((elem_one, elem_one))
    # else:
    #     sums[s] = [(elem_one, elem_one)]
    if 0 in differences:
        differences[0].append((elem_one, elem_one))
    else:
        differences[0] = [(elem_one, elem_one)]
# print(sums)
# print(differences)
result = []
for s in sums:
    if s in differences:
        result.append((sums[s], differences[s]))

# print(result)
for t in result:
    for combo in t[0]:
        # print(t)
        num_one = combo[0]
        num_two = combo[1]
        num_three = t[1][0][0]
        num_four = t[1][0][1]
        print(f"f({num_one}) + f({num_two}) = {results[num_one] + results[num_two]} = f({num_three}) - f({num_four})")