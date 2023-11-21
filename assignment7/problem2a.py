import sys
import numpy as np


def makeMatrix(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[1:]
    m = []
    for line in lines:
      m.append([int(i) for i in line.split()])
  return np.array(m)


def writeToFile(ans):
  with open('problem2aOp.txt', 'w') as f:
    f.write(str(ans))


def main():
  args = sys.argv[1:]
  if len(args) != 2:
    print('usage: filename')
    sys.exit(1)
  fA = args[0]
  fB = args[1]
  mA = makeMatrix(fA)
  mB = makeMatrix(fB)
  detA = np.linalg.det(mA)
  if (detA != 0):
    return writeToFile('Unique solution')
  dets = []
  for i in range(3):
    mAX = mA.copy()
    mAX[:, i] = mB[:, 0]
    dets.append(np.linalg.det(mAX))
  if (dets[0] == 0 and dets[1] == 0 and dets[2] == 0):
    return writeToFile('Infinite solutions')
  else:
    return writeToFile('No solution')


main()
