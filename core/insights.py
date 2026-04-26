from .streak import calculate_streak
from .models import Task


def get_insights(user):
    insights = []

    streak = calculate_streak(user)

    if streak >= 7:
        insights.append("🔥 Elite consistency!")
    elif streak >= 3:
        insights.append("💪 Good momentum.")
    else:
        insights.append("⚠️ Start a study streak today.")

    tasks = Task.objects.filter(user=user)

    if tasks.exists():
        done = tasks.filter(completed=True).count()
        rate = done / tasks.count()

        if rate < 0.5:
            insights.append("📌 Improve task completion rate.")

    return insights