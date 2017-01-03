#-*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class NomeQuarto(models.Model):
	nome = models.CharField(unique=True, max_length=30, null=False, blank=False)

	def __unicode__(self):
		return self.nome

	class Meta:
		db_table = 'NomeQuarto'
		app_label = 'suites'
		verbose_name = u'nome do quarto'
		verbose_name_plural = u'nome dos quartos'

class ControleQuarto(models.Model):
	data_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True) 
	data_fim = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True) 
	nomeQuartos = models.ManyToManyField(NomeQuarto, null=True, blank=True)

	class Meta:
		db_table = 'ControleQuarto'
		app_label = 'suites'
		verbose_name = u'Controle do quarto'
		verbose_name_plural = u'Controle dos quartos'