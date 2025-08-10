# seed.py

import hashlib
from datetime import date, datetime

from sqlmodel import Session, create_engine

from app.core.settings import settings
from app.models.database import (
    Lessons,
    Posts,
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
                full_name="John Doe",
                email="john@example.com",
                password=hash_password("password123"),
                created_at=datetime.now()
            ),
            Users(
                full_name="Jane Smith",
                email="jane@example.com",
                password=hash_password("password123"),
                created_at=datetime.now()
            ),
            Users(
                full_name="Bob Johnson",
                email="bob@example.com",
                password=hash_password("password123"),
                created_at=datetime.now()
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
                updated_at=datetime.now()
            ),
            UserStats(
                user_id=users[1].id,
                total_xp=320,
                current_streak=5,
                best_streak=12,
                last_activity_date=date.today(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            ),
            UserStats(
                user_id=users[2].id,
                total_xp=75,
                current_streak=1,
                best_streak=3,
                last_activity_date=date.today(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            ),
        ]

        for stat in user_stats:
            db.add(stat)
        db.commit()

        # Create sample posts
        posts = [
            Posts(
                title="Getting Started with Python",
                content="Python is a great language for beginners. Here are some tips to get started...",
                user_id=users[0].id
            ),
            Posts(
                title="Advanced Data Structures",
                content="Let's explore some advanced data structures and their applications...",
                user_id=users[1].id
            ),
            Posts(
                title="Web Development Best Practices",
                content="Here are some best practices for modern web development...",
                user_id=users[2].id
            ),
        ]

        for post in posts:
            db.add(post)
        db.commit()

        # Create sample lessons
        lessons = [
            Lessons(
                title="Introduction to Python",
                description="Learn the basics of Python programming language",
                order=1,
                created_at=datetime.now()
            ),
            Lessons(
                title="Variables and Data Types",
                description="Understanding different data types in Python",
                order=2,
                created_at=datetime.now()
            ),
            Lessons(
                title="Control Flow",
                description="Learn about loops and conditional statements",
                order=3,
                created_at=datetime.now()
            ),
        ]

        for lesson in lessons:
            db.add(lesson)
        db.commit()

        # Create sample problems
        problems = [
            Problems(
                lesson_id=lessons[0].id,
                question="What is Python?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="A programming language",
                reward=10,
                order=1,
                created_at=datetime.now()
            ),
            Problems(
                lesson_id=lessons[0].id,
                question="Which of the following is NOT a Python data type?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="array",
                reward=15,
                order=2,
                created_at=datetime.now()
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What is the correct way to declare a variable in Python?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="x = 5",
                reward=10,
                order=1,
                created_at=datetime.now()
            ),
            Problems(
                lesson_id=lessons[1].id,
                question="What type is the value 3.14?",
                type=ProblemType.MULTIPLE_CHOICE,
                answer="float",
                reward=10,
                order=2,
                created_at=datetime.now()
            ),
            Problems(
                lesson_id=lessons[2].id,
                question="What is the output of: print(2 + 2)?",
                type=ProblemType.INPUT,
                answer="4",
                reward=5,
                order=1,
                created_at=datetime.now()
            ),
        ]

        for problem in problems:
            db.add(problem)
        db.commit()

        # Create problem choices for multiple choice questions
        problem_choices = [
            # Problem 1 choices
            ProblemChoices(problem_id=problems[0].id, answer="A programming language", order=1),
            ProblemChoices(problem_id=problems[0].id, answer="A snake", order=2),
            ProblemChoices(problem_id=problems[0].id, answer="A database", order=3),
            ProblemChoices(problem_id=problems[0].id, answer="An operating system", order=4),

            # Problem 2 choices
            ProblemChoices(problem_id=problems[1].id, answer="list", order=1),
            ProblemChoices(problem_id=problems[1].id, answer="dict", order=2),
            ProblemChoices(problem_id=problems[1].id, answer="array", order=3),
            ProblemChoices(problem_id=problems[1].id, answer="tuple", order=4),

            # Problem 3 choices
            ProblemChoices(problem_id=problems[2].id, answer="var x = 5", order=1),
            ProblemChoices(problem_id=problems[2].id, answer="x = 5", order=2),
            ProblemChoices(problem_id=problems[2].id, answer="let x = 5", order=3),
            ProblemChoices(problem_id=problems[2].id, answer="const x = 5", order=4),

            # Problem 4 choices
            ProblemChoices(problem_id=problems[3].id, answer="int", order=1),
            ProblemChoices(problem_id=problems[3].id, answer="float", order=2),
            ProblemChoices(problem_id=problems[3].id, answer="double", order=3),
            ProblemChoices(problem_id=problems[3].id, answer="decimal", order=4),
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
                total_problems=2,
                is_completed=True,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            ),
            UserProgress(
                user_id=users[0].id,
                lesson_id=lessons[1].id,
                completed_problems=1,
                total_problems=2,
                is_completed=False,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now()
            ),
            UserProgress(
                user_id=users[1].id,
                lesson_id=lessons[0].id,
                completed_problems=2,
                total_problems=2,
                is_completed=True,
                last_activity_at=datetime.now(),
                created_at=datetime.now(),
                updated_at=datetime.now()
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
                answers={"1": "A programming language", "2": "array"},
                correct_count=2,
                earned_xp=25,
                created_at=datetime.now()
            ),
            Submissions(
                user_id=users[1].id,
                lesson_id=lessons[0].id,
                answers={"1": "A programming language", "2": "array"},
                correct_count=2,
                earned_xp=25,
                created_at=datetime.now()
            ),
        ]

        for submission in submissions:
            db.add(submission)
        db.commit()

        print("✅ Data seeded successfully!")
        print(f"📊 Created {len(users)} users")
        print(f"📝 Created {len(posts)} posts")
        print(f"📚 Created {len(lessons)} lessons")
        print(f"❓ Created {len(problems)} problems")
        print(f"📈 Created {len(user_stats)} user stats")
        print(f"📊 Created {len(user_progress)} user progress records")
        print(f"📋 Created {len(submissions)} submissions")


if __name__ == "__main__":
    seed_data()
