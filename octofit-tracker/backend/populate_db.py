import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from fitness.models import User, Team, Activity, Leaderboard, Workout

def populate():
    # Create Users
    u1 = User.objects.create(username='alice', email='alice@example.com', team='Red')
    u2 = User.objects.create(username='bob', email='bob@example.com', team='Blue')
    u3 = User.objects.create(username='carol', email='carol@example.com', team='Red')

    # Create Teams
    t1 = Team.objects.create(name='Red', members=['alice', 'carol'])
    t2 = Team.objects.create(name='Blue', members=['bob'])

    # Create Activities
    Activity.objects.create(user='alice', type='run', duration=30)
    Activity.objects.create(user='bob', type='cycle', duration=45)
    Activity.objects.create(user='carol', type='swim', duration=20)

    # Create Leaderboard
    Leaderboard.objects.create(team='Red', score=50)
    Leaderboard.objects.create(team='Blue', score=40)

    # Create Workouts
    Workout.objects.create(user='alice', suggestion='Pushups and squats')
    Workout.objects.create(user='bob', suggestion='Cycling intervals')
    Workout.objects.create(user='carol', suggestion='Swimming laps')

    print('Test data populated.')

if __name__ == '__main__':
    populate()
