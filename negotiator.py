import json
import os


class SalaryNegotiator:

    def __init__(self):

        self.history_file = "salary_history.json"

        self.history = []

        self.load_history()

    def load_history(self):

        if os.path.exists(self.history_file):

            try:

                with open(
                    self.history_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.history = json.load(file)

            except:

                self.history = []

    def save_history(self):

        with open(
            self.history_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.history,
                file,
                indent=4
            )

    def calculate_offer(

        self,

        current_salary,

        expected_salary,

        experience,

        skill_level

    ):

        score = 0

        if experience >= 10:
            score += 35

        elif experience >= 7:
            score += 30

        elif experience >= 5:
            score += 25

        elif experience >= 3:
            score += 20

        else:
            score += 10

        level = skill_level.lower()

        if level == "expert":
            score += 35

        elif level == "advanced":
            score += 28

        elif level == "intermediate":
            score += 20

        else:
            score += 10

        difference = expected_salary - current_salary

        if difference <= 0:

            suggestion = current_salary

            advice = "Your expectation is below or equal to your current salary."

        elif difference <= current_salary * 0.20:

            suggestion = expected_salary

            advice = "Your expected salary is realistic."

        elif difference <= current_salary * 0.40:

            suggestion = current_salary + difference * 0.75

            advice = "Negotiate with supporting achievements."

        else:

            suggestion = current_salary * 1.30

            advice = "Your expectation is very high. Be prepared to justify it."

        if score >= 60:
            recommendation = "Strong Candidate"

        elif score >= 40:
            recommendation = "Competitive Candidate"

        else:
            recommendation = "Needs Skill Improvement"

        result = {

            "current_salary": current_salary,

            "expected_salary": expected_salary,

            "experience": experience,

            "skill_level": skill_level,

            "recommended_offer": round(suggestion, 2),

            "candidate_score": score,

            "recommendation": recommendation,

            "advice": advice

        }

        self.history.append(result)

        self.save_history()

        return result

    def show_history(self):

        if not self.history:

            print("\nNo Negotiation History.")

            return

        print("\n========== HISTORY ==========\n")

        for index, item in enumerate(

            self.history,

            start=1

        ):

            print(f"Candidate {index}")

            print(

                "Current Salary :",

                item["current_salary"]

            )

            print(

                "Expected Salary:",

                item["expected_salary"]

            )

            print(

                "Experience     :",

                item["experience"],

                "Years"

            )

            print(

                "Skill Level    :",

                item["skill_level"]

            )

            print(

                "Recommended    :",

                item["recommended_offer"]

            )

            print(

                "Score          :",

                item["candidate_score"]

            )

            print(

                "Recommendation :",

                item["recommendation"]

            )

            print(

                "Advice         :",

                item["advice"]

            )

            print("-" * 50)

    def clear_history(self):

        self.history.clear()

        self.save_history()

        print("\nHistory Cleared.")