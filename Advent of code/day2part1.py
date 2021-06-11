list = [str(x) for x in open("day2_numbers.txt", "r").readlines()]
invalid_passwords = []
valid_passwords = []

for i in list:
    policy = i.split(": ")[0]
    password1 = i.split(": ")[1]
    password = password1.splitlines()[0]
    policy_range = policy.split(" ")[0]
    policy_letter = policy.split(" ")[1]
    policy_lower = int(policy_range.split("-")[0])
    policy_upper = int(policy_range.split("-")[1])
    count = 0
    for y in password:
        if y == policy_letter:
            count += 1
    if count not in range(policy_lower, policy_upper + 1):
        invalid_passwords.append(password)
    else:
        valid_passwords.append(password)

print(len(valid_passwords))
print(len(invalid_passwords))
print(valid_passwords)
print(invalid_passwords)