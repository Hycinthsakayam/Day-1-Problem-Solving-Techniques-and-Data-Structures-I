"""Sample data shared by the Set 3 tasks (fixed seed so every run gives the same output)."""
import random

FIRST = ["Arun", "Divya", "Karthik", "Meena", "Rahul", "Sneha", "Vikram", "Priya", "Lakshmi", "Sanjay", "Nithya", "Imran"]
LAST = ["Kumar", "Iyer", "Raja", "Nair", "Sharma", "Patil", "Singh", "Devi", "Gupta", "Reddy", "Khan", "Menon"]


def patient_records(n=20_000, seed=11):
    random.seed(seed)
    return [{"patientId": f"P{100000 + i}", "name": f"{random.choice(FIRST)} {random.choice(LAST)}",
             "age": random.randint(1, 90)} for i in range(n)]


def todays_appointments(n=2000, seed=12):
    random.seed(seed)
    appts = []
    for i in range(n):
        minute = random.randint(0, 9 * 60)            # arrivals between 08:00 and 17:00
        appts.append({"token": i + 1, "patientId": f"P{100000 + random.randint(0, 19_999)}",
                      "urgency": random.randint(1, 5),  # 1 = most urgent
                      "arrival": f"{8 + minute // 60:02d}:{minute % 60:02d}"})
    return appts
