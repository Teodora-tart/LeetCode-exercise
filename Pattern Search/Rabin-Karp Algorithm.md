# Rabin-Karp Algorithm for Pattern Searching
Like the Naive Algorithm, Rabin-Karp algorithm also slides the pattern one by one. But unlike the Naive algorithm, Rabin Karp algorithm matches the hash value of the pattern with the hash value of current substring of text, and if the hash values match then only it starts matching individual characters. So Rabin Karp algorithm needs to calculate hash values for following strings.
1) Pattern itself. 
2) All the substrings of the text of length m. 

Since we need to efficiently calculate hash values for all the substring of size m of text, we must have a hash function which has the following property:
Hash at the next shift must be efficiently computable from the current hash value and next character in text or we can say hash(txt[s+1 .. s+m]) must be efficiently computable from hash(txt[s .. s+m-1]) and txt[s+m] i.e., hash(txt[s+1 .. s+m])= rehash(txt[s+m], hash(txt[s .. s+m-1])) and rehash must be O(1) operation.
'''
hash(txt[s+1...s+m]) = (d(hash(txt[s...s+m-1]) - txt[s]×h) + txt[s+m])mod q
hash(txt[s...s+m-1]): hash value at shift s
hash(txt[s+1...s+m]): hash value at next shift(or shift s+1)

d: number of characters in the alphabet
q: a prime number
h: d^(m-1)
```
