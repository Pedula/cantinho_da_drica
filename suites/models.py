#-*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.
class NomeQuarto(models.Model):
	nome = models.CharField(unique=True, max_length=30, null=False, blank=False, verbose_name="Nome do quarto:")

	def __unicode__(self):
		return self.nome

	class Meta:
		db_table = 'NomeQuarto'
		app_label = 'suites'
		verbose_name = u'nome do quarto'
		verbose_name_plural = u'nome dos quartos'

class ControleQuarto(models.Model):
	data_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de entrada:") 
	data_fim = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de saída") 
	nomeQuartos = models.ManyToManyField(NomeQuarto, null=False, blank=False, verbose_name="Nome do quarto:")
	nomeHospede = models.ManyToManyField("Hospede", null=False, blank=False, verbose_name="Nome do Hospede:")
	diaria = models.IntegerField(null=True, blank=True, verbose_name="Valor da diária")
	qtd_dias = models.FloatField(null=True, blank=True, verbose_name="Quantidade de dias:")
	valor_total = models.FloatField(null=True, blank=True, verbose_name="valor total:") 
	valor_reserva = models.FloatField(null=True, blank=True, verbose_name="valor da reserva:")



	def __unicode__(self):
		if self.data_inicio:
			return timezone.localtime(self.data_inicio).strftime("%d/%m/%Y %H:%M")
		else:
			return "--"


	class Meta:
		db_table = 'ControleQuarto'
		app_label = 'suites'
		verbose_name = u'Controle do quarto'
		verbose_name_plural = u'Controle dos quartos'

class Hospede(models.Model):
	nome = models.CharField(unique=True,max_length=100, null=False, blank=False, verbose_name="Nome do cliente:")

	def __unicode__(self):
		return self.nome

	class Meta:
		db_table = 'hospede'
		app_label = 'suites'
		verbose_name = u'Hospede'
		verbose_name_plural = u'Hospedes'