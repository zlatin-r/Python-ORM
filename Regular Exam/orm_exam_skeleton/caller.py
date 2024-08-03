import os
import django
from django.db.models import Q, Count, F, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission


# Create queries within functions


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts:
        return ""

    result = [f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}"
              for a in astronauts]

    return "\n".join(result)


def get_top_astronaut():
    astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not astronaut or astronaut.count_missions == 0:
        return "No data."

    return f"Top Astronaut: {astronaut.name} with {astronaut.count_missions} missions."


def get_top_commander():
    astronaut = Astronaut.objects.annotate(count_missions=Count('commander')) \
        .order_by('-count_missions', 'phone_number') \
        .first()

    if not astronaut or astronaut.count_missions == 0:
        return "No data."

    return f"Top Commander: {astronaut.name} with {astronaut.count_missions} commanded missions."


def get_last_completed_mission():
    mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not mission:
        return 'No data.'

    commander_name = mission.commander.name if mission.commander else 'TBA'
    astronauts_names = ", ".join(a.name for a in mission.astronauts.all().order_by('name'))
    total_spacewalks = sum([a.spacewalks for a in mission.astronauts.all()])

    return (f"The last completed mission is: {mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronauts_names}. "
            f"Spacecraft: {mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    spacecraft = Spacecraft.objects \
        .annotate(count_missions=Count('missions')) \
        .order_by('-count_missions', 'name').first()

    if not spacecraft or spacecraft.count_missions == 0:
        return "No data."

    num_astronauts = Astronaut.objects.filter(missions__spacecraft=spacecraft).distinct().count()

    return (f"The most used spacecraft is: {spacecraft.name}, "
            f"manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.count_missions} missions, "
            f"astronauts on missions: {num_astronauts}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(missions__status=Mission.StatusChoices.PLANNED).distinct()
    spacecrafts_to_update = spacecrafts.filter(weight__gte=200)
    num_to_update = spacecrafts_to_update.count()

    if num_to_update == 0:
        return "No changes in weight."

    spacecrafts_to_update.update(weight=F('weight') - 200)

    avg_weight = Spacecraft.objects.all().aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {num_to_update} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
