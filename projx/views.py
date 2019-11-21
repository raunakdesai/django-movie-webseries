from django.shortcuts import render
from projx.forms import HomeForm
from projx.models import *
# Create your views here.


def home(request):
	movies=Movies
	series=Series
	
	if request.method=='POST':
		form = HomeForm(request.POST)
	
		if form.is_valid():
			look = form.cleaned_data['look']
			genre = form.cleaned_data['select_genre']
			year =  form.cleaned_data['select_year']
			language = form.cleaned_data['select_language']
			user_input = form.cleaned_data['user_input']
			print(len(look))
			
			if (len(look) == 0 or len(look) == 2):
				movies = Movies.objects.all().order_by('-release')
				movies = movies.filter(genre=genre) if genre else movies
				movies = movies.filter(language= language) if language else movies
				movies = movies.filter(release__year= year) if year else movies
				movies = movies.filter(name__startswith=user_input) or movies.filter(name__icontains=user_input) if user_input else movies
				
				#filter_for_series

				series = Series.objects.all().order_by('-rating')
				series = series.filter(genre=genre) if genre else series
				series = series.filter(language= language) if language else series
				series = series.filter(name__startswith=user_input) or series.filter(name__icontains=user_input) if user_input else series
			
			elif look[0] =="Movies":
				movies = Movies.objects.all()
				movies = movies.filter(genre=genre) if genre else movies
				movies = movies.filter(language= language) if language else movies
				movies = movies.filter(release__year= year) if year else movies
				movies = movies.filter(name__startswith=user_input) or movies.filter(name__icontains=user_input) if user_input else movies
				

			else:
				series = Series.objects.all()
				series = series.filter(genre=genre) if genre else series
				series = series.filter(language= language) if language else series
				series = series.filter(name__startswith=user_input) or series.filter(name__icontains=user_input) if user_input else Series
		return render(request,'home.html',{'form':form,'movies':movies, 'series':series})
	
	else:
		form = HomeForm()
		movies =  Movies.objects.all().order_by('-release')
		series =  Series.objects.all().order_by('-rating')
		return render(request,'home.html',{'form':form,'movies':movies,'series':series})
