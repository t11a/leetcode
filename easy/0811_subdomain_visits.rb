class Solution


  def subdomain_visits(cpdomains)
    h = {}

    cpdomains.each do |cpdomain|
      num = cpdomain.split(' ')[0].to_i
      domain = cpdomain.split(' ')[1]
      pairs = create_pairs(domain)

      pairs.each do |pair|
        if h[pair] == nil
          h[pair] = num
        else
          h[pair] += num
        end
      end
    end

    ans = []
    h.each do |k,v|
      ans << "#{v} #{k}"
    end

    return ans
  end

  # a.b.c => [a.b.c, b.c, c]
  def create_pairs(subdomain)
    labels = subdomain.split('.')
    ans = []
    i = 0
    while true
      if labels[i..-1].size != 0
        ans << labels[i..-1].join('.')
        i += 1
      else
        break
      end
    end

    return ans
  end

end

# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]


p Solution.new().subdomain_visits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])