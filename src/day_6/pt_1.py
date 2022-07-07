total_count = 0
with open("answers.txt") as answers:
    group_answers = set()
    for answer in answers:
        answer = answer.rstrip()
        if len(answer) == 0:
            total_count += len(group_answers)
            group_answers = set()
        else:
            for char in answer:
                group_answers.add(char)
    total_count += len(group_answers)

print(total_count)