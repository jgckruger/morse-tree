import json
from classes.node import Node

class Tree:
    root = None

    def __init__(self, root = None):
        self.root = Node()
        letters = json.load(open('./letters.json'))
        for letters, morse in letters.items():
            self.root.insert(morse)

    def find(self, letter):
        return self.root.find(letter)

    def visit_preorder(self):
        self.root.visit('PREORDER')

    def visit_inorder(self):
        self.root.visit('INORDER')

    def visit_postorder(self):
        self.root.visit('POSTORDER')

    def print_preorder(self):
        pass

    def print_inorder(self):
        pass

    def print_postorder(self):
        pass

    def parse(self, letters):
        pass
