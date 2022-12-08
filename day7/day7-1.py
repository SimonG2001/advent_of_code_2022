


score = 0
dirs = {}
needToFree = 0
smallest = 999999999999999
def calculateDir(start, input, name):
    global score, dirs, needToFree, smallest
    i = start
    dirSize = 0
    while input[i].split()[0] != '$':
        if input[i].split()[0] == "dir":
            dirname = input[i].split()[1]
            j = i
            level = 0
            while True:
                if input[j] == "$ cd ..":
                    level -= 1
                elif input[j].split()[1] == "cd":
                    level += 1
                if level == 1 and input[j-2] == "$ cd " + dirname:
                    break
                j += 1
            dirSize += calculateDir(j, input, dirname)
        else:
            dirSize += int(input[i].split()[0])
        i += 1
        if i > len(input)-1:
            break
    dirs[name] = dirSize

    if dirSize >= needToFree and dirSize < smallest:
        smallest = dirSize

    if dirSize <= 100000:
        score += dirSize
    return dirSize


with open('input.txt', 'r') as f:
    lines = f.readlines()
    alllines = []
    totalSize = 0 
    for line in lines:
        alllines.append(line.split("\n")[0])
        if line.split()[0] != "$" and line.split()[0] != "dir":
            totalSize += int(line.split()[0])

    freeSpace = 70000000 - totalSize
    needToFree = 30000000 - freeSpace
    dirs["/"] = calculateDir(2, alllines, "/")
    



print("exersice 1: ", score)
print("exersice 2: ", smallest)

with open('input.txt') as file:
    commands = file.read().split('\n')
lines = [x.split(' ') for x in commands]
dirs = {}
curDirs = []
print('Day 07 Part 1:', sum([x for x in dirs.values() if x <= 100000] if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('input.txt').read().split('\n')]] else ''))
print('Day 07 Part 2:', min([x for x in dirs.values() if x > dirs['//']-40000000]) if not (dirs := {}) and not (curDirs := []) and [((l[0] == '$' and l[1] == 'cd') and (((l[2] == '/') and (curDirs := ['//']) and not (dirs.update({'//':0}))) or (l[2] == '..' and curDirs.pop()) or ((curDir := '/'.join(curDirs) + '/' + l[2]) and not curDirs.append(curDir) and (not dirs.get(curDir) and not dirs.update({curDir:0}))))) or (l[0].isdigit() and [dirs.update({d: dirs[d] + int(l[0])}) for d in curDirs]) for l in [c.split(' ') for c in open('input.txt').read().split('\n')]] else '')
