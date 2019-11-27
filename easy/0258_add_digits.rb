class Solution

  def add_digits(num)
    n = num
    while n >= 10
      sum = 0
      while n > 0
        sum += n % 10
        n = n / 10
      end
      n = sum
    end

    return n
  end

end

p Solution.new().add_digits(38)