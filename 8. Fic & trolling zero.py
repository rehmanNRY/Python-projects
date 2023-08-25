def fic(nmbr):
    if nmbr == 0 or nmbr == 1:
        return 1
    else:    
        return nmbr * fic(nmbr-1)
def trollingZero(nmbr):
    count = 0
    i = 5
    while nmbr//i != 0:
        count += int(nmbr/i)
        i*=5
    return count
nmbr = int(input("Enter the number: "))
print(fic(nmbr))
print(trollingZero(nmbr))