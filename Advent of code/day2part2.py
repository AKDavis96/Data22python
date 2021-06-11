list = [str(x) for x in open("day2_numbers.txt", "r").readlines()]
invalid_passwords = []
valid_passwords = []
for i in list:
    policy = i.split(": ")[0]
    password1 = i.split(": ")[1]
    password = password1.splitlines()[0]
    policy_range = policy.split(" ")[0]
    policy_letter = policy.split(" ")[1]
    policy_first = int(policy_range.split("-")[0])
    policy_second = int(policy_range.split("-")[1])
    count = 0
    if policy_letter == password[policy_first - 1]:
        count += 1
    if policy_letter == password[policy_second - 1]:
        count += 1
    else:
        count += 0

    if count == 1:
        valid_passwords.append(password)
    else:
        invalid_passwords.append(password)

print(len(valid_passwords))
print(len(invalid_passwords))
print(valid_passwords)
print(invalid_passwords)




