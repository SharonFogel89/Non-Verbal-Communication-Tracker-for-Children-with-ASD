from core.models import Child, Observer
from core.logic import add_child, list_all_children, add_observer

def show_menu():
    print("\n=== Non-Verbal Communication Tracker ===")
    print("1. Add a new child")
    print("2. List all children")
    print("3. Add a new Observer")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Child's name: ")
            date_of_birth = input("Date of birth (YYYY-MM-DD): ")
            diagnosis = input("Date of diagnosis (YYYY-MM-DD, optional): ") or None
            notes = input("Notes (optional): ") or None

            child = Child(
                id=None,
                name=name,
                date_of_birth=date_of_birth,
                date_of_diagnosis=diagnosis,
                notes=notes
            )

            child_id = add_child(child)
            print(f"Child {child.name} added with ID: {child_id}")

        elif choice == "2":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

        elif choice == "3":
            name = input("Observer's name: ")
            relation = input("Relation: (mother, father, terapist) ")
            notes = input("Notes (optional): ") or None

            observer = Observer(
                id=None,
                name=name,
                relation=relation,
                notes=notes
            )

            observer_id = add_observer(observer)
            print(f"Observer {observer.name} added with ID: {observer_id}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()