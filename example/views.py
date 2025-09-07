import pandas as pd
from django.shortcuts import render
from datetime import datetime

def load_data():
    try:
        df = pd.read_csv("workouts.csv")
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        return df
    except Exception:
        return pd.DataFrame(columns=["Fecha", "Ejercicio", "Series", "Repeticiones", "Peso"])

def index(request):
    return render(request, "app_workouts/index.html")

def years(request):
    df = load_data()
    years = sorted(df["Fecha"].dt.year.unique())
    return render(request, "app_workouts/years.html", {"years": years})

def months(request, year):
    df = load_data()
    months = sorted(df[df["Fecha"].dt.year == year]["Fecha"].dt.month.unique())
    return render(request, "app_workouts/months.html", {"year": year, "months": months})

def days(request, year, month):
    df = load_data()
    mask = (df["Fecha"].dt.year == year) & (df["Fecha"].dt.month == month)
    days = sorted(df[mask]["Fecha"].dt.day.unique())
    return render(request, "app_workouts/days.html", {"year": year, "month": month, "days": days})

def workout_detail(request, year, month, day):
    df = load_data()
    mask = (
        (df["Fecha"].dt.year == year)
        & (df["Fecha"].dt.month == month)
        & (df["Fecha"].dt.day == day)
    )
    workout = df[mask].to_dict(orient="records")
    return render(request, "app_workouts/workout_detail.html", {
        "year": year,
        "month": month,
        "day": day,
        "workout": workout
    })
