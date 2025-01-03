class TaskManagementSystem:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description, assignee=None, deadline=None, status="Pending"):
        task = {
            "id": self.task_id_counter,
            "title": title,
            "description": description,
            "assignee": assignee,
            "deadline": deadline,
            "status": status
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        print(f"Task '{title}' added successfully!")

    def view_tasks(self, filter_status=None):
        print("\n--- Task List ---")
        for task in self.tasks:
            if filter_status and task["status"] != filter_status:
                continue
            print(f"ID: {task['id']} | Title: {task['title']} | Assignee: {task['assignee']} | "
                  f"Deadline: {task['deadline']} | Status: {task['status']}")
        print("\n")

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task["id"] == task_id:
                for key, value in kwargs.items():
                    if key in task:
                        task[key] = value
                print(f"Task ID {task_id} updated successfully!")
                return
        print(f"Task ID {task_id} not found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task ID {task_id} deleted successfully!")
                return
        print(f"Task ID {task_id} not found!")

    def view_assignee_tasks(self, assignee):
        print(f"\n--- Tasks Assigned to {assignee} ---")
        for task in self.tasks:
            if task["assignee"] == assignee:
                print(f"ID: {task['id']} | Title: {task['title']} | Deadline: {task['deadline']} | Status: {task['status']}")
        print("\n")


# Main Program
if __name__ == "__main__":
    system = TaskManagementSystem()

    while True:
        print("\n--- Office Task Management Menu ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. View Tasks by Assignee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            assignee = input("Enter assignee (optional): ") or None
            deadline = input("Enter deadline (optional, e.g., YYYY-MM-DD): ") or None
            system.add_task(title, description, assignee, deadline)
        elif choice == "2":
            filter_status = input("Filter by status (optional, e.g., 'Pending', 'Completed'): ") or None
            system.view_tasks(filter_status)
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            title = input("Update title (optional): ") or None
            description = input("Update description (optional): ") or None
            assignee = input("Update assignee (optional): ") or None
            deadline = input("Update deadline (optional, e.g., YYYY-MM-DD): ") or None
            status = input("Update status (optional, e.g., 'Pending', 'Completed'): ") or None
            updates = {k: v for k, v in {"title": title, "description": description, "assignee": assignee, "deadline": deadline, "status": status}.items() if v}
            system.update_task(task_id, **updates)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            system.delete_task(task_id)
        elif choice == "5":
            assignee = input("Enter assignee name: ")
            system.view_assignee_tasks(assignee)
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
