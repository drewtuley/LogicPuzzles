# "I've got ten or more daughters"
# "I've got less than ten daughters"
# "I've got at least one daughter"

# If only one of these statements are true, how many daughters have I got?

for daughter_count in range(0, 11):
    truth_count = 0
    if daughter_count >= 10:
        truth_count += 1
    if daughter_count < 10:
        truth_count += 1
    if daughter_count >= 1:
        truth_count += 1

    if truth_count == 1:
        print('Only 1 logical truth - ergo I must have {dc} daughters'.format(dc=daughter_count))
