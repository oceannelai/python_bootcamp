class AnagramChecker:
    def __init__(self, file_name ="sowpods.txt"):
        with open(file_name) as f:
            self.words = [word.strip().upper() for word in f.readlines()]
    def is_valid_word(self,word):
        return word.upper() in self.words
    def get_anagrams(self,word):
        word = word.upper()
        word_sorted= sorted(list(word))
        anagrams = []
        for other_word in self.words:
            if sorted(list(other_word)) == word_sorted:
                anagrams.append(other_word)
        anagrams.remove(word)
        return anagrams

