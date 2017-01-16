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
		ordering = ['nome']

class ControleQuarto(models.Model):
	NEGOCIANDO = 1
	FECHADO = 2
	RESERVADO = 3
	CANCELADO = 4

	STATUS_QUARTO = (
		(NEGOCIANDO, u'Negociando'),
		(RESERVADO, u'Reservado'),
		(FECHADO, u'Fechado'),
		(CANCELADO, u'Cancelado'),
	)

	IVO = 1
	SANDRA = 2
	RENATO = 3
	RENAN = 4
	VIVIANE = 5
	GARNIZE = 6
	OUTROS = 7

	VENDEDOR = (
		(GARNIZE, u'Garnize'),
		(RENATO, u'Renato'),
		(IVO, u'Ivo'),
		(SANDRA, u'Sandra'),
		(RENAN, u'Renan'),
		(VIVIANE, u'Viviane'),
		(OUTROS, u'Outros'),
	)

	data_inicio = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de entrada:") 
	data_fim = models.DateTimeField(auto_now_add=False, auto_now=False, null=False, blank=False, verbose_name="Data de saída") 
	nomeQuartos = models.ManyToManyField(NomeQuarto, null=False, blank=False, verbose_name="Nome do quarto:")
	nomeHospede = models.ManyToManyField("Hospede", null=False, blank=False, verbose_name="Nome do Hospede:")
	status = models.PositiveSmallIntegerField(choices=STATUS_QUARTO, null=False, blank=False, default=NEGOCIANDO)
	vendedor = models.PositiveSmallIntegerField(choices=VENDEDOR, null=False, blank=False, default=IVO)
	diaria = models.IntegerField(null=True, blank=True, verbose_name="Valor da diária")
	qtd_dias = models.FloatField(null=True, blank=True, verbose_name="Quantidade de dias:")
	valor_total = models.FloatField(null=True, blank=True, verbose_name="valor total:") 
	valor_reserva = models.FloatField(null=True, blank=True, verbose_name="valor da reserva:")
	observacao = models.TextField(null=True, blank=True, verbose_name="Observação")




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
		ordering = ('-data_inicio',)





class Hospede(models.Model):
	nome = models.CharField(unique=True,max_length=100, null=False, blank=False, verbose_name="Nome do cliente:")

	def __unicode__(self):
		return self.nome

	class Meta:
		db_table = 'hospede'
		app_label = 'suites'
		verbose_name = u'Hospede'
		verbose_name_plural = u'Hospedes'
		ordering = ['nome']