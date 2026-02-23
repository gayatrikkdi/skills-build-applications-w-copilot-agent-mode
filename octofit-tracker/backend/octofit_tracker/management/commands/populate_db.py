from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
 # Removed incorrect djongo import

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)
        Activity.objects.create(user=superman, type='swim', duration=60)
        Activity.objects.create(user=captain, type='walk', duration=20)

        # Create workouts
        Workout.objects.create(user=ironman, description='Chest workout', duration=40)
        Workout.objects.create(user=batman, description='Leg workout', duration=50)
        Workout.objects.create(user=superman, description='Cardio', duration=30)
        Workout.objects.create(user=captain, description='Yoga', duration=25)

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=80)
        Leaderboard.objects.create(user=captain, points=70)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
