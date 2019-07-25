"""
Substring:
A substring is a part of string s[i:j] such that i <= j. It is a contiguous slice of the original string.

For example : List of substrings of string S = "abc" contains following strings.

a
b
c
ab
bc
abc

 a string of length n contains n*(n + 1) / 2 substrings


 Subsequence:
A subsequents is a sequence that can be derived from another sequence by deleting some elements
( possibly zero but not all ) without changing the order of the remaining elements.
For example : List of subsequences of string S = "abc" contains following sequences.
a
b
c
ab
bc
ac
abc
Therefore, a sequence of size n contains (2^n)-1 subsequences.

Subset:
Subset is any unordered set of elements from the original list.

For example : List of subsets of string S = "abc" contains following sets.

{}
{a}
{b}
{c}
{c,b}
{a,b}
{a,c}
{a,b,c}
Therefore, a set of size n contains 2^n subsets.

NOTE :

{b,a,c} is a subset of string "abc" but not a subsequence.
Each subsequence of a collection of elements is its subset also, but reverse does not hold.

"""