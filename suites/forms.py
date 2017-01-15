#-*- coding:utf-8 -*-
from django import forms
from suites.models import ControleQuarto
from django.core.exceptions import ValidationError
from django.db.models import Q



class ControleQuartoForm(forms.ModelForm):
	class Meta:
		model = ControleQuarto
		fields = '__all__'

	def clean(self):

		data_inicio = self.cleaned_data["data_inicio"]
		data_fim = self.cleaned_data["data_fim"]
		nomeQuartos = self.cleaned_data["nomeQuartos"]


		if data_inicio and not data_fim and not nomeQuartos:
			raise forms.ValidationError({'data_fim': (u"Ao preencher a data início, a data fim e nome do quarto deve ser preenchida também")})
		elif data_inicio and data_fim and not nomeQuartos:
			raise forms.ValidationError({'nomeQuartos': (u"Ao preencher a data início e data fim, a nome do quarto deve ser preenchida também")})
		elif data_inicio and not data_fim and nomeQuartos:
			raise forms.ValidationError({'data_fim': (u"Ao preencher a data início e nome do quarto, a data fim deve ser preenchida também")})

		elif data_fim and not data_inicio and not nomeQuartos:
			raise forms.ValidationError({'data_inicio': (u"Ao preencher a data fim, a data inicio e nome do quarto deve ser preenchida também")})
		elif data_fim and not data_inicio and nomeQuartos:
			raise forms.ValidationError({'data_inicio': (u"Ao preencher a data fim e nome do quarto, a data início deve ser preenchida também")})

		elif nomeQuartos and not data_inicio and not data_fim:
			raise forms.ValidationError({'data_inicio': (u"Ao preencher a nome do quarto, a data início e data fim deve ser preenchida também")})
		elif not nomeQuartos and not data_inicio and not data_fim:
			raise forms.ValidationError({'data_inicio': (u"Voce precisa cadastrar todos os campos.")})


		if data_inicio and data_fim:
			if data_inicio > data_fim:
				raise forms.ValidationError({'data_fim': (u"A data fim deve ser maior que a data início")})

			total = 0
			total += ControleQuarto.objects.filter(~Q(status=4), data_inicio__lte=data_inicio,data_fim__gte=data_inicio, nomeQuartos=nomeQuartos ).exclude(pk=self.instance.id).count()
			total += ControleQuarto.objects.filter(~Q(status=4), data_inicio__lte=data_fim,data_fim__gte=data_fim, nomeQuartos=nomeQuartos).exclude(pk=self.instance.id).count()
			total += ControleQuarto.objects.filter(~Q(status=4), data_inicio__gte=data_inicio,data_fim__lte=data_fim, nomeQuartos=nomeQuartos).exclude(pk=self.instance.id).count()
			if total > 0:
				raise forms.ValidationError({'data_inicio': (u"Já existe um quarto cadastrado para este período")})

		return self.cleaned_data