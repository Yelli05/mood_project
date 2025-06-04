from django.shortcuts import render, redirect
from foodpicker.models import Food
from moods.models import Mood
import random

def mood_home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        emoji = request.POST.get("emoji", "")

        if name:
            Mood.objects.create(name=name, emoji=emoji)
        return redirect('mood_home')  # Stay on the same page after adding mood

    mood_id = request.GET.get("mood")
    if mood_id:
        foods = list(Food.objects.filter(mood_id=mood_id))
    else:
        foods = list(Food.objects.all())

    moods = Mood.objects.all()

    if foods:
        selected = random.choice(foods)
        food_name = selected.name
        food_emoji = selected.emoji
    else:
        food_name = "No food available"
        food_emoji = "❓"

    return render(request, "moods/home.html", {
        "foods": foods,
        "food": food_name,
        "emoji": food_emoji,
        "moods": moods,
    })
