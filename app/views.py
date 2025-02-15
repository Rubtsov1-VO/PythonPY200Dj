from lib2to3.fixes.fix_input import context

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView
from django.views import View
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm, CustomUserCreationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView


def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

   # if request.method == "POST":
        #received_data = request.POST  # Приняли данные в словарь
        #my_text = received_data.get('my_text')
        #my_email = received_data.get('my_email')
        #my_pass = received_data.get('my_pass')
        # как пример получение данных по ключу `my_text`
        # my_text = received_data.get('my_text')
    if request.method == "POST":
        form = TemplateForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            my_text = form.cleaned_data.get("my_text")
            my_email = form.cleaned_data.get("my_email")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_pass = form.cleaned_data.get("my_pass")
            my_date = form.cleaned_data.get("my_date")
            my_int = form.cleaned_data.get("my_int")
            my_check = form.cleaned_data.get("my_check")
            return JsonResponse(data=[my_text, my_check, my_date, my_email, my_int, my_pass, my_select, my_textarea], safe=False, json_dumps_params={"indent": 4})
        # TODO Проведите здесь получение и обработку данных если это необходимо
        return render(request, 'app/template_form.html', context={"form":form})
        #return JsonResponse(data={"text": my_text, "email": my_email, "password": my_pass},json_dumps_params={"ensure_ascii": False})
        # TODO Верните HttpRequest или JsonResponse с данными


def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    #if request.method == "POST":
    #    data = request.POST
    #    user = authenticate(username=data["username"], password=data["password"])
    #    if user:
    #        login(request, user)
    #        return redirect("app:user_profile")
    #    return render(request, "app/login.html", context={"error": "Неверные данные"})
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})

def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    #if request.method == "POST":
    #    return render(request, 'app/register.html')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Возвращает сохраненного пользователя из данных формы
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("app:user_profile")

        return render(request, 'app/register.html', context={"form": form})

def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')

def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})


class TemplView(View):
    def get(self, request):
        return render(request, 'app/template_form.html')
    # TODO скопируйте код, что есть в template_view в теле условия request.method == "GET"

    def post(self, request):

        form = TemplateForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            my_text = form.cleaned_data.get("my_text")
            my_email = form.cleaned_data.get("my_email")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_pass = form.cleaned_data.get("my_pass")
            my_date = form.cleaned_data.get("my_date")
            my_int = form.cleaned_data.get("my_int")
            my_check = form.cleaned_data.get("my_check")
            return JsonResponse(data=[my_text, my_check, my_date, my_email, my_int, my_pass, my_select, my_textarea],
                                safe=False, json_dumps_params={"indent": 4})
        # TODO Проведите здесь получение и обработку данных если это необходимо
        return render(request, 'app/template_form.html', context={"form": form})
# TODO скопируйте код, что есть в template_view в теле условия request.method == "POST"


class MyTemplView(TemplateView):
    template_name = 'app/template_form.html'

    def post(self, request, *args, **kwargs):
        form = TemplateForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            my_text = form.cleaned_data.get("my_text")
            my_email = form.cleaned_data.get("my_email")
            my_select = form.cleaned_data.get("my_select")
            my_textarea = form.cleaned_data.get("my_textarea")
            my_pass = form.cleaned_data.get("my_pass")
            my_date = form.cleaned_data.get("my_date")
            my_int = form.cleaned_data.get("my_int")
            my_check = form.cleaned_data.get("my_check")
            return JsonResponse(data=[my_text, my_check, my_date, my_email, my_int, my_pass, my_select, my_textarea],
                                safe=False, json_dumps_params={"indent": 4})
        # TODO Проведите здесь получение и обработку данных если это необходимо
        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
        # TODO прописываем всё что было в методе post в TemplView(View)

class MyFormView(FormView):
    template_name = 'app/template_form.html'
    form_class = TemplateForm
    success_url = '/'

    def form_valid(self, form):
        return JsonResponse(form.cleaned_data)

class MyLoginView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True  # Данный флаг не позволит авторизированному
    # пользователю зайти на страницу с авторизацией и сразу его перенаправит на
    # ссылку редиректа. По умолчанию redirect_authenticated_user = False