class Solution

  def fizz_buzz(n)
    ans = []
    1.upto(n) do |i|
      if i % 15 == 0
        ans << "FizzBuzz"
      elsif i % 3 == 0
        ans << "Fizz"
      elsif i % 5 == 0
        ans << "Buzz"
      else
        ans << i.to_s
      end
    end

    return ans
  end

end

p Solution.new().fizz_buzz(15)