require 'pp'
# https://www.programcreek.com/2014/05/leetcode-implement-trie-prefix-tree-java/
class TrieNode

  attr_accessor :c, :children, :is_leaf

  def initialize(c)
    @c = c
    @is_leaf = false
    @children = {}
  end

end

class Trie

    def initialize()
        @root = TrieNode.new('*')
    end

    # Inserts a word into the trie.
    # :type word: String
    # :rtype: Void
    def insert(word)
        children = @root.children

        i = 0
        word.split('').each do |c|
          t = nil
          if children[c]
            t = children[c]
          else
            t = TrieNode.new(c)
            children[c] = t
          end

          children = t.children

          if i == word.size - 1
            t.is_leaf = true
          end

          i += 1
        end
    end

    # Returns if the word is in the trie.
    # :type word: String
    # :rtype: Boolean
    def search(word)
        t = search_node(word)

        if t != nil and t.is_leaf
          return true
        else
          return false
        end
    end

    # Returns if there is any word in the trie that starts with the given prefix.
    # :type prefix: String
    # :rtype: Boolean
    def starts_with(prefix)
        if search_node(prefix) == nil
          return false
        else
          return true
        end
    end

    def search_node(str)
      children = @root.children
      t = nil
      str.split('').each do |c|
        if children[c]
          t = children[c]
          children = t.children
        else
          return nil
        end
      end

      return t
    end

end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)

trie = Trie.new();

trie.insert("apple")
p trie.search("apple") == true   # returns true
p trie.search("app") == false     # returns false
p trie.starts_with("app") == true # returns true
trie.insert("app");
p trie.search("app") == true     # returns true

trie.insert("banana")
p trie.search("banana") == true
p trie.search("ban") == false
p trie.starts_with("ban") == true