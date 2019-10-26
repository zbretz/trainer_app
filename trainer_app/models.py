from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Exercise(models.Model):
	name = models.CharField(max_length=128, unique=True)
	image = models.ImageField(null = True, upload_to='exercise_demos/')

	def __str__(self):
		return self.name

class Unit(models.Model):
	exercises = models.ManyToManyField(Exercise)

	def __str__(self):
		return str([str(exercise) for exercise in self.exercises.all()])

class Group(models.Model):
	group_name = models.CharField(max_length=128, default='sample')

class Workout(models.Model):
	units = models.ManyToManyField(Unit)
	workout_number = models.IntegerField(default=1)
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=128, unique=True)
	current_workout = models.ForeignKey(Workout, null=True, on_delete=models.CASCADE)
	#change from default to autonowadd=true
	last_workout_completed = models.DateTimeField(default = datetime.now().replace(year=2000))
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
#class Workout_Log(models.Model):
#	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
#	user = models.ForeignKey(User, on_delete=models.CASCADE)
#	workout_completed = models.BooleanField(default=True) #change to datefield


###############################
#class User(models.Model):
#	name = models.CharField(max_length=128, unique=True)

#class Exercise(models.Model):
#	exercise_type = models.CharField(max_length=128, unique=True)
#	name = models.CharField(max_length=128, unique=True)

#class Unit(models.Model):
#	unit_type = models.CharField(max_length=128, unique=True)
#	exercises = models.ManyToManyField(Exercise)

#class Workout(models.Model):
#	units = models.ManyToManyField(Unit)
#	users = models.ManyToManyField(User, through='Workout_Activity')

#class Workout_Activity
#	user = models.ForeignKey(User, on_delete=models.CASCADE)
#	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
#	completed = models.DateField(auto_now=True, null=True)