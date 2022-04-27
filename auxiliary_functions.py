def get_user_int_choice(min: int, max: int) -> int:
    # user_choice_str = ""
    user_choice_int = min - 1
    while min > user_choice_int or max < user_choice_int:
        user_choice_str = input(f"enter number between {min} to {max}: ")
        try:
            user_choice_int = int(user_choice_str)
        except ValueError:
            print("Enter valid number!")
        print()
    return user_choice_int