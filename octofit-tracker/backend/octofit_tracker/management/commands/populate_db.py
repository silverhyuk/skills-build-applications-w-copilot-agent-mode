from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Team Beta", "members": [users[2]["_id"], users[3]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30, "date": "2025-05-15T08:00:00Z"},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 45, "date": "2025-05-15T09:00:00Z"},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "cycle", "duration": 60, "date": "2025-05-15T10:00:00Z"},
        ]
        db.activity.insert_many(activities)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
            {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
        ]
        db.workouts.insert_many(workouts)

        # Create leaderboard
        leaderboard = [
            {"_id": ObjectId(), "team": teams[0]["_id"], "points": 150},
            {"_id": ObjectId(), "team": teams[1]["_id"], "points": 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
