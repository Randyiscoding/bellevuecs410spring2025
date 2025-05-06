def naive_string_matching(text, pattern):
    """
    Implement the naive string matching algorithm.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    occur = []
    lenText = len(text)
    lenPattern = len(pattern)
    for i in range(lenText - lenPattern + 1):
        if text[i:i + lenPattern] == pattern:
            occur.append(i)
    return occur

    pass

def rabin_karp(text, pattern, d, q):
    """
    Implement the Rabin-Karp string matching algorithm.
    'd' is the number of characters in the input alphabet, and 'q' is a prime number.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    occur = []
    lenText = len(text)
    lenPattern = len(pattern)
    h = pow(d, lenPattern - 1, q)
    p = 0
    t = 0

    for i in range(lenPattern):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for s in range(lenText - lenPattern + 1):
        if p == t:
            is_match = True
            for i in range(lenPattern):
                if pattern[i] != text[s + i]:
                    is_match = False
                    break
            if is_match:
                occur.append(s)
        if s < (lenText - lenPattern):
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + lenPattern])) % q
            t = (t + q) % q
    return occur
    pass

def kmp_pattern_preprocessing(pattern):
    """
    Preprocess the pattern for the KMP string matching algorithm.
    Return the lps (longest proper prefix which is also a suffix) array.
    """
    lps = len(pattern) * [0]
    x = 0
    y = 1
    while y < len(pattern):
        if pattern[y] == pattern[x]:
            x += 1
            lps[y] = x
            y += 1
        else:
            if x != 0:
                x = lps[x - 1]
            else:
                lps[y] = 0
                y += 1
    return lps
    pass

def trie_insert(root, key):
    """
    Insert 'key' into the trie rooted at 'root'.
    """
    for x in key:
        if x not in root:
            root[x] = {}  # Add new node if missing
        root = root[x]
    root['end_of_word'] = True
    return root
    pass
