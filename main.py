from analyzer.strength_checker import analyze_strength
from analyzer.recommender import generate_recommendations
from analyzer.breach_checker import is_password_breach
from analyzer.generator import generate_secure_password
from analyzer.bulk_pwd_checker import batch_password_checker
def main():
    print("Hello from password-audit!")
    while True:
        print("\n What would you like to do?")
        print("1. Audit a single password")
        print("2. Process a batch of passwords")
        print("3. Generate a secure password")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            password = input("Enter a password to audit :")
            breached = is_password_breach(password)
            print(f"\n Breached status: {'Breached password' if breached else 'No breaches found'}")
            report = analyze_strength(password)
            recommendations = generate_recommendations(report)
            print("\nPassword Report:")
            for key, value in report.items():
                print(f"{key}: {value}")

            print("\nRecommendations:")
            for tip in recommendations:
               print(f"- {tip}")

        elif choice == "2":
            filepath = input("Enter the path to the file containing passwords: ")
            result = batch_password_checker(filepath)
            print(result)

        elif choice == "3":
            length = int(input("Enter the length of your desired password (minimum 8 characters): "))
            secure_password = generate_secure_password(length)
            print(f"Generated secure password: {secure_password}")

        elif choice == "4":
            print("Thank you for using password-audit!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
