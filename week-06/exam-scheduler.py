from datetime import datetime, timedelta

# Global variable
college_name = "Bhaktapur Multiple Campus"

start_date = "2025-05-01"

exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]

def parse_date(date_str):
    # Converts the date string into datetime object and returns it
    return datetime.strptime(date_str, "%Y-%m-%d")

def get_exam_date(start_str, days):
    # Adds the start date and days then converts it into string and returns it
    start_date_obj = parse_date(start_str)
    exam_date_obj = start_date_obj + timedelta(days=days)
    return exam_date_obj.strftime("%Y-%m-%d")

def print_schedule(start_str, exams):
    # Display each of the subject with its corresponding exam date
    print(f"College: {college_name}")
    print(f"Start Date: {start_str}\n")
    print("Exam Schedule:")
    print(f"{'Subject:':<30} Date:")
    print("-" * 41)

    for subject, gaps in exams:
        exam_date = get_exam_date(start_str, gaps)
        print(f"{subject:<30} {exam_date}")

    print("-" * 41)

print_schedule(start_date, exams)
