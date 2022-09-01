from pylinkedstack import Stack


def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        line = str(line[:-1])
        for token in line:
            if token in "{[(":
                # print(token)
                s.push(token)
            elif token in "}])":
                # print(token)
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (token == '}' and left != '{') or \
                        (token == ']' and left != '[') or \
                            (token == ')' and left != '('):
                        return False

    return s.isEmpty()


srcfile = open('sourcefile.txt', 'r')

if(isValidSource(srcfile)):
    print("Valid")
else:
    print("Not Valid")
