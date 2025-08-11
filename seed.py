# seed.py

import hashlib
from datetime import date, datetime

from sqlmodel import Session, create_engine

from app.core.settings import settings
from app.models.database import (
    Lessons,
    ProblemChoices,
    Problems,
    ProblemType,
    Submissions,
    UserProgress,
    Users,
    UserStats,
)


def hash_password(password: str) -> str:
    """Simple password hashing for demo purposes"""
    return hashlib.sha256(password.encode()).hexdigest()


def seed_data():
    engine = create_engine(settings.DB_CONNECTION_STR)

    with Session(engine) as db:
        # Create sample users
        users = [
            Users(
                full_name="Crystal Wijaya",
                email="crystal@example.com",
                password=hash_password("password123"),
                created_at=datetime.now(),
            ),
            Users(
                full_name="Rizky Sunaryo",
                email="rizky@example.com",
                password=hash_password("password123"),
                created_at=datetime.now(),
            ),
            Users(
                full_name="Susi Susanti",
                email="susi@example.com",
                password=hash_password("password123"),
                created_at=datetime.now(),
            ),
        ]

        for user in users:
            db.add(user)
        db.commit()

        # Create user stats for each user
        user_stats = [
            UserStats(
                user_id=users[0].id,
                total_xp=150,
                current_streak=3,
                best_streak=7,
                last_activity_date=date.today(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            UserStats(
                user_id=users[1].id,
                total_xp=320,
                current_streak=5,
                best_streak=12,
                last_activity_date=date.today(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            UserStats(
                user_id=users[2].id,
                total_xp=75,
                current_streak=1,
                best_streak=3,
                last_activity_date=date.today(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
        ]

        for stat in user_stats:
            db.add(stat)
        db.commit()

        # Create sample lessons
        lessons = [
            Lessons(
                title="Basic Arithmetic",
                description="Master addition and subtraction with fun problems",
                order=1,
                created_at=datetime.now(),
            ),
            Lessons(
                title="Multiplication Mastery",
                description="Learn your times tables through interactive practice",
                order=2,
                created_at=datetime.now(),
            ),
            Lessons(
                title="Division Basics",
                description="Understand division with simple problems",
                order=3,
                created_at=datetime.now(),
            ),
        ]

        for lesson in lessons:
            db.add(lesson)
        db.commit()

        # Create sample problems
        problems = [
            Problems(
                lesson_id=lessons[0].id,
                question="What is 15 + 7?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="22",
                reward=10,
                order=1,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[0].id,
                question="What is 25 - 8?",
                type=ProblemType.INPUT,
                answer="17",
                reward=10,
                order=2,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[0].id,
                question="What is 12 + 19?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="31",
                reward=10,
                order=3,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[0].id,
                question="What is 40 - 15?",
                type=ProblemType.INPUT,
                answer="25",
                reward=10,
                order=4,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What is 6 × 7?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="42",
                reward=15,
                order=1,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What is 8 × 9?",
                type=ProblemType.INPUT,
                answer="72",
                reward=15,
                order=2,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What is 5 × 6?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="30",
                reward=15,
                order=3,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What is 4 × 8?",
                type=ProblemType.INPUT,
                answer="32",
                reward=15,
                order=4,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[2].id,
                question="What is 24 ÷ 6?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="4",
                reward=20,
                order=1,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[2].id,
                question="What is 35 ÷ 7?",
                type=ProblemType.INPUT,
                answer="5",
                reward=20,
                order=2,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[2].id,
                question="What is 18 ÷ 3?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="6",
                reward=20,
                order=3,
                created_at=datetime.now(),
            ),
            Problems(
                lesson_id=lessons[2].id,
                question="What is 28 ÷ 4?",
                type=ProblemType.INPUT,
                answer="7",
                reward=20,
                order=4,
                created_at=datetime.now(),
            ),
        ]

        for problem in problems:
            db.add(problem)
        db.commit()

        # Create problem choices for multiple choice questions
        problem_choices = [
            # Problem 1 choices (What is 15 + 7?)
            ProblemChoices(
                problem_id=problems[0].id,
                answer="20",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[0].id,
                answer="21",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[0].id,
                answer="22",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[0].id,
                answer="23",
                order=4,
            ),
            # Problem 3 choices (What is 12 + 19?)
            ProblemChoices(
                problem_id=problems[2].id,
                answer="29",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[2].id,
                answer="30",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[2].id,
                answer="31",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[2].id,
                answer="32",
                order=4,
            ),
            # Problem 5 choices (What is 6 × 7?)
            ProblemChoices(
                problem_id=problems[4].id,
                answer="40",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[4].id,
                answer="41",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[4].id,
                answer="42",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[4].id,
                answer="43",
                order=4,
            ),
            # Problem 7 choices (What is 5 × 6?)
            ProblemChoices(
                problem_id=problems[6].id,
                answer="28",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[6].id,
                answer="29",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[6].id,
                answer="30",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[6].id,
                answer="31",
                order=4,
            ),
            # Problem 9 choices (What is 24 ÷ 6?)
            ProblemChoices(
                problem_id=problems[8].id,
                answer="3",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[8].id,
                answer="4",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[8].id,
                answer="5",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[8].id,
                answer="6",
                order=4,
            ),
            # Problem 11 choices (What is 18 ÷ 3?)
            ProblemChoices(
                problem_id=problems[10].id,
                answer="5",
                order=1,
            ),
            ProblemChoices(
                problem_id=problems[10].id,
                answer="6",
                order=2,
            ),
            ProblemChoices(
                problem_id=problems[10].id,
                answer="7",
                order=3,
            ),
            ProblemChoices(
                problem_id=problems[10].id,
                answer="8",
                order=4,
            ),
        ]

        for choice in problem_choices:
            db.add(choice)
        db.commit()

        # Create sample user progress
        user_progress = [
            UserProgress(
                user_id=users[0].id,
                lesson_id=lessons[0].id,
                completed_problems=2,
                total_problems=4,
                is_completed=False,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            UserProgress(
                user_id=users[0].id,
                lesson_id=lessons[1].id,
                completed_problems=0,
                total_problems=4,
                is_completed=False,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
            UserProgress(
                user_id=users[1].id,
                lesson_id=lessons[0].id,
                completed_problems=4,
                total_problems=4,
                is_completed=True,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            ),
        ]

        for progress in user_progress:
            db.add(progress)
        db.commit()

        # Create sample submissions
        submissions = [
            Submissions(
                user_id=users[0].id,
                lesson_id=lessons[0].id,
                answers={"1": "22", "2": "17", "3": "31"},
                correct_count=3,
                earned_xp=30,
                created_at=datetime.now(),
            ),
            Submissions(
                user_id=users[1].id,
                lesson_id=lessons[0].id,
                answers={"1": "22", "2": "17", "3": "31", "4": "25"},
                correct_count=4,
                earned_xp=40,
                created_at=datetime.now(),
            ),
        ]

        for submission in submissions:
            db.add(submission)
        db.commit()

        print("✅ Data seeded successfully!")
        print(f"📊 Created {len(users)} users")
        print(f"📚 Created {len(lessons)} lessons")
        print(f"❓ Created {len(problems)} problems")
        print(f"📈 Created {len(user_stats)} user stats")
        print(f"📊 Created {len(user_progress)} user progress records")
        print(f"📋 Created {len(submissions)} submissions")


if __name__ == "__main__":
    seed_data()
