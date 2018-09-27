

def left_join_hash_tables(hash1, hash2):
    output = []

    for key, val in hash1.items():
        output.append([key, val, 'none'])

    for key, val in hash2.items():
        for i in output:
            if key in i:
                output[i.index(key)].append(val)
                output[i.index(key)].remove('none')

    return output
