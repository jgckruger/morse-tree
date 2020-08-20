import json
from classes.node import Node
import config

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
        self.root.visit_save('PREORDER', None)
        matrix, N, M = config.preorder_print_matrix, config.N, config.M

        for i in range(N):
            if matrix[i][0] == None:
                    continue
            matrix[i][0] = matrix[i][0].replace("│      ", "  │    ")

        for j in range(1, M):
            for i in range(N):
                if matrix[i][j] == None:
                    continue
                matrix[i][j] = matrix[i][j].replace("│      ", "  │    ")
                if matrix[i][j][0] == '└':
                    matrix[i][j] = matrix[i][j].replace('└', '—')
                    matrix[i][j-1] = "{:7}".format("  └————")

        for j in range(M):
            for i in range(N-1, j, -1):
                if matrix[i][j] == None:
                    continue
                if matrix[i][j][:3] == '  │':
                    matrix[i][j] = "{:8}".format("")
                else:
                    break

        for j in range(M-4):
            son, dad = [], []
            for i in range(N):
                if matrix[i][j] == None:
                    continue
                if matrix[i][j][2] == '└':
                    son.append(i) 
                if matrix[i][j][2] == '[':
                    dad.append(i)

            for i, val in enumerate(dad):
                if i == 0:
                    continue
                aux = -1
                for val2 in son:
                    if val2 > aux and val2 < val:
                        aux = val2
                for z in range(aux+1, val):
                    matrix[z][j] = "{:8}".format("")

        for i in range(N):
            str_ = ""
            for j in range(M):
                if matrix[i][j] == None:
                    continue
                str_ += str(matrix[i][j])
            print(str_)

    def print_inorder(self):
        self.root.visit_save('INORDER', None)

    def print_postorder(self):
        self.root.visit_save('POSTORDER', None)

    def parse(self, letters):
        pass
