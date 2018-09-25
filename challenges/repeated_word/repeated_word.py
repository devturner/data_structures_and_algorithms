from .hashtable import Hashtable


def repeated_word(in_str):
    error = False
    hash_table = Hashtable()

    while error is False:
        words = in_str.(' ', 1 )
        hash_table.hash(words)
        if hash_table.key_error:
            error = True
            return words[1]
    
    ruturn 'No words are repeated'
