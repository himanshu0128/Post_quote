from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from helper import convert_text_to_img


def index(request):
	context = {
		"img_url" : convert_text_to_img()
	}
	return render(request, 'index.html', context=context)
