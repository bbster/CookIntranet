from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os
from django.shortcuts import render



class VueAppView(View):

    def get(self, request):
        try:
            # with open(os.path.join(str(settings.ROOT_DIR), 'frontend', 'dist', 'index.html'),'r') as file:
            # file = open(os.path.join(str(settings.ROOT_DIR), 'frontend', 'dist', 'index.html'),'r')
            # return HttpResponse(print(file.read()),status=200)
            # file = open(os.path.join(str(settings.ROOT_DIR), 'frontend', 'dist', 'index.html'))
            # return HttpResponse(print(file),status=200)
            return render(request,os.path.join(str(settings.ROOT_DIR), 'frontend', 'dist', 'index.html'))
        except:
            return HttpResponse(
                """
                index.html not found ! build your Vue app !!
                """,
                status=501,
            )