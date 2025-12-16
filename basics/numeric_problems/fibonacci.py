import numpy as np

line = int(input("Enter the line number :"))
column = int(input("Enter the column number :"))

# Total cell number
totalcell = line * column

# Fibonacci sequence
fibonacci = [0, 1]
while len(fibonacci) < totalcell:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# making matrix with fibonacci sequence
fibonacci_dizi = np.array(fibonacci[:totalcell])
matris = fibonacci_dizi.reshape((line, column))

# Printin Matrix
print("\nFibonacci Matrisi:")
print(matris)
