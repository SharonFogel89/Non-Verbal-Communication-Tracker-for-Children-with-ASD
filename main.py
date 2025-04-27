from core.models import Child, Observer, BehaviorType, BehaviorEntry
from core.logic import add_child, list_all_children, add_observer, list_all_observer
from core.logic import list_all_behavior_type, add_behavior_entry, list_behaviors_by_child
from core.logic import list_all_categories, filter_behaviors, get_behavior_summary_by_category
from core.logic import list_milestone_behavior_types, get_behavior_timeline_monthly, get_behavior_timeline_weekly
from core.logic import list_open_alerts, resolve_alert, check_and_create_alerts

from datetime import date

def show_menu():
    print("\n=== Non-Verbal Communication Tracker ===")
    print(" 1. Add a new child")
    print(" 2. List all children")
    print(" 3. Add a new Observer")
    print(" 4. List all Observers")
    print(" 5. Add a new Behavior Entry")
    print(" 6. Lists all behavior entries for a specific child")
    print(" 7. Filters behavior entries based child, category, observer or/and is consolidated")
    print(" 8. Behavior Summary by Category")
    print(" 9. Lists all behavior types marked as milestone")
    print("10. Timeline (monthly)")
    print("11. Timeline (weekly)")
    print("12. List Open Alerts")
    print("13. Resolve an Alert")

    print(" 0. Exit")

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

        elif choice == "6":
            
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

            child_id = input("Enter child ID to list behaviors: ")
            behaviors = list_behaviors_by_child(child_id)

            print("\nBehaviors registered for the child:")
            for behavior in behaviors:
                behavior_id = behavior[0]
                behavior_date = behavior[4]
                notes = behavior[5]
                consolidated = behavior[7]
                base = behavior[8]
                behavior_name = behavior[9]

                print(f"- {behavior_date}: {behavior_name} | Consolidated: {consolidated} | Pre-existing: {base} | Notes: {notes or 'None'}")


        elif choice == "7":
            
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

            child_id = input("Enter child ID to filter behaviors (or leave blank): ") or None

            categories = list_all_categories()
            print("\nCategories:")
            for category in categories:
                print(f"- {category.id}: {category.name}, {category.description}")

            category_id = input("Enter category ID to filter (or leave blank): ") or None

            observers = list_all_observer()
            print("\nRegistered observer:")
            for observer in observers:
                print(f"- {observer.id}: {observer.name}, {observer.relation}")
            observer_id = input("Enter observer ID to filter (or leave blank): ") or None
            
            is_consolidated_input = input("Only consolidated behaviors? (yes/no/blank): ").lower()

            if is_consolidated_input in ["yes", "y", "YES", "Yes","Y"]:
                is_consolidated = True
            elif is_consolidated_input in ["no", "n", "NO", "No","N"]:
                is_consolidated = False
            else:
                is_consolidated = None

            behaviors = filter_behaviors(child_id, category_id, observer_id, is_consolidated)

            if behaviors:
                for behavior in behaviors:
                    print(f"- {behavior[4]}: {behavior[-2]} ({behavior[-1]}) - Consolidated: {behavior[7]}")
            else:
                print(f"No behavior")

        elif choice == "8":

            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

            child_id = input("Enter child ID for summary: ")
            summary = get_behavior_summary_by_category(child_id)
            
            print("\nBehavior Summary by Category:")
            for category_name, behavior_count in summary:
                print(f"- {category_name}: {behavior_count} behaviors")

        elif choice == "9":

            milestone_behaviors = list_milestone_behavior_types()
            print("\nMilestone Behaviors:")
            for milestone_behavior in milestone_behaviors:
                print(f"- {milestone_behavior.id}: {milestone_behavior.name} — {milestone_behavior.description}")

        elif choice == "10":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")
            
            child_id = input("Enter child ID for timeline (monthly): ")

            timeline = get_behavior_timeline_monthly(child_id)

            if timeline:
                print("\nBehavior Timeline (monthly):")
                for month, behavior_count in timeline:
                    print(f"- {month.strftime('%Y-%m')}: {behavior_count} behaviors")
            else:
                print("No behaviors found for this child.")

        elif choice == "11":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")
            
            child_id = input("Enter child ID for timeline (weekly): ")
            timeline = get_behavior_timeline_weekly(child_id)

            if timeline:
                print("\nBehavior Timeline (weekly):")
                for week, behavior_count in timeline:
                    print(f"- {week.strftime('%Y-%m')}: {behavior_count} behaviors")
            else:
                print("No behaviors found for this child.")

        elif choice == "12":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

            child_id = input("Enter the child's ID to list open alerts: ")
            alerts = list_open_alerts(child_id)

            if alerts:
                print("\nOpen Alerts:")
                for alert in alerts:
                    print(f"- ID {alert[0]} on {alert[2]}: {alert[3]}")
            else:
                print("No open alerts found.")

        elif choice == "13":
            children = list_all_children()
            print("\nRegistered children:")
            for child in children:
                print(f"- {child.id}: {child.name} (Birthday: {child.date_of_birth})")

            child_id = input("Enter the child's ID to list open alerts: ")
            alerts = list_open_alerts(child_id)
            
            if alerts:
                print("\nOpen Alerts:")
                for alert in alerts:
                    print(f"- ID {alert[0]} on {alert[2]}: {alert[3]}")
                    alert_id = input("Enter the alert ID to mark as solved: ")
                    resolve_alert(alert_id)
                    print(f"Alert {alert_id} has been marked as solved.")

            else:
                print("No open alerts found.")
            
            
        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":

    check_and_create_alerts()
    main()