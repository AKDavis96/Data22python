
list = [str(x) for x in open("day2_numbers.txt", "r").readlines()]
invalid_passwords = []
valid_passwords = []

for i in list:
    policy = (i.split(": ")[0])
    password1 = (i.split(": ")[1])
    password = password1.splitlines()[0]
    policy_range = policy.split(" ")[0]
    policy_character = policy.split(" ")[1]
    range_lower = int(policy_range.split("-")[0])
    range_upper = int(policy_range.split("-")[1])
    count = password.count(policy_character)

    if count not in range(range_lower, range_upper + 1):
        invalid_passwords.append(i)
    else:
        valid_passwords.append(i)

print(len(valid_passwords))