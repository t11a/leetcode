class Solution

  def longest_palindrome(s)
    return s if s.size <= 1

    longest = s[0,1]

    0.upto(s.size-1) do |i|
      tmp = expand(s, i, i)
      longest = tmp if tmp.size > longest.size

      tmp = expand(s, i, i+1)
      longest = tmp if tmp.size > longest.size
    end

    return longest
  end

  def expand(s, l, r)
    while (l >= 0 and r < s.size and s[l] == s[r])
      l -= 1
      r += 1
    end
    return s[l+1,r]
    #return s[l+1..r-1]
  end

end

s = "abba"
p Solution.new().longest_palindrome(s)

s = "abcba"
p Solution.new().longest_palindrome(s)