from datetime import date
from .models import StudySession


def calculate_streak(user):
    sessions = StudySession.objects.filter(user=user).order_by('-date')

    if not sessions:
        return 0

    streak = 1
    today = date.today()

    for i in range(1, len(sessions)):
        if (sessions[i-1].date - sessions[i].date).days == 1:
            streak += 1
        else:
            break

    return streak