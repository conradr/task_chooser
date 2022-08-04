# task1 = "Wash"
# task2 = "Cook"
# task3 = "Clean"
# task4 = "Ironing"
# task5 = "Clothes"


# def decide(task1, task2):
#     if task1 == "Wash" and task2 == "Cook" or task1 == "Cook" and task2 == "Wash":
#         print(f"I got wash and cook, so wash wins")
#     elif task1 == "Wash" and task2 == "Clean" or task1 == "Clean" and task2 == "Wash":
#         print(f"I got wash and clean, so you're cleaning")
#     elif task1 == "Wash" and task2 == "Iron" or task1 == "Iron" and task2 == "Wash":
#         print(f"I got wash and iron, so iron wins")
#     elif task1 == "Wash" and task2 == "Clothes" or task1 == "Clothes" and task2 == "Wash":
#         print(f"I got wash and clothes, so wash dishes wins")
#     elif task1 == "Cook" and task2 == "Clean" or task1 == "Clean" and task2 == "Cook":
#         print(f"I got Cook and Clean, so you're Cooking")
#     elif task1 == "Cook" and task2 == "Iron" or task1 == "Iron" and task2 == "Cook":
#         print(f"I got cook and iron, so iron wins")
#     elif task1 == "Cook" and task2 == "Clothes" or task1 == "Clothes" and task2 == "Cook":
#         print(f"I got cook and clothes, so clothes wins")


# decide(task3, task2)

tasks = [
    {
        "name": "wash dishes",
        "preferred over": ["cook dinner", "wash clothes"]
    },
    {
        "name": "cook dinner",
        "preferred over": ["clean windows", "ironing"]
    },
    {
        "name": "clean windows",
        "preferred over": ["wash dishes", "ironing"]
    },
    {
        "name": "ironing",
        "preferred over": ["wash dishes", "wash clothes"]
    },
    {
        "name": "wash clothes",
        "preferred over": ["cook dinner", "clean windows"]
    }]


def decider(task1, task2):
    for task in task1["preferred over"]:
        if task1 == task2:
            print(f"The tasks are the same")
            return
        elif task == task2["name"]:
            print(f"{task1['name']} is the winner")
            return
        else:
            print(f"{task2['name']} is the winner")


decider(tasks[1], tasks[2])
