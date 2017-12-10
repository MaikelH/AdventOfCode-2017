import numpy as np

inputString = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"

currentPosition = 0
skipSize = 0
numbers = np.array(range(0, 256))

sequence = np.array(list(map(lambda x: int(x), inputString.split(","))))

for n in sequence:
    subselect = np.take(numbers, range(currentPosition, currentPosition+n), None, None, mode='wrap')
    reverse = subselect[::-1]
    np.put(numbers, range(currentPosition, currentPosition+n), reverse, mode='wrap')
    # numbers[currentPosition:n] = reverse

    currentPosition = (currentPosition + n + skipSize) % numbers.size
    skipSize = skipSize + 1

# Multiply first two numbers
print(numbers[0] * numbers[1])
