import random

class SimpleCrossword:
    def __init__(self, size):
        self.size = size
        self.grid = [['_' for _ in range(size)] for _ in range(size)]
        self.words = []

    def add_word(self, word):
        self.words.append(word.upper())

    def place_word(self, word):
        direction = random.choice(['H', 'V'])
        max_attempts = 100

        for _ in range(max_attempts):
            if direction == 'H':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - len(word))
                if self.can_place(word, row, col, direction):
                    for i in range(len(word)):
                        self.grid[row][col + i] = word[i]
                    return True
            else:
                row = random.randint(0, self.size - len(word))
                col = random.randint(0, self.size - 1)
                if self.can_place(word, row, col, direction):
                    for i in range(len(word)):
                        self.grid[row + i][col] = word[i]
                    return True
        return False

    def can_place(self, word, row, col, direction):
        if direction == 'H':
            for i in range(len(word)):
                if self.grid[row][col + i] not in ('_', word[i]):
                    return False
        else:
            for i in range(len(word)):
                if self.grid[row + i][col] not in ('_', word[i]):
                    return False
        return True

    def fill_grid(self):
        for word in self.words:
            if not self.place_word(word):
                print(f"Failed to place the word: {word}")

    def display(self):
        for row in self.grid:
            print(' '.join(row))

# Example usage
crossword = SimpleCrossword(10)
words_to_add = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "RUBY", "CPLUSPLUS"]

for word in words_to_add:
    crossword.add_word(word)

crossword.fill_grid()
crossword.display()
