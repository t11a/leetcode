class Solution:
    def isAlienSorted(self, words, order):
        len_w = len(words)

        for i in range(0, len_w-1):
            s = words[i]
            t = words[i+1]

            len_s = len(s)

            for j in range(0, len_s):
                if j >= len(t):
                    return False

                s_idx = order.index(s[j])
                t_idx = order.index(t[j])

                if s_idx == t_idx:
                    pass
                elif s_idx < t_idx:
                    break
                else:
                    return False

        return True
        