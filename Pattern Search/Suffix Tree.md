# Pattern Searching using Suffix Tree
## Find a pattern in the built suffix tree
1) Starting from the first character of the pattern and root of Suffix Tree, do following for every character.
2) For the current character of pattern, if there is an edge from the currentnode of suffix tree, follow the edge.
3) If there is no edge, print "pattern doesn't exist in text" and return.
4) If all characters of pattern have been processed, i.e., there is a path from root for characters of the given pattern, then print “Pattern found”.

## Ukkonen's Suffix Tree Construction
A suffix tree T for a m-character string S is a rooted directed tree with exactly m leaves numbered 1 to m
> Root can have zero, one or more children
>
> Each internal node, other than the root, has at least two children
> 
> Each edge is labelled with a nonempty substring of S.
> 
> No two edges coming out of same node can have edge-labels beginning with the same character.
> 
Concatenation of the edge-labels on the path from the root to leaf i gives the suffix of S that starts at position i, i.e. S[i…m].

Note: Position starts with 1 (it’s not zero indexed, but later, while code implementation, we will used zero indexed position)
