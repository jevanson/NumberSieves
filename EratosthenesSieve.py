import math

@staticmethod
def eratosthenes_sieve(N):
	primes = []

	A = [True] * (N+1)
	sqrtN = math.floor( math.sqrt(N) )

	for i in range(2, sqrtN + 1):
		if A[i]:
			j = 0
			while i*i+j*i <= N:
				A[i*i+j*i] = False
				j = j + 1

	for i in range(2,N+1):
		if A[i]:
			primes.append(i)

	return primes

if __name__ == '__main__':
	result = eratosthenes_sieve(100)
	print(result)