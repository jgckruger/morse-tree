import json
from classes.node import Node

letters = json.load(open('./letters.json'))

for i in enumerate(letters):

a = Node()