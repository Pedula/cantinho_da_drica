#-*- coding:utf-8 -*-
from django.contrib import admin
from suites.models import NomeQuarto, ControleQuarto
from suites.forms import ControleQuartoForm
from django.utils import timezone


class ControleQuartoAdmin(admin.ModelAdmin):
	form = ControleQuartoForm

	def nome_quarto(self):
		return ", ".join([p.nome for p in self.nomeQuartos.all()])
	nome_quarto.short_description = 'Nome dos quartos'


	list_display = ('txt_data_inicio', 'txt_data_fim', nome_quarto)

	def txt_data_inicio(self, instance):
		if instance.data_inicio:
			return timezone.localtime(instance.data_inicio).strftime("%d/%m/%Y %H:%M")
		else:
			return "--"

	def txt_data_fim(self, instance):
		if instance.data_fim:
			return timezone.localtime(instance.data_fim).strftime("%d/%m/%Y %H:%M")
		else:
			return "--"

admin.site.register(NomeQuarto)
admin.site.register(ControleQuarto, ControleQuartoAdmin)
