from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Trainer(models.Model):
    trainer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.trainer.username

class Celebrity_Video(models.Model):
	trainer = models.CharField(max_length=128, null=True)
	#trainer = models.ForeignKey(Trainer, null=True, on_delete = models.SET_NULL)
	vid_name = models.CharField(max_length=128, unique=True)
	image = models.ImageField(null = True, upload_to='exercise_demos/instagram/')
	thumbnail = models.ImageField(null = True, upload_to='exercise_demos/instagram/posters/')

	def save(self, *args, **kwargs):
		self.thumbnail = 'exercise_demos/instagram/posters/{0}poster.png'.format(self.vid_name)
		self.image = 'exercise_demos/instagram/{0}.mp4'.format(self.vid_name)
		super(Celebrity_Video, self).save(*args, **kwargs)

	def __str__(self):
		return self.vid_name

def exercise_image_path(instance, filename):
	return 'exercise_demos/{0}'.format(filename)

class Exercise(models.Model):
	name = models.CharField(max_length=128, unique=True)
	#image = models.ImageField(null = True, upload_to='exercise_demos/{0}'.format(name))
	#image = models.ImageField(null = True, upload_to=exercise_image_path)
	#image = models.ImageField(null = True, upload_to='exercise_demos/{0}'.format(name), default='exercise_demos/pushup.jpeg')
	image = models.ImageField(null = True, upload_to='exercise_demos/')

	def save(self, *args, **kwargs):
		self.image = 'exercise_demos/{0}.mp4'.format(self.name)
		super(Exercise, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Unit(models.Model):
	exercises = models.ManyToManyField(Exercise)
	times_to_repeat = models.IntegerField(default=1)

	def __str__(self):
		return str([str(exercise) for exercise in self.exercises.all()])

class Rep_Scheme(models.Model):
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	reps = models.CharField(max_length = 32, null=True)

default_description = "This part will occupy 12 columns on a small screen, 8 on a medium screen, and 9 on a large screen. This part will occupy 12 columns on a small screen, 8 on a medium screen, and 9 on a large screen."
class Group(models.Model):
	group_name = models.CharField(max_length=128, default='sample')
	description = models.CharField(max_length=256, null=True, default=default_description)
	trainer = models.ForeignKey(Trainer, null=True, on_delete = models.SET_NULL)#, default= 1)
	
	def __str__(self):
		return self.group_name

class Workout(models.Model):
	units = models.ManyToManyField(Unit)
	workout_number = models.IntegerField(default=1)
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

#combine with userprofile? 
class WorkoutLog(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	#group is redundant since it's in workout
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
	workout = models.ForeignKey(Workout, null=True, on_delete=models.CASCADE)
	date_performed = models.DateTimeField(null=True)
	
	#def __str__(self):
	#	return self.group.group_name + ' ' + str(self.workout.workout_number) + ' ' + self.date_performed

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=128, unique=True)

	current_workout = models.ForeignKey(Workout, null=True, on_delete=models.CASCADE)
	#change from default to autonowadd=true
	last_workout_completed = models.DateTimeField(default = datetime.now().replace(year=2000))
	group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
	trainer = models.ForeignKey(Trainer, null=True, on_delete = models.SET_NULL)#, default= 1)

	def __str__(self):
		return self.user.username


class CircuitComplete(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
	unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
	date_time = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return "unit :" + self.unit + ", date/time: " + self.date_time


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