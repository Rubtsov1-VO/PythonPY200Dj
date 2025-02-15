from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from landing.forms import TemplateForm



# Create your views here.
class TemplView(View):
    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):

        form = TemplateForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            return JsonResponse(data=[name, email, user_agent, ip],
                                safe=False, json_dumps_params={"indent": 4})
        return render(request, 'landing/index.html', context={"form": form})
