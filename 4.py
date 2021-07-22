def revString(x):
    tempString = [char for char in x]
    y = []
    for i in range(len(tempString)):
        out = tempString.pop(len(tempString)-1)
        y.append(out)
    return ''.join(y)


def test_RevString():
    print(revString('Kasur'))
    print(revString('Aplikasi'))
    print(revString('lemari'))


test_RevString()
