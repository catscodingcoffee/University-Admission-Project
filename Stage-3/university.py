num_applicants = int(input())
num_accepted = int(input())
applicants = []
for i in range(num_applicants):
    info = input()
    info_split = info.split(' ')
    applicants.append(info_split)

sorted_applicants = sorted(
    applicants,
    key = lambda x:(x[2]),
    reverse=True
)

print("Successful applicants:")
for i in range(num_accepted):
    print(f"{sorted_applicants[i][0]} {sorted_applicants[i][1]}")
