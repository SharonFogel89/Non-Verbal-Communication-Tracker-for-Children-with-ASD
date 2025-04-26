from core.models import Child, Observer, BehaviorType, BehaviorEntry
from core.logic import add_child, list_all_children, add_observer, list_all_observer
from core.logic import list_all_behavior_type, add_behavior_entry

from datetime import date

def show_menu():
    print("\n=== Non-Verbal Communication Tracker ===")
    print("1. Add a new child")
    print("2. List all children")
    print("3. Add a new Observer")
    print("4. List all Observers")
    print("5. Add a new Behavior Entry")
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

        elif choice == "4":
            observers = list_all_observer()
            print("\nRegistered observers:")
            for observer in observers:
                print(f"- {observer.id}: {observer.name} (Relation: {observer.relation})")

        elif choice == "5":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")
            child_id = input("Select the children: ")

            observers = list_all_observer()
            print("\nRegistered observer:")
            for observer in observers:
                print(f"- {observer.id}: {observer.name}, {observer.relation}")
            observer_id = input("Select the observer: ")

            behavior_types = list_all_behavior_type()
            print("\nBehavior_Type:")
            for behavior_type in behavior_types:
                print(f"- {behavior_type.id}: {behavior_type.name}, {behavior_type.description}")

            behavior_type_id = input("Select the behavior type: ")
            behavior_date = input("Date observed (YYYY-MM-DD) [Default: today]: ").strip()
            if not behavior_date:
                behavior_date = date.today().isoformat()
            notes = input("Notes (optional): ")  or None
            duration_sec = int(input("Duration sec (optional): ").strip() or 0)
            consolidated_input = input("Is the behavior consolidated? (yes/no): ").strip().lower()
            consolidated = consolidated_input in ["yes", "y", "YES", "Yes","Y"]
            base_input = input("Was the child already performing this behavior before tracking? (yes/no): ").strip().lower()
            base = base_input in ["yes", "y", "YES", "Yes","Y"]             

            behavior_entry = BehaviorEntry(
                id=None,
                child_id=child_id,
                observer_id=observer_id,
                behavior_type_id=behavior_type_id,
                behavior_date=behavior_date,
                notes = notes,
                duration_sec=duration_sec,
                consolidated=consolidated,
                base=base
                )

            behavior_entry_id = add_behavior_entry(behavior_entry)
            print(f"behavior entry {behavior_type_id} added with ID: {behavior_entry_id}")


        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()