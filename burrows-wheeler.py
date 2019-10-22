def circuler_shifts(string):
    return [string[i:] + string[:i] for i in range(0, len(string))]

def all_rotations(string):
    return circular_shifts('^' + string + '|')

def burrows_wheeler_transform(string):
    res = [word[-1] for word in sorted(all_rotations(string))]
    return ''.join(res)

#FIXME: sorting. the ^ and | changes when characters are lowercase
