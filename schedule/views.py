from datetime import datetime, time, timedelta

from django.contrib.auth import get_user
from django.shortcuts import redirect, render

from .models import Schedule, TypeOfCut


def home_view(request):
    return render(request, "home.html")


def schedule_view(request):
    date_now = datetime.now().date()  # Dia atual
    date_required = date_now + timedelta(days=1)  # Próximo dia

    # Horários já agendados
    schedules_hours = Schedule.objects.filter(date_hour__date=date_required)

    # Horários disponíveis
    available_hour = []
    for hour in range(8, 20):
        available = time(hour, 0, 0)
        available_hour.append(datetime.combine(date_required, available))

    # Removendo os horários já agendados
    for schedule in schedules_hours:
        not_available = schedule.date_hour.time()
        if not_available in available_hour:
            available_hour.remove(not_available)

    type_of_cut = TypeOfCut.objects.all().order_by("type_cut")

    if request.method == "POST":
        date = request.POST["appointmentDate"]
        hour = request.POST["appointmentTime"]
        type_service = request.POST["serviceType"]
        # obs = request.POST["additionalNotes"]
        date_hour_str = f"{date} {hour}"
        date_hour = datetime.strptime(date_hour_str, "%Y-%m-%d %H:%M")

        new_schedule = Schedule(
            date_hour=date_hour,
            type_of_cut=TypeOfCut.objects.all().filter(type_cut=type_service).first(),
            user=get_user(request),
        )
        new_schedule.save()
        return redirect("home")
    else:
        ...

    return render(
        request,
        "schedule.html",
        {
            "available_hour": available_hour,
            "type_of_cut": type_of_cut,
        },  # Noqa: E501
    )
