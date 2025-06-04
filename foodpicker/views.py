import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Food
from moods.models import Mood  # ✅ needed for mood-based food picking

def home(request):
    if request.method == "POST":
        name = request.POST.get("food")
        emoji = request.POST.get("emoji", "")
        mood_id = request.POST.get("mood")  # 👈 get selected mood
        mood = Mood.objects.filter(id=mood_id).first() if mood_id else None

        if name:
            Food.objects.create(name=name, emoji=emoji, mood=mood)  # 👈 save with mood
        return redirect('food_home')

    foods = list(Food.objects.all())
    moods = Mood.objects.all()  # 👈 get all moods

    if foods:
        selected = random.choice(foods)
        food_name = selected.name
        food_emoji = selected.emoji
    else:
        food_name = "No food available"
        food_emoji = "❓"

    return render(request, "foodpicker/home.html", {
        "foods": foods,
        "food": food_name,
        "emoji": food_emoji,
        "moods": moods,  # 👈 send moods to template
    })
def home_by_mood(request, mood_id):
    try:
        mood = Mood.objects.get(id=mood_id)
        foods = list(Food.objects.filter(mood=mood))
    except Mood.DoesNotExist:
        mood = None
        foods = []

    moods = Mood.objects.all()  # Add this for form dropdown

    if foods:
        selected = random.choice(foods)
        food_name = selected.name
        food_emoji = selected.emoji
    else:
        food_name = "No food for this mood"
        food_emoji = "😐"

    return render(request, "foodpicker/home.html", {
        "foods": foods,
        "food": food_name,
        "emoji": food_emoji,
        "mood": mood,
        "moods": moods,  # pass moods here
    })



from django.http import JsonResponse
from .models import Food
from moods.models import Mood

def random_food(request):
    mood_id = request.GET.get("mood")
    if mood_id:
        foods = list(Food.objects.filter(mood_id=mood_id))
    else:
        foods = list(Food.objects.all())

    if foods:
        selected = random.choice(foods)
        return JsonResponse({"name": selected.name, "emoji": selected.emoji})
    else:
        return JsonResponse({"name": "Nothing", "emoji": "❌"})




