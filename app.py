from negotiator import SalaryNegotiator


class SalaryNegotiatorApp:

    def __init__(self):

        self.engine = SalaryNegotiator()

    def negotiate_salary(self):

        try:

            print("\n========== Salary Negotiation ==========\n")

            current_salary = float(

                input("Current Salary: ")

            )

            expected_salary = float(

                input("Expected Salary: ")

            )

            experience = int(

                input("Years of Experience: ")

            )

            print("\nSkill Levels")

            print("1. Beginner")

            print("2. Intermediate")

            print("3. Advanced")

            print("4. Expert")

            option = input("\nChoose Skill Level: ")

            skills = {

                "1": "Beginner",

                "2": "Intermediate",

                "3": "Advanced",

                "4": "Expert"

            }

            if option not in skills:

                print("\nInvalid Skill Level.")

                return

            result = self.engine.calculate_offer(

                current_salary,

                expected_salary,

                experience,

                skills[option]

            )

            print("\n========== RESULT ==========\n")

            print(

                "Candidate Score      :",

                result["candidate_score"]

            )

            print(

                "Recommendation       :",

                result["recommendation"]

            )

            print(

                "Suggested Salary     : ₹",

                result["recommended_offer"]

            )

            print(

                "Negotiation Advice   :",

                result["advice"]

            )

        except ValueError:

            print("\nInvalid Input.")

    def menu(self):

        while True:

            print("\n")

            print("=" * 45)

            print("      SALARY NEGOTIATOR")

            print("=" * 45)

            print("1. Salary Negotiation")

            print("2. View History")

            print("3. Clear History")

            print("4. Exit")

            choice = input(

                "\nEnter Choice: "

            )

            if choice == "1":

                self.negotiate_salary()

            elif choice == "2":

                self.engine.show_history()

            elif choice == "3":

                answer = input(

                    "\nClear History? (y/n): "

                )

                if answer.lower() == "y":

                    self.engine.clear_history()

            elif choice == "4":

                print("\nGoodbye!")

                break

            else:

                print("\nInvalid Choice.")


if __name__ == "__main__":

    app = SalaryNegotiatorApp()

    app.menu()