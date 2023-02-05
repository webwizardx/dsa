# KMP (Knuth-Morris-Pratt) Algorithm for pattern matching.
# The algorithm uses a "partial match" table to skip unmatched chars in T (text)
# for faster searching, compared to bruteforce solution.
# Time complexity: O(n + m), where n is length of T and m is length of P (pattern)

from typing import List


def kmpAlgorithm(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    elif len(haystack) == len(needle) and haystack == needle:
        return 0

    def createKmpTable(needle: str) -> List[int]:
        table = [0] * len(needle)
        j, i = 0, 1
        while i < len(needle):
            if needle[j] == needle[i]:
                table[i] = j + 1
                j += 1
                i += 1
            else:
                if j != 0:
                    j = table[j - 1]
                else:
                    i += 1
        return table

    table = createKmpTable(needle)

    j, i, startNeedle = 0, 0, -1

    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            if startNeedle == -1:
                startNeedle = i - j

            i += 1
            j += 1
        else:
            startNeedle = -1
            if j != 0:
                j = table[j - 1]
            else:
                i += 1

    return startNeedle if j == len(needle) else -1
