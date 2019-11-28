# https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
class TrieNode

  attr_accessor :children, :last

  def initialize()
    @children = {}
    @last = false
  end

end

class Trie

  def initialize()
    @root = TrieNode.new()
    @words = []
  end

  def form_trie(keys)
    keys.each do |key|
      insert(key)
    end
  end

  def insert(key)
    node = @root

    key.split('').each do |ch|
      if node.children[ch] == nil
        node.children[ch] = TrieNode.new()
      end

      node = node.children[ch]
    end
    node.last = true
  end

  def search(key)
    node = @root
    found = true

    key.split('').each do |ch|
      if node.children[ch] == nil
        found = false
        break
      end
      node = node.children[ch]
    end
    return (node and node.last and found)
  end

  def suggestions_rec(node, word)
    @words << word if node.last
      
    node.children.each do |k,v|
      suggestions_rec(v, word + k)
    end
  end

  def print_auto_suggestions(key)
    node = @root
    not_found = false
    tmp_word = ''

    key.split('').each do |ch|
      if node.children[ch] == nil
        not_found = true
        break
      end

      tmp_word += ch
      node = node.children[ch]
    end

    if not_found
      return 0
    elsif node.last and node.children.empty?
      return -1
    end

    suggestions_rec(node, tmp_word)

    @words.each do |word|
      puts(word)
    end

    return 1
  end

end

keys = ["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"]
key = "help"

t = Trie.new()

t.form_trie(keys)

puts("**** test for search method ****")
p t.search("hello") == true
p t.search("h") == false
p t.search("cat") == true

puts("**** suggestions for #{key} ****")
comp = t.print_auto_suggestions(key)

if comp == -1
  puts("No other strings found with this prefix") 
elsif comp == 0
  puts("No string found with this prefix")
end