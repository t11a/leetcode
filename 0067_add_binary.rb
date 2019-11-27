class Solution

  def add_binary(a, b)
    # pading
    max = [a.size, b.size].max
    a = sprintf("%0#{max}d", a)
    b = sprintf("%0#{max}d", b)

    # add
    carry = 0
    ans = ""
    (max-1).downto(0).each do |i|
      if a[i] ==  '1'
        carry += 1
      end

      if b[i] == '1'
        carry += 1
      end

      # (ans, carry)
      # 1 + 1 = 0 -> (0, 1)
      # 1 + 0 = 1 -> (1, 0)
      # 0 + 1 = 1 -> (1, 0)
      # 0 + 0 = 0 -> (0, 0)
      if carry % 2 == 0
        ans = "0" + ans
      else
        ans = "1" + ans
      end

      carry = carry / 2

    end

    if carry == 1
      ans = "1" + ans
    end

    return ans
  end

end

a = "11"
b = "1"
p Solution.new().add_binary(a, b)