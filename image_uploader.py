import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','trainer_project.settings')

import django
django.setup()

from trainer_app.models import *

def load_media():
	for file in os.listdir():
		exercise_name = file.split('.')[0]
		try:
			exercise = Exercise.objects.get(name=exercise_name)
			exercise.image = 'exercise_demos/{0}'.format(file)
			exercise.save()
			print('success: ' + exercise_name)
		except Exception as e:
			print(exercise_name)
			print(e)

def read_dir():
	path = os.path.dirname(os.path.abspath(__file__))
	new_path = os.path.join(path, "media/exercise_demos")
	print(os.listdir(new_path))


if __name__ == "__main__":
	#load_media()
	read_dir()