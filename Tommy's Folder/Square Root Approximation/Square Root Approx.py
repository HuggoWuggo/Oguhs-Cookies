Square_Index = []
num = 1
Counter = 0

#Get first 10000 whole square numbers
for i in range(10000):
    Squared = num * num
    Square_Index.append(Squared)
    num += 1
print(Square_Index)

#Approximate nearest whole square numbers
Approx = int(input('Sqrt? >> '))
for L in range(len(Square_Index)):
    if int(Square_Index[Counter]) - Approx >= 0:
        Diff1 = int(Square_Index[Counter]) - Approx
        Diff2 = Approx - int(Square_Index[Counter - 1])
        if Diff1 < Diff2:
            Closest_Whole = Square_Index[Counter]
            Counter += 1
            Difference = Diff1
        else:
            Closest_Whole = Square_Index[Counter - 1]
            Difference = Diff2
        break
    else:
        Counter += 1

#Getting Square root of approximation
Sqrt = int(Closest_Whole) / Counter

#Solve with formula
Answer = Sqrt + Difference / (2 * Sqrt)
print(f'Approximated Square Root is {Answer}')