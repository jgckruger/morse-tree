import json
import config

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

    def find(self, morse, pos = 0):
        if pos == len(morse):
            return self.letter
        else:
            next_code = morse[pos]
            if next_code == '.' and self.left:
                return self.left.find(morse, pos+1)
            elif next_code == '-' and self.right:
                return self.right.find(morse, pos+1)
        return ""

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

    def visit_save(self, order, letter_father):
        if order == 'PREORDER':
            self.process3(letter_father)
            if self.left is not None: 
                self.left.visit_save(order, self)
            if self.right is not None: 
                self.right.visit_save(order, self)
        elif order == 'INORDER':
            if self.left is not None: 
                self.left.visit_save(order, self)
            self.process2(letter_father)
            if self.right is not None: 
                self.right.visit_save(order, self)
        elif order == 'POSTORDER':
            if self.left is not None: 
                self.left.visit_save(order, self)
            if self.right is not None: 
                self.right.visit_save(order, self)
            self.process2(letter_father)


    def process(self):
        print(self)

    def process2(self, obj_dad):
        str_ = ""
        for i in range(self.pos):
            str_ += "│{:7}".format("")
        
        if obj_dad == None:
            str_ += "[{}]".format("root")
        else:
            str_ += "└>[{}]".format(None if self.letter == '' else self.letter)
        print(str_)

    def process3(self, obj_dad):
        for i in range(self.pos+1):
            config.preorder_print_matrix[config.row][i] = "│{:7}".format("")
        if obj_dad == None:
            config.preorder_print_matrix[config.row][self.pos] = "[{}]".format("root")
        else:
            config.preorder_print_matrix[config.row][self.pos+1] = "└>[{}]".format(None if self.letter == '' else self.letter )
        
        config.row += 1


    def __str__(self):
        return self.letter