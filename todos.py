todos_list = []

while True:
       
    todo_description = input("Enter todo description: ")
    todo_date = input("Enter todo's date: ")
        
    todo = {
    'description': todo_description,
    'date': todo_date
    }

    todos_list.append(todo)
  
    for p in todos_list:
        print(f"Todo task: {p['description']}, When: {p['date']}")
