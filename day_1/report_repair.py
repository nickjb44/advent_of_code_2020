def product_of_two_summands(expenses, total):
    complement = {}

    for i, expense in enumerate(expenses):
        complement[total - expense] = i
    
    first_expense = None
    second_expense = None
    for i, expense in enumerate(expenses):
        if expense in complement and complement[expense] != i:
            first_expense = expense 
            second_expense = expenses[complement[expense]]
            print(f"first expense is {first_expense} and second is {second_expense}")
            return first_expense * second_expense
    

example = [1721, 979,366, 299,675, 1456]
print(product_of_two_summands(example, 2020))

expenses = []

with open("expenses_input.txt", "r") as expenses_file:
    for expense in expenses_file:
        expenses.append(int(expense))

print(product_of_two_summands(expenses, 2020))



##----------------------------------------------------------------------##
def product_of_three_summands(expenses, total):
    for i in range(len(expenses)):
        for j in range(i+ 1,len(expenses)):
            for k in range(j+1, len(expenses)):
                if expenses[i]+expenses[j]+expenses[k] == total:
                    print(f"first expense is {expenses[i]} second is {expenses[j]} and third is {expenses[k]}")
                    return expenses[i]*expenses[j]*expenses[k]



print(product_of_three_summands(example, 2020))
print(product_of_three_summands(expenses, 2020))