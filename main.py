
productions = {}
print('¿Que archivo desea abrir? (test1, test2, etc')
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

print(nonTerminalSymbols)
print(terminalSymbols)
print(startSymbol)
print(productions)

def parsingTree(productions):
    Q = []
    Q.append(startSymbol)
    depth = 0
    uwv = ""
    while Q and depth != desireDepth and p != uwv:
        q = Q.pop(0)
        i = 0
        done = False
        A = ''
        for x in q:
            if x.isupper():
                A = x
                break

        while not done and p != uwv:
            rules = productions[A]
            for rule in rules:
