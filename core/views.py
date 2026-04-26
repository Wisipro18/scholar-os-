from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
import calendar

from .models import Task, StudySession, StudyEvent


# =========================
# DASHBOARD
# =========================
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    study_data = {
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "hours": [2, 3, 1, 4, 2, 5, 3]
    }

    return render(request, "dashboard.html", {
        "tasks": tasks,
        "streak": calculate_streak(request.user),
        "insights": "You're improving steadily 🚀",
        "study_data": study_data
    })


# =========================
# CGPA
# =========================
@login_required
def cgpa_view(request):
    if request.method == "POST":
        grades = request.POST.getlist("grade")
        units = request.POST.getlist("units")

        grade_map = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}

        total_points = 0
        total_units = 0

        for g, u in zip(grades, units):
            if g in grade_map and u:
                total_points += grade_map[g] * int(u)
                total_units += int(u)

        cgpa = total_points / total_units if total_units > 0 else 0

        return render(request, "cgpa.html", {
            "cgpa": round(cgpa, 2)
        })

    return render(request, "cgpa.html")


# =========================
# CALENDAR
# =========================
@login_required
def calendar_view(request):
    today = date.today()

    month = int(request.GET.get("month", today.month))
    year = int(request.GET.get("year", today.year))

    cal = calendar.Calendar()
    month_days = list(cal.itermonthdays(year, month))

    events = StudyEvent.objects.filter(date__year=year, date__month=month)

    event_map = {}
    for event in events:
        event_map.setdefault(event.date.day, []).append(event.title)

    return render(request, "calendar.html", {
        "month_days": month_days,
        "month": month,
        "year": year,
        "event_map": event_map,
        "month_name": calendar.month_name[month],
    })


# =========================
# ADD EVENT
# =========================
@login_required
def add_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date_value = request.POST.get("date")

        if title and date_value:
            StudyEvent.objects.create(
                title=title,
                date=date_value
            )

    return redirect("/calendar/")


# =========================
# POMODORO
# =========================
@login_required
def pomodoro_view(request):
    return render(request, "pomodoro.html")


# =========================
# STREAK
# =========================
def calculate_streak(user):
    sessions = StudySession.objects.filter(user=user).order_by('-date')

    if not sessions:
        return 0

    streak = 1
    previous_date = sessions[0].date

    for session in sessions[1:]:
        if (previous_date - session.date).days == 1:
            streak += 1
            previous_date = session.date
        else:
            break

    return streak