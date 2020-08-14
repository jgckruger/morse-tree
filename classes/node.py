import json

class Node:
    left = None
    right = None
    value = None
    letter = None

    def __init__(self, left = None, right = None, value = None, letter = None, parent_morse = None):
        self.left = left                    # Node 1
        self.right = right                  # Node 2
        self.value = value                  # '-'
        if parent_morse and value:
            self.morse = parent_morse + value
            self.calculate_letter()
        
    def calculate_letter(self):
        letters = json.load(open('./letters.json'))
        self.letter = next((x for x in letters if x.value == self.morse), None)

    def visit(self):
        print(self.letter)

    def insert(self, value, parent_morse):
        if self.value is None:
            self.value = value
        elif value == '.':
            if self.left is None:
                self.left = Node(value = value, parent_morse = self.morse)
            else:
                self.left.insert(value)
        elif value == '-':
            if self.right is None:
                self.right = Node(value = value, parent_morse = self.morse)
            else:
                self.right.insert(value)
        else:
            print('Invalid character: ', value)

if __name__ == '__main__':
    test = Node()