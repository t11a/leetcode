class Solution

  def is_valid(s)
    stack = []

    mappings ={
      ')' => '(',
      ']' => '[',
      '}' => '{'
    }

    s.split('').each do |ch|
      if mappings[ch]
        if stack.size == 0
          return false
        end

        top = stack.pop
        if top != mappings[ch]
          return false
        end
      else
        stack << ch
      end
    end

    return true
  end

end

p Solution.new().is_valid("()")
p Solution.new().is_valid("()[]{}")
p Solution.new().is_valid("([)]")
p Solution.new().is_valid("{[]}")