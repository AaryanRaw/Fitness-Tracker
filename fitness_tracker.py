class Exercise:
    def __init__(self,name,duration_min,intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity



class User:
    def __init__(self,username):
        self.username = username
        self.exercise = []
        self.goals = {}


    def log_exercise(self,exercise):
        self.exercise.append(exercise)

    def calculate_calories_burned(self):
        total_calories = 0
        for exercise in self.exercise:
            calories = exercise.duration_min * exercise.intensity
            total_calories = calories
        return total_calories

    def set_goal(self,goal_type,target_value):
        self.goals[goal_type] = target_value


    def track_progress(self):

        total_calories_burned = self.calculate_calories_burned()
        if 'calories' in self.goals:
            goal_calories = self.goals['calories']
            progress_percentage = (total_calories_burned / goal_calories)* 100
            return progress_percentage
        else:
            return "Get some calories bro"


def log_exercise(user):
    name = input("Enter the exercise name: ")
    duration = int(input("Enter duration in minutes: "))
    intensity = int(input("Enter intensity from 1-10: "))
    exercise = Exercise(name,duration,intensity)
    user.log_exercise(exercise)
    print("Exercise has been logged!")


def set_goal(user):
    goal_type = input("Enter goal type (i.e., calories): ")
    target_value = int(input("Enter target value: "))
    user.set_goal(goal_type,target_value)
    print("Goal has been set!")



def track_progress(user):
    progress = user.track_progress()
    if progress != "Get some calories bro":
        print(f"Progress towards goal: {progress:.2f}%")
    else:
        print("No goal has been set")


def main():
    username = input("Enter your username: ")
    user = User(username)

    while True:
        print("\n--- Fitness Tracking System ---")
        print("1. Log Exercise")
        print("2. Set Goal")
        print("3. Track Progress")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")
        if choice == "1":
            log_exercise(user)
        elif choice == "2":
            set_goal(user)
        elif choice == "3":
            track_progress(user)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Ummmmm Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()




