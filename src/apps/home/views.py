from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_auth, authenticate, decorators, logout
from django.db import *
import json

# Create your views here.
from django.views.generic import View, FormView
from apps.home.form import *

from django.utils.decorators import method_decorator

# @user_is_logged
# def home_GET(request):
#     context = {}
#     return render(request,'home/home.html',context)
# class home_GET(ListView):
#     id = "perriot"


# def home_POST(request):
#     context = {}


# def home_PUT(request):
#     context = {}


# def home_DELETE(request):
#     context = {}


# def home(request):
#     context = {}
#     if request.method == "GET":
#         print("geti")
#         return home_GET(request)
#     elif request.method == "POST":
#         print("Peti")
#     elif request.method == "PUT":
#         print("pueti")
#     elif request.method == "DELETE":
#         print("eeti")


# EXAMPLE CLASS VIEW
# @method_decorator(user_is_logged, name="dispatch")

# def consume_is_logged(args):
#     try:
#         return args[0]
#     except:
#         return False


def get_id(request):
    if request.user.pk != None:
        return request.user.pk
    else:
        return None


def add_basic_context(request):
    context = {}
    context["id"] = get_id(request)
    context["user_is_logged"] = request.user.is_authenticated
    return context


@method_decorator(decorators.login_required(login_url="/login"), name="dispatch")
class home(View):
    def get(sefl, request, *args, **kargs):
        context = {}
        context.update(add_basic_context(request))
        # consume_is_logged(args)
        # context["user_is_logged"] = request.user.is_authenticated

        return render(request, "home/home.html", context)
        # if request.user.is_authenticated:
        #     return render(request,

        #     return redirect("/login")


# EXAMPLE CLASS VIEW


# @decorators.permission_required('home.add_user',raise_exception=True)


def signup(request):
    context = {}
    context["error"] = {}
    # context["user_is_logged"] = request.user.is_authenticated
    context.update(add_basic_context(request))

    context["form"] = Create_user_form
    if request.method == "GET":
        return render(request, "home/signup.html", context)
    elif request.method == "POST":
        form_data = Create_user_form(request.POST)
        if form_data.is_valid():
            try:
                form_data.save()
                user = authenticate(
                    request,
                    username=form_data.cleaned_data["username"],
                    password=form_data.cleaned_data["password1"],
                )

                if user is not None and user.is_active:
                    login_auth(request, user)
                    # request.session["pk"] = user.pk
                    return redirect("/home")
                else:
                    return redirect("/signup")
            except IntegrityError as err:
                print(err)
                return render(request, "home/signup.html", context)

        else:
            # ["password_mismatch"]
            # context["errors"] = form_data.error_messages
            # context["errors"]["password_mismatch"] = ""
            # context["errors"]["password1"] = ""
            # context["errors"]["password2"] = ""
            context["errors"] = form_data.errors.values()
            return render(request, "home/signup.html", context)

    # context = {}
    # context["form"] = Create_user_form
    # if request.method == "GET":
    #     return render(request, "home/signup.html", context)
    # elif request.method == "POST":

    #     form = Create_user_form(request.POST)
    #     if form.is_valid():
    #         # for key in request.POST.keys():
    #         #     if key != "csrfmiddlewaretoken":
    #         #         data.update({key: request.POST[key]})
    #         # data.update({"password": data["password1"]})
    #         # data.__delitem__("password1")
    #         # data.__delitem__("password2")

    #         # print(data)
    #         try:
    #             form.save()
    #             user = authenticate(
    #                 request,
    #                 username=form.cleaned_data["username"],
    #                 password=form.cleaned_data["password1"],
    #             )

    #             if user is not None and user.is_active:
    #                 login_auth(request, user)

    #                 return redirect("/home")
    #             else:
    #                 return redirect("/signup")
    #         except IntegrityError as err:
    #             print(err)
    #             return render(request, "home/signup.html", context)
    #     else:
    #         print(form.error_messages)
    #         context["errors"] = form.error_messages
    #         return render(request, "home/signup.html", context)


def login(request):
    context = {}
    context["form"] = Login_User_Form
    # context["user_is_logged"] = request.user.is_authenticated

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None and user.is_active:
            login_auth(request, user)
            # request.session["pk"] = user.pk
            return redirect("/home")
        else:
            context["error"] = "Credenciales incorrectas."
    return render(request, "home/login.html", context)


# def logout_view(request):
#     logout(request)


class logout_view(View):
    def get(sefl, request, *args, **kargs):
        logout(request)
        return redirect("/login")


# class login(FormView):
#     template_name = "home/login.html"
#     form_class = Create_user_form
#     success_url = "/home"


#     def form_valid(self, form):
#         print(form)
#         return super().form_valid(form)


# from myapp.forms import ContactForm
# from django.views.generic.edit import FormView


# class ContactFormView(FormView):
#     template_name = "contact.html"
#     form_class = ContactForm
#     success_url = "/thanks/"


#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)
def is_logged_view(request):
    stade = False
    try:
        request.session["pk"]
        stade = True
    except KeyError as error:
        """"""
    except Error as error2:
        print(error2)

    return JsonResponse({"status": stade}, safe=False)
