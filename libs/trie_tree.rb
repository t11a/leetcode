require 'pp'

class TrieNode

  attr_accessor :char, :children, :word_finished, :counter

  def initialize(char)
    @char = char
    @children = []
    @word_finished = false
    @counter = 1
  end

end

class Trie

  def add(root, word)
    node = root

    word.split('').each do |char|
      found_in_child = false

      node.children.each do |child|
        if child.char == char
          child.counter += 1
          node = child
          found_in_child = true
          break
        end
      end

      if !found_in_child
        new_node = TrieNode.new(char)
        node.children << new_node
        node = new_node
      end
    end

    node.word_finished = true
  end

  def find_prefix(root, prefix)
    node = root

    return [false, 0] if root.children.empty?

    prefix.split('').each do |char|
      char_not_found = true

      node.children.each do |child|
        if child.char == char
          char_not_found = false

          node = child
          break
        end
      end

      return [false, 0] if char_not_found
    end

    return [true, node.counter]
  end

end

root = TrieNode.new("*")

trie = Trie.new()

trie.add(root, "hackathon")
trie.add(root, "hack")

pp root

p trie.find_prefix(root, 'hac')
p trie.find_prefix(root, 'hack')
p trie.find_prefix(root, 'hackathon')
p trie.find_prefix(root, 'ha')
p trie.find_prefix(root, 'hammer')