class Solution

  def top_k_frequent(nums, k)
    h = {}
    nums.each do |n|
      if h[n] == nil
        h[n] = 1
      else
        h[n] += 1
      end
    end

    # use priority queue for h
    # merge sort
    h_a = h.to_a
    sort(h_a, 0, h_a.size-1)
    
    ans = []
    k.times do
      ans << h_a.pop[0]
    end

    return ans
  end

  def sort(h, p, r)
    return if p >= r
    q = (p+r)/2
    sort(h, p, q)
    sort(h, q+1, r)
    merge(h, p, q, r)
  end

  def merge(h, p, q, r)
    a = []
    b = []

    (p..q).each do |i|
      a << h[i]
    end

    (q+1..r).each do |i|
      b << h[i]
    end

    a << [0, 2**32]
    b << [0, 2**32]

    i = 0
    j = 0
    (p..r).each do |k|
      if a[i][1] < b[j][1]
        h[k] = a[i]
        i += 1
      else
        h[k] = b[j]
        j += 1
      end
    end
  end

end

nums = [1,1,1,2,2,3]
k = 2

p Solution.new().top_k_frequent(nums,k)

nums = [1]
k = 1
p Solution.new().top_k_frequent(nums,k)
