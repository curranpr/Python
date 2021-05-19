list1 = [1,2,1,2,3,4,2]

list1.sort()

print(list1)

iterationCount = int(len(list1) / 2)

for currPos in range(iterationCount):

    # End of list
    if (currPos == len(list1) - 1):
        break

    else:
        # Match found
        if (list1[currPos] == list1[currPos+1]):
            print("Match found for element ", list1[currPos])
            list1.remove(list1[currPos])
            list1.remove(list1[currPos+1])
            currPos = currPos + 2

        # Match not found
        else:
            print("Match not found for element ", list1[currPos])
            currPos = currPos + 1



