1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
Program:
  
rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')
    
_______________________________________________________
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

Program:
  
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
_______________________________________________________

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
Program

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
_______________________________________________________

Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
Program: –

rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
_______________________________________________________

Pattern: –

0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
Program

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
_______________________________________________________

Pattern: –

1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
Program: –

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
_______________________________________________________

Pattern 1: –

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

Program: –

rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
 _______________________________________________________

Pattern 2: –

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

Program

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
_______________________________________________________

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Program: –

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
_______________________________________________________
Pattern: –

1
3 2
6 5 4
10 9 8 7
Program: –

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
_______________________________________________________

Pattern: –

          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
Program: –

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
_______________________________________________________

Pattern:

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
Program: –

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

rows = 7
print_pascal_triangle(rows)
 Run
Square pattern with numbers

_______________________________________________________

Pattern: –

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
Program: –

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
_______________________________________________________

Pattern: –

1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
Program: –

rows = 8
rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1)
        square = i * j
        print(i * j, end='  ')
    print()
 _______________________________________________________

* 
* * 
* * * 
* * * * 
* * * * * 

Program: –


rows = 5
for i in range(0, rows)
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
_______________________________________________________

Pattern: –

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

Program: –


rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

_______________________________________________________
Pattern: –

* * * * *  
* * * *  
* * *  
* *  
*


Program: –

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")
_______________________________________________________

Pattern: –

        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
Program:

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
