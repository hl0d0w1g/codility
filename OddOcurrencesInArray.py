"""
A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element 
that has the same value, except for one element that is left unpaired.

For example, in array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

        the elements at indexes 0 and 2 have value 9,
        the elements at indexes 1 and 3 have value 3,
        the elements at indexes 4 and 6 have value 9,
        the element at index 5 has value 7 and is unpaired.

Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Assume that:

        N is an odd integer within the range [1..1,000,000];
        each element of array A is an integer within the range [1..1,000,000,000];
        all but one of the values in A occur an even number of times.

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
"""

def solution(A):
	N = len(A) - 1
	while A.index(A[N]) != N:
		print(N, A.index(A[N]), A.index(A[N]) != N, A)
		if A[A.index(A[N])] != 0:
			A[A.index(A[N])] = 0
		N -= 1
	return A[N]


array = [9, 3, 9, 9, 7, 9, 7, 5, 4, 3, 4, 6, 5, 3, 6]
print(solution(array))

#SCORE: 66%; 100% correctness, 25% performance
#Detected time complexity: O(N**2)
"""
medium2
medium random test n=100,003
	TIMEOUT ERROR
	running time: >6.00 sec., time limit: 0.48 sec.

big1
big random test n=999,999, multiple repetitions
	TIMEOUT ERROR
	running time: >9.00 sec., time limit: 3.58 sec.

big2
big random test n=999,999
	TIMEOUT ERROR
	running time: >9.00 sec., time limit: 3.82 sec.

"""