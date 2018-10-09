def solution(A):
	lenght = len(A)
	media = round(sum(A)/lenght)
	steps = 0
	correct = 0
	while correct != lenght:
		print(A, steps)
		for i in range(lenght):
			if A[i] > media:
				A[i] -= 1
			elif A[i] < media:
				A[i] += 1
			else:
				correct += 1
		steps += 1
		print(correct)

	return steps


H = [11, 3, 7, 1]
print(solution(H))