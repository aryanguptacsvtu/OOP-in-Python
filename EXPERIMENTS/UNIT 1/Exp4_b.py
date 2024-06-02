scores =[88,92,79,93,86,79]
print("Original Scores:",scores)

scores.append(80)
print(scores)

scores.remove(92)
print(scores)

print("Count:",scores.count(79))
scores.sort()
print("Sorted scores:",scores)