from django.db import models

# Create your models here.
class Movies(models.Model):
	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to='poster')
	description = models.TextField()
	language = models.CharField(max_length=20)
	director = models.CharField(max_length=30)
	release = models.DateField()
	rating = models.FloatField()

	def __str__(self):
		return self.name



class Series(models.Model):
	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to='poster')
	discription = models.TextField()
	rating = models.FloatField()
	# release = models.DateField()
	language = models.CharField(max_length=20)
	

	def __str__(self):
		return self.name



class Actor(models.Model):
	name = models.CharField(max_length=30)
	profile = models.ImageField(upload_to='profile')
	movie = models.ManyToManyField(Movies, blank=True)
	series = models.ManyToManyField(Series, blank=True)
	gender = models.CharField(max_length=10)
	dob = models.DateField()

	def __str__(self):
		return self.name




class Genre(models.Model):
	genre = models.CharField(max_length=100)
	g_movie = models.ManyToManyField(Movies, blank=True)
	g_series = models.ManyToManyField(Series,blank=True)

	def __str__(self):
		return self.genre




class Season(models.Model):
	name = models.CharField(max_length=50)
	s_series = models.ForeignKey(Series, on_delete = models.CASCADE)
	

	def __str__(self):
		return self.name


class Episode(models.Model):
	name = models.CharField(max_length = 50)
	length = models.TimeField()
	description = models.TextField()
	rating = models.FloatField()
	release = models.DateField()
	e_season = models.ForeignKey(Season, on_delete = models.CASCADE)

	def __str__(self):
		return self.name
