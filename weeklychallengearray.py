array1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 5, 2, 7]
array2 = ['!', '@', '#', '$', '%', '^', '&', '*', 10, 1, 2, 3, 4, 5]
shuffledarray = []
num = 0
for item in range(min(len(array1), len(array2))):
	shuffledarray.append(array1[num])
	shuffledarray.append(array2[num])
	num += 1

if num < max(len(array1), len(array2)):   #can all be replaced by shuffledarray.extend(array1[min(len(array1), len(array2)):] or array2[min(len(array1), len(array2)):])
	if len(array1) < len(array2):
		ugly = len(array2) - len(array1)
		while ugly > 0:
			shuffledarray.append(array2[num])
			num += 1
			ugly -= 1
	elif len(array1) > len(array2):
		ugly = len(array1) - len(array2)
		while ugly > 0:
			shuffledarray.append(array1[num])
			num += 1
			ugly -= 1

print(shuffledarray)