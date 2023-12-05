from django.shortcuts import render, redirect
from django.contrib.auth import decorators, authenticate
from django.http import JsonResponse, HttpResponse
from apps.home.models import User
from apps.users.forms import Update_User_Form
from django.db import Error
from apps.home.views import add_basic_context
# Create your views here.
# from apps.home.decorators import user_is_logged


# AGREGAR UN MIDDLE DONDE VALIDE TANTO CUENTA DE SUPER ADMIN (QUE LA PASSWORD SEA LA SUYA) Y
# QUE EL ID Y CONTRA CORRESPONDAN A LA CUENTA QUE SE QUIERE BORRAR EN CASO DE UNO NORMAL


# @decorators.permission_required("home.delete_user")
# def test(request, id):
#     print(id)
#     return HttpResponse("asdasdasd")

@decorators.login_required(login_url="/login")
def delete_confirm(request, id):
    if request.method == "POST":
        if request.user.has_perm("home.delete_user") or (
            request.user.pk == id
            and authenticate(
                request,
                username=request.user.username,
                password=request.POST["password"],
            )
            == request.user
        ):
            User.objects.filter(pk=id).delete()
            return JsonResponse(status=200, data={})
        else:
            return JsonResponse(status=403, data={})
    else:
        return HttpResponse(status=404)


# User.objects.filter()
@decorators.login_required(login_url="/login")
def update_user(request, id):
    context = {}
    context.update(add_basic_context(request))
    context["form"] = Update_User_Form(user_id=id)
    if request.method == "POST":
        context["errors"] = []
        form = Update_User_Form(request.POST)
        form_validation = form.is_valid(request=request)
        # context["errors"] += list(form.errors.values()) + form_validation["txt"]
        # print(context["errors"])
        if form_validation:
            # if pass_validations["bool"] == False:
            #     form.cleaned_data.pop("password")
            #     form.cleaned_data.pop("new_password")
            #     form.cleaned_data.pop("new_re_password")

            # validate_password(
            #     oldp=form.cleaned_data["password"],
            #     newp=form.cleaned_data["new_password"],
            #     renewp=form.cleaned_data["new_re_password"],
            #     request=request,
            # )
            # form.cleaned_data["id"] = id
            # form.save()
            try:
                password = User()
                password.set_password(form.cleaned_data["new_password"])
                form.cleaned_data["password"] = password.password
                form.cleaned_data.pop("new_re_password")
                form.cleaned_data.pop("new_password")
            except:
                False
            # print(form.cleaned_data)
            User.objects.filter(pk = request.user.pk).update(**form.cleaned_data)
            return render(request, "usuarios/update_user.html", context)
        else:
            return render(request, "usuarios/update_user.html", context)
    else:
        return render(request, "usuarios/update_user.html", context)


# def delete_user_view(request, id):
#     context = {}
#     if request.user.id != id:
#         print(
#             "El usuario ["
#             + str(request.user.id)
#             + "] intento eliminar al usuario ["
#             + str(id)
#             + "]... sos medio turbio... y no queremos gente turbia..."
#         )
#         return redirect("/logout")

#     return render(request, "users/delete.html", context)
