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
	data_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de entrada:") 
	data_fim = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de saída") 
	nomeQuartos = models.ManyToManyField(NomeQuarto, null=False, blank=False, verbose_name="Nome do quarto:")
	diaria = models.IntegerField(null=True, blank=True, verbose_name="Valor da diária")
	qtd_dias = models.IntegerField(null=True, blank=True, verbose_name="Quantidade de dias:")
	valor_reserva = models.FloatField(null=True, blank=True, verbose_name="valor da reserva:")
	valor_total = models.FloatField(null=True, blank=True, verbose_name="valor total:") 

	class Meta:
		db_table = 'ControleQuarto'
		app_label = 'suites'
		verbose_name = u'Controle do quarto'
		verbose_name_plural = u'Controle dos quartos'