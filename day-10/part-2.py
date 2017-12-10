import numpy as np

inputString = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"

currentPosition = 0
skipSize = 0
numbers = np.array(range(0, 256))

sequence = np.array(list(map(lambda x: ord(x), list(inputString))))
sequence = np.append(sequence, [17, 31, 73, 47, 23])

for x in range(0,64):
    for n in sequence:
        subselect = np.take(numbers, range(currentPosition, currentPosition+n), None, None, mode='wrap')
        reverse = subselect[::-1]
        np.put(numbers, range(currentPosition, currentPosition+n), reverse, mode='wrap')
        # numbers[currentPosition:n] = reverse

        currentPosition = (currentPosition + n + skipSize) % numbers.size
        skipSize = skipSize + 1

# Create dense hash
denseHash = np.zeros(16)

for n in range(0, 16):
    xorNumbers = numbers[n*16:(n*16)+16]
    denseHash[n] = np.bitwise_xor.reduce(xorNumbers)

strings = list(map(lambda x: hex(int(x)).replace('0x', ''), denseHash))
print(strings)
