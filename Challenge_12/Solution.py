inputs = open("input.txt").read().strip()
# Inspired from /u/marchelzo

from json import loads
inputs = loads(inputs)


def counter(j, part_2 = False):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([counter(i, part_2) for i in j])
    if type(j) != dict:
        return 0
    if part_2 and 'red' in j.values():
        return 0
    return counter(list(j.values()), part_2)

print(counter(inputs))
print(counter(inputs, True))