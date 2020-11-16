
tree = {}
print('Que archivo desea abrir? (test1, test2, etc')
fname = input()
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
        if key in tree.keys():
            tree[key].append(value)
        else:
            tree[key] = []
            tree[key].append(value)

print(nonTerminalSymbols)
print(terminalSymbols)
print(startSymbol)
print(tree)

    
