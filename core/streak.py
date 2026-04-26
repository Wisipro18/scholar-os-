from datetime import date, timedelta
from .models import StudySession


def calculate_streak(user):
    sessions = StudySession.objects.filter(user=user).order_by('-study_date')

    if not sessions:
        return 0

    streak = 1
    current = sessions[0].study_date

    today = date.today()

    if current != today and current != today - timedelta(days=1):
        return 0

    for s in sessions[1:]:
        if s.study_date == current - timedelta(days=1):
            streak += 1
            current = s.study_date
        else:
            break

    return streak