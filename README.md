# Salary Negotiator

## Overview

Salary Negotiator is a terminal-based Python application that helps estimate a reasonable salary offer based on a candidate's current salary, expected salary, experience, and skill level.

It provides a recommendation, negotiation advice, and stores previous negotiations for future reference.

---

## Features

- Salary Recommendation
- Candidate Score Calculation
- Skill Level Evaluation
- Negotiation Advice
- Negotiation History
- JSON Storage
- Terminal-Based Interface

---

## Project Structure

salary-negotiator/

├── negotiator.py

├── app.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

```bash
python app.py
```

---

## Menu

```
1. Salary Negotiation
2. View History
3. Clear History
4. Exit
```

---

## Example

Current Salary

```
600000
```

Expected Salary

```
900000
```

Experience

```
5 Years
```

Skill Level

```
Advanced
```

---

## Output

```
Candidate Score : 53

Recommendation : Competitive Candidate

Suggested Salary : ₹825000

Advice :

Negotiate with supporting achievements.
```

---

## Generated File

salary_history.json

Example

```json
[
    {
        "current_salary": 600000,
        "expected_salary": 900000,
        "experience": 5,
        "skill_level": "Advanced",
        "recommended_offer": 825000.0,
        "candidate_score": 53,
        "recommendation": "Competitive Candidate",
        "advice": "Negotiate with supporting achievements."
    }
]
```

---

## Future Improvements

- Location Based Salary
- Company Budget Analysis
- Skill Weighting
- Industry Specific Salary
- Salary Trends
- PDF Report Export
- Candidate Comparison
- Experience Level Charts
- Market Salary Database
- AI Recommendation
- Recruiter Dashboard

---

## License

MIT License