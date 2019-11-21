from django import forms
from django.forms import ModelForm
from projx.models import *
import datetime
from django.db.models.functions import ExtractYear  


class HomeForm(forms.Form):
	choices = {
		('movies','Movies'),
		('series','Series'),
	}
	language = Movies.objects.values_list('language', flat=True).distinct()
	lang_choices = [('', '-------')] + [(id, id) for id in language]

	language = Series.objects.values_list('language', flat=True).distinct()
	lang_choices = [('', '-------')] + [(id, id) for id in language]

	myear = Movies.objects.annotate(year=ExtractYear('release')).values_list('year',flat=True).distinct()
	year_choices = [('', "-------")] + [(id, id) for id in myear]
	# syear =	Series.objects.annotate(year=ExtractYear('release')).values_list('year',flat=True).distinct()
	# year_choices = year_choices + [(id, id) for id in syear]
    
	
	look = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices,required=False)
	select_genre = forms.ModelChoiceField(queryset=Genre.objects.all(),empty_label='-------',required=False)
	select_year = forms.CharField(max_length=100, widget=forms.Select(choices= year_choices),required=False)
	select_language = forms.CharField(max_length=100, widget=forms.Select(choices= lang_choices), required=False)
	user_input = forms.CharField(max_length = 100,min_length=3,required=False, widget = forms.TextInput(attrs= {'placeholder':'Search','class':'input','id':'input'}))

	look.widget.attrs.update({'display':'inline-block','text-decoration': 'none',})
	select_genre.widget.attrs.update({'class':'select'})
	select_year.widget.attrs.update({'class':'select'})
	select_language.widget.attrs.update({'class':'select'})
		
