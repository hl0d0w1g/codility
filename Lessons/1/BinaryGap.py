"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

    def solution(N);

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

        N is an integer within the range [1..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).
"""

def solution(N):
	binary = ""
	while N > 1:
		# convert the rest of the division by 2 to a string and add to the string
		binary += str(N % 2)    
		# make the exact division by 2
		N = N // 2 	

	# add the last 1 			
	binary += str(N) 
	# invert the order of the string			
	binary = binary[::-1]
	# principal gap, is the bigest gap found 		
	pgap = 0 
	# second gap, is the current gap 					
	sgap = 0 					
	for i in binary:
		if i == "0":
			# if the current caracter is a cero, increase the actual gap			
			sgap += 1
		if i == "1":
			# if the current caracter is a one, check what is the biggest gap			
			if sgap > pgap:
				pgap = sgap
			sgap = 0

	return pgap

# SCORE 100%; 100% correcteness, 100% performance



