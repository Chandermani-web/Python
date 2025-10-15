with open("todo.txt", "r") as file:
    todo = file.read()

# Replace all levels in one go
todo = (todo.replace("high", "####")
            .replace("medium", "######")
            .replace("low", "###"))

with open("todo.txt", "w") as file:
    file.write(todo)
