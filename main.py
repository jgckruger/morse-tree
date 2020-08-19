from classes.tree import Tree
import sys
tree = Tree()
#tree.visit_preorder()
#tree.visit_inorder()
#tree.visit_postorder()
#tree.print_preorder()
tree.print_inorder()
#tree.print_postorder()

# TODO: optionally read file from parameter
try:
    filepath = sys.argv[1]
except:
    filepath = 'test_input.txt'

final_translate = ""

with open(filepath) as fp:
    line = fp.readline()
    while line:
        letters = line.split(' ')
        morse_codes = []
        for letter in letters:
            morse = tree.find(letter.strip())
            morse_codes.append(morse)
        morse_word = ''.join(morse_codes)
        final_translate += morse_word + " "
        line = fp.readline()

print(final_translate)
