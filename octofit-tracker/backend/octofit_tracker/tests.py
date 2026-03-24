from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com')
        team = Team.objects.create(name='Team1')
        team.members.add(user)
        self.assertEqual(team.name, 'Team1')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='active', email='active@example.com')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, calories=200, date='2023-01-01')
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio session', difficulty='Easy', duration=20)
        self.assertEqual(workout.name, 'Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(username='leader', email='leader@example.com')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
