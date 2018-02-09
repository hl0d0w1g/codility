"""
You are given an array A consisting of the integers −1, 0 and 1. A slice of that array is any pair of integers (P, Q) such that 0 ≤ P ≤ Q < N. Your task is to find the longest slice of A whose elements yield a non-negative sum.

Write a function:

    def solution(A)

that, given an array A of length N, consisting only of the values −1, 0, 1, returns the length of the longest slice of A that yields a non-negative sum. If there's no such slice, your function should return 0.

For example, given A = [−1, −1, 1, −1, 1, 0, 1, −1, −1], your function should return 7, as the slice starting at the second position and ending at the eighth is the longest slice with a non-negative sum.

For another example, given A = [1, 1, −1, −1, −1, −1, −1, 1, 1] your function should return 4: both the first four elements and the last four elements of array A are longest valid slices.

Assume that:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1..1].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
"""

def solution(A):
	P = 0
	Q = len(A)
	lslice = 0
	suma = 0
	while Q - P > lslice - 1:
		#print("while1", P, Q, lslice)
		while Q - P > lslice - 1:
			#print("while2", P, Q, lslice)
			_Q = Q
			for i in range(Q - P):
				suma += A[_Q - 1]
				#print("suma: ", suma, A[_Q - 1], _Q - 1)  
				_Q -= 1
			if suma >= 0:
				lslice = Q - P
				break;
			Q -= 1
			suma = 0
		P += 1
		Q = len(A)

	#print(P, Q, lslice)
	return lslice


array = [-1, -1, 1, -1, 1, 0, 1, -1, -1]
print(solution(array))

#SCORE 63%; 100% Correctness, 27% Performance; Correct functionality, problems with scalability