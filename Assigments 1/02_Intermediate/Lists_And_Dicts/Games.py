def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "⚠️ Index out of range!"

def modify_element(lst, index, new_value):
    """Modifies the list at the given index with a new value or returns an error if out of range."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"✅ Updated list: {lst}"
    return "⚠️ Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced portion of the list with proper index handling."""
    if 0 <= start <= end <= len(lst):
        return f"Sliced list ({start}:{end}): {lst[start:end]}"
    return "⚠️ Invalid slice range!"

def index_game():
    """Interactive list manipulation game."""
    game_list = [1, 2, 3, 4, 5]  # Example list
    print(f"\n Welcome to the Index Game! Current list: {game_list}")

    while True:
        print("\nChoose an operation: (1) Access, (2) Modify, (3) Slice, (4) Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                index = int(input("Enter an index: ").strip())
                print(access_element(game_list, index))
            except ValueError:
                print("⚠️ Invalid input! Enter a number.")

        elif choice == "2":
            try:
                index = int(input("Enter an index to modify: ").strip())
                new_value = input("Enter a new value: ").strip()
                print(modify_element(game_list, index, new_value))
            except ValueError:
                print("⚠️ Invalid input! Enter a number.")

        elif choice == "3":
            try:
                start = int(input("Enter start index: ").strip())
                end = int(input("Enter end index: ").strip())
                print(slice_list(game_list, start, end))
            except ValueError:
                print("⚠️ Invalid input! Enter numbers.")

        elif choice == "4":
            print("Thanks for playing! Exiting now...")
            break

        else:
            print("⚠️ Invalid choice! Please select 1-4.")

if __name__ == '__main__':
    index_game()
