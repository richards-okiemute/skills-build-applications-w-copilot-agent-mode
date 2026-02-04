from django.core.management.base import BaseCommand
from django.db import connection
from fitness.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel_members = ['spiderman', 'ironman', 'captainamerica']
        dc_members = ['batman', 'superman', 'wonderwoman']

        t1 = Team.objects.create(name='marvel', members=marvel_members)
        t2 = Team.objects.create(name='dc', members=dc_members)

        # Create users
        users = [
            ('spiderman', 'spiderman@marvel.com', 'marvel'),
            ('ironman', 'ironman@marvel.com', 'marvel'),
            ('captainamerica', 'captain@marvel.com', 'marvel'),
            ('batman', 'batman@dc.com', 'dc'),
            ('superman', 'superman@dc.com', 'dc'),
            ('wonderwoman', 'wonderwoman@dc.com', 'dc'),
        ]
        for username, email, team in users:
            User.objects.create(username=username, email=email, team=team)

        # Activities
        Activity.objects.create(user='spiderman', type='run', duration=30)
        Activity.objects.create(user='ironman', type='cycle', duration=45)
        Activity.objects.create(user='batman', type='gym', duration=60)

        # Leaderboard
        Leaderboard.objects.create(team='marvel', score=200)
        Leaderboard.objects.create(team='dc', score=180)

        # Workouts
        Workout.objects.create(user='spiderman', suggestion='Web-slinging sprints')
        Workout.objects.create(user='batman', suggestion='Gadget-assisted strength training')

        # Ensure unique index on email using pymongo if possible
        try:
            from pymongo import MongoClient
            client = MongoClient('mongodb://localhost:27017')
            db = client['octofit_db']
            users_coll = User._meta.db_table
            db[users_coll].create_index('email', unique=True)
            self.stdout.write(self.style.SUCCESS('Created unique index on users.email'))
        except Exception:
            self.stdout.write(self.style.WARNING('Could not create unique index via pymongo (maybe MongoDB not available).'))

        self.stdout.write(self.style.SUCCESS('Test data populated.'))
