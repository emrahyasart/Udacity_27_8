def list_to_dict(p):
    my_dict = {}
    t = []
    result = 1
    order = 1

    i = 1
    while i < len(p):
        if p[i] == p[i - 1]:
            result += 1
        else:
            if p[i - 1] not in my_dict:
                t.append(result)
                t.append(order)
                my_dict[p[i - 1]] = t
                t = []
                order += 1
                result = 1
            else:
                if my_dict[p[i - 1]][1] > result:
                    continue
                else:
                    my_dict[p[i - 1]][1] == result
        i += 1

    if result > 1:
        t.append(result)
        t.append(order)
        my_dict[p[i - 1]] = t

    return my_dict


def create_sub_list(p):
    dicts = list_to_dict(p)
    t = []
    for e in dicts:
        t.append(dicts[e][0])
    return t


def longest_repetition(p):
    if len(p) == 0:
        return None
    else:
        dicts = list_to_dict(p)
        dict_2 = {}
        t = create_sub_list(p)
        k = []
        result = 0
        if t.count(max(t)) > 1:
            for values in dicts:
                dict_2[values] = dicts[values][0] * dicts[values][1]
            for values in dicts:
                if max(t) == dicts[values][0]:
                    result = max(t) * dicts[values][1]
                    k.append(result)
                    result = 0

            for e in dict_2:
                if dict_2[e] == min(k):
                    return e

        else:
            for values in dicts:
                if max(t) == dicts[values][0]:
                    return values


print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print (longest_repetition([1,2,3,4,5]))
# 1

print (longest_repetition([]))
# None