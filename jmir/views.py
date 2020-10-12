from django.shortcuts import render

import requests
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from rest_framework import routers, serializers, viewsets
from .serializers import JMIRSerializer

#import models
from jmir.models import JMIR

#to show messages
from django.contrib import messages

# Create your views here.

#https://academicguides.waldenu.edu/library/doi
#https://search.crossref.org/?q=10.2196%2F12121&from_ui=yes
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821292/
#https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821292/

#https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
#https://www.django-rest-framework.org/


class JMIRViewSet(viewsets.ModelViewSet):
    queryset = JMIR.objects.all()#.order_by('name')
    serializer_class = JMIRSerializer

class JMIRCrossRef(TemplateView):
	def __init__(self):
		self.template_name = "jmir/crossref.html"

	def post(self, request, *args, **kwargs):
		''' get functoin to save and get data to display in table'''
		print ('post ran')
		context={}
		table_list = []
		#loop to get rid of the system messages so it can solve the problem
		system_messages = messages.get_messages(request)
		for message in system_messages:
			# This iteration is necessary to clear messages
			pass
		system_messages.used = True


		doi_url= request.POST['file']
		print (doi_url)
		#todo check if any of this doi is in the database
		if JMIR.objects.filter(DOI=doi_url).exists():
			print ('yes')
			val = JMIR.objects.filter(DOI=doi_url)
			table_list.append(list(val.values_list()))
			messages.success(request, 'table successfully loaded pre-existing data')
		else:
			print ('no not in url')
			#run the request to get the data
			url  = "https://api.crossref.org/works/" + doi_url
			response = requests.get(url)
			print ('ans ', response, response.status_code)
			#we have a valid doi and a valid url with valid data
			if response.status_code == 200:
				ans = response.json()
				print('creating db')
				#create or update the db 
				_, created = JMIR.objects.update_or_create(
						reference_count = ans['message']['reference-count'],
						publisher = ans['message']['publisher'],
						issuex = ans['message']['issue'],
						short_container_title = ans['message']['short-container-title'],
						DOI = ans['message']['DOI'],
						article_type = ans['message']['type'],
						page = ans['message']['page'],
						source = ans['message']['source'],
						title = ans['message']['title'][0],
						prefix = ans['message']['prefix'],
						volume = ans['message']['volume'],
						member = ans['message']['member'],
						container_title = ans['message']['container-title'][0],
						language = ans['message']['language'],
						score = ans['message']['score'],
						issn = ans['message']['ISSN'][0],
						url = ans['message']['URL'],
						defaults={
								}
				)
				table_list.append([( ans['message']['reference-count'], ans['message']['publisher'], ans['message']['issue'],
							ans['message']['short-container-title'], ans['message']['DOI'], ans['message']['type'],
							ans['message']['page'], ans['message']['source'], ans['message']['title'][0], 
							ans['message']['prefix'], ans['message']['volume'], ans['message']['member'],
							ans['message']['container-title'][0], ans['message']['language'], ans['message']['score'],
							ans['message']['ISSN'][0], ans['message']['URL'] )])
				messages.success(request, 'successful api saved and loaded ')
			else:
				messages.error(request, 'This DOI does not exist in the crossref api please enter correct doi')

		context.update({'table_list': table_list})


		return render(request, self.template_name, context )


def ncbi(request):
	# pubmed protein nuccore ipg nucleotide structure sparcle genome annotinfo assembly bioproject biosample blastdbinfo books cdd clinvar gap gapplus grasp dbvar gene gds geoprofiles homologene medgen mesh ncbisearch nlmcatalog omim orgtrack pmc popset proteinclusters pcassay biosystems pccompound pcsubstance seqannot snp sra taxonomy biocollections gtr 
	# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi? db=nucleotide&id=1509580163, 1509580026, 1509580024, 1509580022&rettype=fasta&retmode=text.
	#url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=none&id=31115346'
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?db=genome&id=31115346'
	#response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/")
	response = requests.get(url) #get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/31115346")	   
	print ('testing')
	return HttpResponse(response.text)
	#return JsonResponse(response.json())



class AboutView(TemplateView):
	template_name='jmir/about.html'