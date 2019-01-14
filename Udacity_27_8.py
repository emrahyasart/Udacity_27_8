def longest_repetition(p):
    best_rank = 1
    best_order = 0
    current_rank = 1
    current_order = 0
    i = 1
    if len(p) == 0:
        return None
    else:
        while i < len(p):
            if p[i] == p[i-1]:
                current_rank += 1
                current_order = i-1
                i +=1
                if current_rank > best_rank:
                    best_rank = current_rank
                    best_order = current_order
                else:
                    continue
            else:
                current_order = i-1
                current_rank = 1
                i += 1
        return p[best_order]

print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print (longest_repetition([1,2,3,4,5]))
# 1

print (longest_repetition([]))
# None
