"""Parsing Tree Builder

This script allows the user to process a string with a desire depth
in which the tree will be built.

This tool accepts text documents (.txt).

This script requires that `anytree` be installed within the Python
environment you are running this script in.

This file contains the following funcitons:

    * parsingTree - builds a dictionary of the tree when its processing the string.
    * printTree - builds the tree to be displayed in the console.
"""
from anytree import Node, RenderTree
productions = {}
depth_log = {}
tree = {}
print('Which .txt file? (test1, test2, etc)')
fname = input()
print('Which string are you evaluating?')
p = input()
print('Until which depth?')
desireDepth = input()
fname = fname + '.txt'
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1

with open(fname, 'r') as f:
    nonTerminalSymbols = f.readline().split(",")
    nonTerminalSymbols[len(nonTerminalSymbols)-1] = nonTerminalSymbols[len(nonTerminalSymbols)-1].strip()

    terminalSymbols = f.readline().split(",")
    terminalSymbols[len(terminalSymbols)-1] = terminalSymbols[len(terminalSymbols)-1].strip()

    startSymbol = f.readline()
    startSymbol = startSymbol.strip()
    
    for x in range(count-3):

        temp = f.readline()
        temp = temp.split("->")
        temp[len(temp)-1] = temp[len(temp)-1].strip()
        key = temp[0]
        value = temp[1]
        if key in productions.keys():
            productions[key].append(value)
        else:
            productions[key] = []
            productions[key].append(value)

def printTree(key, parent):
    """Gets the parent node and add its correspondig child

    Parameters
    ----------
    key : str
        the value of the child
    parent : node
        the parent node which is going to have the key value as a child

    Returns
    -------
    list
        a list of strings used that are the header columns
    """
    for x in tree:
        for y in tree[x]:
            if x == key:
                node = Node(y, parent=parent)
                printTree(y,node)

def parsingTree():
    """Builds a dictionary of the tree when its processing the string 

    Parameters
    ----------
    

    Returns
    -------
    
    """
    Q = []
    Q.append(startSymbol)
    uwv = ""
    depth_log[startSymbol] = 0
    match = False
    while Q and not match:
        q = Q.pop(0)
        if depth_log[q] == int(desireDepth):
            break
        done = False
        for x in range(len(q)):
            if q[x].isupper():
                partsOfNode = q.partition(q[x])
                break
        while not done and not match:
            process = productions[partsOfNode[1]]
            for w in process:
                u = partsOfNode[0]
                v = partsOfNode[2]
                uwv = u + w + v
                isItTerminal = False
                for x in uwv:
                    if x.isupper():
                        isItTerminal = True
                        break
                isTherePrefix = True
                for x in range(len(u)):
                    if x < len(p) and u[x] != p[x]:
                        isTherePrefix = False
                        break
                if isItTerminal and isTherePrefix:
                    if q in tree.keys():
                        tree[q].append(uwv)
                    else:
                        tree[q] = []
                        tree[q].append(uwv)
                    depth_log[uwv] = depth_log[q] + 1
                    Q.append(uwv)
                    if uwv == p:
                        match = True
                if not isItTerminal and isTherePrefix:
                    if q in tree.keys():
                        tree[q].append(uwv)
                    else:
                        tree[q] = []
                        tree[q].append(uwv)
                    depth_log[uwv] = depth_log[q] + 1
                    if uwv == p:
                        match = True
            done = True
    if match:
        print("The string was accepted")
    else:
        print("The string was not accepted")
    root = Node(startSymbol)
    printTree(startSymbol, root)
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

parsingTree()
