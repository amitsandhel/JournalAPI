from django.db import models

# Create your models here.

class JMIR(models.Model):
	reference_count = models.IntegerField("Reference Count", blank=True, null=True)
	publisher = models.CharField("publisher", max_length=200, default='')
	issuex = models.IntegerField("issue", blank=True, null=True)
	short_container_title = models.CharField('Short Container title', max_length=200, default='')
	DOI = models.CharField('DOI', max_length=150, default='')
	article_type = models.CharField('Type', max_length=100, default='')
	page = models.CharField('Page', max_length=150, default='')
	source = models.CharField('Source', max_length=100, default='')
	title = models.CharField('Title', max_length=500, default='')
	prefix = models.DecimalField('Prefix', max_digits=9, decimal_places=4, blank=True, null=True)
	volume = models.IntegerField('volume', blank=True, null=True )
	member = models.IntegerField('member', blank=True, null=True)
	container_title = models.CharField('Container Title', max_length=300, default='')
	language = models.CharField('language', max_length=5, default='')
	score = models.DecimalField('Score', max_digits=4, decimal_places=1, blank=True, null=True)
	issn = models.CharField('issn', max_length=50, default='')
	url = models.CharField('url', max_length=200, default='')
	
	def __str__(self):
		return self.DOI
