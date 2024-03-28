#123456789
#cd 7,8,3
def getLuhnssum(seq):
    seq = ''.join(seq.split())#incase of spaces and to join all num
    
    if not seq.isdigit():
        raise Exception("Input must contain only digits")
    
    total_sum = 0
    for i in range(len(seq) - 1, -1, -1):
        c = int(seq[i])#to convert str to int
#i=012345   
#v=123456
        if (len(seq)-i) % 2 == 0:
            e = c * 2
            if e >= 10:
                total_sum += e - 9
            else:
                total_sum += e
        else:
            total_sum += c
    return total_sum

def checkIsValidSequence(sequence):
    luhnsValue = getLuhnssum(sequence)
    if luhnsValue % 10 == 0:
        return True
    else:
        return False
    
def getCheckDigit(value):
    luhnsValue = getLuhnssum(value + '0')
    if luhnsValue == 0:
        return 0
    else:
        return (10 - (luhnsValue % 10))  # return calculated check digit

