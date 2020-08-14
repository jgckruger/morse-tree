import json

class Node:
    left = None
    right = None
    value = None
    letter = None

    def __init__(self, morse = '', pos = 0):
        self.morse = morse[:pos+1]
        self.pos = pos
        if (pos+1) < len(morse):
            next_code = morse[pos+1]
            if next_code == '.':
                self.left = Node(morse, pos+1)
            elif next_code == '-':
                self.right = Node(morse, pos+1)

        self.calculate_letter()

    def insert(self, morse, pos = -1):
        if (pos+1) < len(morse):
            next_code = morse[pos+1]
            if next_code == '.' and self.left is None:
                self.left = Node(morse, pos+1)
            elif next_code == '-' and self.right is None:
                self.right = Node(morse, pos+1)
            
            elif next_code == '.' and self.left is not None:
                self.left.insert(morse, pos+1)
            elif next_code == '-' and self.right is not None:
                self.right.insert(morse, pos+1)
    
    def calculate_letter(self):
        letters = json.load(open('./letters.json'))
        for letters, morse in letters.items():
            if morse == self.morse:
                self.letter = letters
        if self.letter is None:
            self.letter = ''

    def visit(self, order):
        if order == 'PREORDER':
            self.process()
            if self.left is not None: 
                self.left.visit(order)
            if self.right is not None: 
                self.right.visit(order)
        elif order == 'INORDER':
            if self.left is not None: 
                self.left.visit(order)
            self.process()
            if self.right is not None: 
                self.right.visit(order)
        elif order == 'POSTORDER':
            if self.left is not None: 
                self.left.visit(order)
            if self.right is not None: 
                self.right.visit(order)
            self.process()

    def process(self):
        print(self)

    def __str__(self):
        return self.letter