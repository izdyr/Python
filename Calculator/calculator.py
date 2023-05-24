# Print the tutorial and get the problem to solve it.
print("This is Calculator! You can make your question with this symbols (+,  -, x or *, / or ÷)")
question = input("What do you want to solve? ")
# Definition of functions in the order of question, solution, answer.
x, y, z = question.split()
x, z = float(x), float(z)

# How to solve question ?
if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*" or "x":
    answer = x * z
elif y == "/" or "÷" and z != 0:
    answer = x / z
# Print Eror if there is no way to solve it
else:
    print("Eror")
# print answer
print(question, "=", answer)
