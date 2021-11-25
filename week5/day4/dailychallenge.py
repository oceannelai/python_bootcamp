

import random
class Text():
    def __init__(self, text):
        self.text = text
        self.most_used = None
    @classmethod
    def from_file(file_path):
        with open('the_stranger.txt', 'r') as f:
            file_text = f.read()
        return Text(file_text)
    def get_random_sentence(self, length):
        chosen_word = []
        for i in range(length):
            chosen_word.append(random.choice(self.text.split()))
        return " ".join(chosen_word)
    def word_count(self, word):
        return self.text.split(" ").count(word)
    