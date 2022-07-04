data=[x.replace('-',' ').replace(':','').split() for x in open("passwords_with_rules.txt", "r")]
print(len(
    list(
        filter(
            lambda x: x[3].count(x[2]) in range(int(x[0]), int(x[1])+1), data)
            )))