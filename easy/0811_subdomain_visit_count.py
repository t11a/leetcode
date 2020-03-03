class Solution:
    def subdomainVisits(self, cpdomains):
        h = {}
        for elm in cpdomains:
            cnt = int(elm.split(' ')[0])
            domain = elm.split(' ')[1]

            for str in self._create_pairs(domain):
                h[str] = h.get(str, 0) + cnt

        output = []
        for k, v in h.items():
            output.append("{} {}".format(v, k))

        return output

    def _create_pairs(self,domain):
        # 'a.b.c' => ['a.b.c', 'b.c', 'c']
        labels = domain.split('.')

        output = []
        for i in range(0, len(labels)):
            output.append(".".join(labels[i::]))

        return output

# Input: 
# ["9001 discuss.leetcode.com"]
# Output: 
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))

# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
