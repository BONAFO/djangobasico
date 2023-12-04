from django.shortcuts import render, redirect
from django.contrib.auth import decorators, authenticate
from django.http import JsonResponse, HttpResponse
from apps.home.models import User
from apps.users.forms import Update_User_Form
from django.db import Error

# Create your views here.
# from apps.home.decorators import user_is_logged


def validate_password(oldp, newp, renewp, request):
    change = True
    errors = {}

    if oldp is False:
        change = False
    if newp is False:
        change = False
    if renewp is False:
        change = False
    if change:
        print("CMBIAMOS")
    else:
        return {"err": "", "bool": change }
    try:
        user = User.objects.filter(pk=200).values_list("username")
        print(len(user))
        # auth = authenticate(request, username=user, password=oldp)
        if len(user) == 0:
            return {"err": "", "bool": False}
        else:
            return {"err": "Contraseña original erronea o invalida", "bool": False}
    except Error as error:
        return {"err": error, "bool": False}


# AGREGAR UN MIDDLE DONDE VALIDE TANTO CUENTA DE SUPER ADMIN (QUE LA PASSWORD SEA LA SUYA) Y
# QUE EL ID Y CONTRA CORRESPONDAN A LA CUENTA QUE SE QUIERE BORRAR EN CASO DE UNO NORMAL
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


def update_user(request, id):
    context = {}
    context["form"] = Update_User_Form(user_id=id)
    #     1
    # dni False
    # 99
    # password True
    # False
    # new_password False
    # False
    # new_re_password False
    # False
    if request.method == "POST":
        context["errs"] = {}
        form = Update_User_Form(request.POST)
        # print(request.POST)
        # print(form.is_valid())
        # print(form.cleaned_data)
        if form.is_valid():
            print(form.cleaned_data)
            pass_validations = validate_password(
                oldp=form.cleaned_data["password"],
                newp=form.cleaned_data["new_password"],
                renewp=form.cleaned_data["new_re_password"],
                request=request,
            )
            
            if pass_validations["bool"] :
                1
            else :
                # form.cleaned_data
                form.cleaned_data.pop("password")
                form.cleaned_data.pop("new_password")
                form.cleaned_data.pop("new_re_password")
             
            print(pass_validations)    
            print(form.cleaned_data)

            # validate_password(
            #     oldp=form.cleaned_data["password"],
            #     newp=form.cleaned_data["new_password"],
            #     renewp=form.cleaned_data["new_re_password"],
            #     request=request,
            # )
            # form.cleaned_data["id"] = id
            # form.save()
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
