# Python Program for KMP Algorithm

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # Create lps[] that will hold the longest prefix values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    computeLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i]:
            j += 1
            i += 1
        if j == M:
            print("Found pattern at index ", j)
            j = lps[j-1]
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    length = 0 # length of the previous longest prefix suffix
    lps[0] = 0 # lps[0] is always 0
    i = 1 

    # the loop calculates lps[i] for i = 1 to M-1
    while i<M:
        if pat[i] == pat[lenth]:
            length += 1
            lps[i] = length  
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
    
    
