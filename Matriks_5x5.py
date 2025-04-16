A = [
    [1,5,1,5,1],
    [2,4,2,4,2],
    [3,3,3,3,3],
    [4,2,4,2,4],
    [5,1,5,1,5]
]
B = [
    [5,9,5,9,5],
    [6,8,6,8,6],
    [7,7,7,7,7],
    [8,6,8,6,8],
    [9,5,9,5,9]
]

C = []

for k in range(5):
    baris = []
    for j in range(5):
        jumlah = 0
        for z in range(5):
            jumlah += A[k][z] * B[z][j]
        baris.append(jumlah)
    C.append(baris)

for row in C:
    print(row)            