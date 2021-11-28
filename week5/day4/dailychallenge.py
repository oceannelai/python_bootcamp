

"“”Create a class called Text that takes a string as an argument and store the text in a attribute.
Implement the following methods:
a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
a method that returns the most common word in the text.
a method that returns a list of all the unique words in the text.
a classmethod that returns a Text instance but with a text file: >>> Text.from_file(‘the_stranger.txt’)“”"
class Text:
    def __init__(self, text):
        self.text = text
    def freq(self, word):
        if self.text.split(' ‘).count(word) > 0 :
            return self.text.split(’ ‘).count(word)
        else:
            return None
    @classmethod
    def from_file(cls, text_file):
        with open(text_file) as f:
            lines = f.readlines()
            lines = [line.replace(“\n”, “”) for line in lines]
            return Text(“”.join(lines))
    def commom(self):
        text_set = list(set(self.text.split(” “)))
        highest = text_set[0]
        for word in text_set:
            if self.text.split(” “).count(word) > self.text.split(” “).count(highest):
                highest = word
        return highest
    def unique_words(self):
        return list(set(self.text.split(’ ’)))
“”"Create a class called TextModification that inherits from Text.
Implement the following methods:
a method that returns the text without any punctuation.
a method that returns the text without any english stop-words (check out what this is !!).
a method that returns the text without any special characters.“”"
from string import punctuation
from nltk.corpus import stopwords
class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
    def de_punctuation(self):
        return “”.join([char for char in self.text if punctuation.count(char) == 0])
    def de_stopwords(self):
        return ” “.join([word for word in self.text.split(” “) if stopwords.words(‘english’).count(word) == 0])
book = Text.from_file(‘the_stranger.txt’)
txt = book.text
# the_freq = book.freq(‘The’)
# common_most = book.commom()
txt_modified = TextModification(book.text)
txt_de_punct = txt_modified.de_punctuation()
print(txt_modified.de_stopwords())
“”"[‘the’, ‘book’, ‘is’]
    highest = ‘the’, count = 353
    [‘the’, ‘book’, ‘is’, ‘the’]
    next_word = ‘book’, count = 400
    if next_word count > highest:
        highest = ‘book’“”"
book = Text.from_file(‘the_stranger.txt’)
txt = book.text
the_freq = book.freq(‘The’)
common_most = book.commom()
“”"list_nums = [5,6,1,1,2,2,3,4]
highest = list_nums[0]
for n in list_nums:
    if n > highest:
        highest = n”“”