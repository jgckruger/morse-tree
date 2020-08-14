from classes.tree import Tree

tree = Tree()
# tree.visit_preorder()
# tree.visit_inorder()
# tree.visit_postorder()

# TODO: optionally read file from parameter
filepath = 'test_input.txt'
with open(filepath) as fp:
    line = fp.readline()
    letters = line.split(' ')
    morse_codes = []
    for letter in letters:
        morse = tree.find(letter)
        morse_codes.append(morse)
    morse_word = ' '.join(morse_codes)
    print(morse_word)
