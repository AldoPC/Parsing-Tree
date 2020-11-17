from anytree import Node, RenderTree
productions = {}
depth_log = {}
tree = {}
print('¿Que archivo desea abrir? (test1, test2, etc)')
fname = input()
print('¿Cual es el string a evaluar?')
p = input()
print('¿Cual es la profundiddad?')
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
    for x in tree:
        for y in tree[x]:
            if x == key:
                node = Node(y, parent=parent)
                printTree(y,node)

def parsingTree(desireDepth, p):
    Q = []
    Q.append(startSymbol)
    uwv = ""
    depth_log[startSymbol] = 0
    while Q and p != uwv:
        q = Q.pop(0)
        if depth_log[q] == int(desireDepth):
            break
        done = False
        for x in range(len(q)):
            if q[x].isupper():
                partsOfNode = q.partition(q[x])
                break
        while not done and p != uwv:
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
                if not isItTerminal and isTherePrefix:
                    if q in tree.keys():
                        tree[q].append(uwv)
                    else:
                        tree[q] = []
                        tree[q].append(uwv)
                    depth_log[uwv] = depth_log[q] + 1
            done = True
    if uwv == p:
        print("Se pudo procesar el string")
    else:
        print("No se pudo procesar el string")
    initialNode = Node(startSymbol)
    printTree(startSymbol, initialNode)
    for pre, fill, node in RenderTree(initialNode):
        print("%s%s" % (pre, node.name))

parsingTree(desireDepth, p)




