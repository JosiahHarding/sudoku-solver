from typing import List, Any, Tuple

import setup.initialise as init


def run_event_loop(board, events):
    count = 0
    while len(events) > 0:
        count += 1
        p = events.pop()
        # print("processing event " + str(p))
        slices = []
        slices.append(init.get_sqr(board, p))
        slices.append(init.get_col(board, p))
        slices.append(init.get_row(board, p))
        for slice in slices:
            events = events | actual_numbers_rule(slice)
            events = events | multiples_rule(slice)
    print("processed " + str(count) + " events")


def actual_numbers_rule(slice):
    hidden_slice = init.dict_manipulation(slice)
    updated = set()

    # run the naked side of the rule
    ones = set_ones(slice)  # get the ones function
    for point, value in ones.items():  # for the point and value in ones:
        for p, possible in slice.items():  # for p ad possible in the slice:
            if p != point and value in slice[p]:  # if p does not equal point and value is in slice[p]:
                slice[p].remove(value)  # remove value from slice[p]
                updated.add(p)

    # run the hidden side of the rule
    ones = set_ones(hidden_slice)  # get the ones function
    for value, point in ones.items():  # for the value and point in ones
        if len(slice[point]) > 1:  # if the length of slice[point] is greater than 1:
            slice[point].clear()  # clear that slice
            slice[point].add(value)  # and add the value
            updated.add(point)  # and add that point to the set 'updated'
    return updated


# This rule operates on a slice of the board.
# For point and possible in the items of the slice:
#	If the length of the set possible is equal to 1:
#		Remove that number from all of the other possibles in the slice being scanned.
# Return the list
def set_ones(slice):
    ones = {}  # creating a new dict
    for point, possible in slice.items():  # for each point in the items of slice:
        if len(possible) == 1:  # If the length of the set ‘possible’ is equal to 1:
            ones[point] = list(possible)[0]  # a new point in ones is equal to the number in possible
    return ones  # return the slices


def multiples_rule(slice):
    hidden_slice = init.dict_manipulation(slice)
    updated = set()
    multiples = find_multiples(slice)
    for item in multiples:
        points = item[0]
        possible = item[1]
        for p in set(slice.keys()) - points:
            if len(possible & slice[p]) > 0:
                slice[p].difference_update(possible)
                updated.add(p)

    multiples = find_multiples(hidden_slice)
    for item in multiples:
        possible = item[0]
        points = item[1]
        for p in points:
            if len(slice[p]) > len(possible):
                slice[p].intersection_update(possible)
                updated.add(p)
    return updated


def find_multiples(slice):
    multiples = []
    sorted = multiples_sort(slice)
    while len(sorted) > 1:
        item = sorted[0]
        sorted.remove(item)
        keys = {item[2]}
        values = set(item[1])
        toremove = []

        for i in sorted:
            point = i[2]
            possible = i[1]  # I won!!
            if len(possible & values) > 0:
                values = values | possible
                keys.add(point)
                toremove.append(i)

            if len(values) == len(keys):
                multiples.append((keys, values))
                break

        for i in toremove:
            sorted.remove(i)
    return multiples


def multiples_sort(slice):
    newlist = []
    for point, possible in slice.items():
        count = len(possible)
        item = (count, possible, point)
        newlist.append(item)
    newlist.sort()
    return newlist
