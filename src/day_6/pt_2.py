total_count = 0
with open("answers.txt") as answers:
    group_answers = {}
    n_people_in_group = 0
    for answer in answers:
        answer = answer.rstrip()
        if len(answer) == 0:
            for char in group_answers:
                if group_answers[char] == n_people_in_group:
                    total_count += 1
            n_people_in_group = 0
            group_answers = {}

        else:
            n_people_in_group += 1
            for char in answer:
                if char in group_answers:
                    group_answers[char] += 1
                else:
                    group_answers[char] = 1
                     
    for char in group_answers:
        if group_answers[char] == n_people_in_group:
            total_count += 1
    n_people_in_group = 0
    group_answers = {}

print(total_count)