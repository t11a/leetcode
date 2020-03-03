import re

class Solution:
    def reorderLogFiles(self, logs):
        length = len(logs)

        digits = []
        letters = []

        for i in range(0, length):
            if self._is_digit(logs[i].split(' ')):
                digits.append(logs[i])
            else:
                letters.append(logs[i])
        
        length = len(letters)

        for i in range(0, length-1):
            for j in range(i+1, length):
                s = letters[i].split(' ')
                t = letters[j].split(' ')

                if self._is_letter(s) and self._is_letter(t):
                    if self._lexico_check(s[1:], t[1:]):
                        pass
                    else:
                        self._swap(letters, i, j)

        return letters + digits


    def _lexico_check(self,s, t):
        l1 = len(s)
        l2 = len(t)
        min_len = min(l1, l2)

        for i in range(0, min_len):
            if s[i] == t[i]:
                continue
            elif s[i] < t[i]:
                return True
            else:
                return False

        return False

    def _is_digit(self, log):
        p = re.compile('^[0-9]+$')
        return not p.match("".join(log[1:])) == None

    def _is_letter(self, log):
        p = re.compile('^[0-9]+$')
        return p.match("".join(log[1:])) == None

    def _swap(self, logs, i, j):
        tmp = logs[i]
        logs[i] = logs[j]
        logs[j]= tmp
