result1 = float(input())
result2 = float(input())
result3 = float(input())

mean = (result1+result2+result3)/3
print(mean)

if mean>=60.0:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we "
          "will not be able to offer you admission.")
