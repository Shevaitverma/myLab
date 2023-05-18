k=1
q=10
for i in range(10):
	for j in range(q):
		print(" ", end="")
	for c in range(k):
		if i == 5:
			print("* ", end="")
		else:
			if c == 0:
				print("* ", end="")
			elif c == k-1:
				print("* ", end=" ")
			else:
				print(" ", end=" ")
	print()
	q=q-1
	k=k+1