from hash_table import HashTable


def left_join_hash_tables(hash1, hash2):
    output = []
    idx = 0
    for i in range(0, len(hash1.hashtable)):
        if hash1.hashtable[i] and hash2.hashtable[i]:
            output.append(hash1.get(hash1.hashtable[i][0][0])[0])
            output[idx].append(hash2.get(hash2.hashtable[i][0][0])[0][1])
            idx += 1
        elif hash1.hashtable[i]:
            output.append(hash1.get(hash1.hashtable[i][0][0])[0])
            output[idx].append('none')
            idx += 1

    return output
