from collections.abc import Mapping
from typing import Any
from django.contrib.auth import forms, authenticate, password_validation
from django.forms.utils import ErrorList
from apps.home.models import User
from django import forms as form_model
from django.core.exceptions import ValidationError


def validate_password(oldp, newp, renewp, username, request):
    msg = {"txt": [], "bool": True}
    if oldp is False:
        msg["bool"] = False
    elif newp is False:
        msg["bool"] = False
    elif renewp is False:
        msg["bool"] = False
    elif renewp != newp:
        msg["txt"].append(
            {
                "txt": "Las nuevas contraseñas no coinciden.",
                "field": "new_password",
            }
        )
        msg["bool"] = False
    elif oldp == newp:
        msg["txt"].append(
            {"txt": "Tu nueva contraseña no puede ser la antigua.", "field": "new_re_password"}
        )
        msg["bool"] = False

    if msg["bool"]:
        try:
            password_validation.validate_password(newp)
        except ValidationError as error:
            # print(1111)
            # errore = errore + list(error)
            error_list = list(error)
            raw_txt = "Su nueva contraseña contiene los siguientes errores: "
            for err in error_list:
                raw_txt += err + ","
            msg["txt"].append({"txt": raw_txt, "field": "password"})
            # msg["txt"] +
            msg["bool"] = False
        if msg["bool"]:
            auth = authenticate(request, username=username, password=oldp)
            if auth is None:
                msg["txt"].append("Contraseña original erronea o invalida")
                msg["txt"].append(
                    {
                        "txt": "Las nuevas contraseñas no coinciden.",
                        "field": "password",
                    }
                )
                msg["bool"] = False
            else:
                msg["bool"] = True
    return msg


class Update_User_Form(form_model.ModelForm):
    error_css_class = "is-invalid"
    required_css_class = "required-field"
    # nombre = form_model.CharField(
    #     label="Nombre",
    #     empty_value=False,
    #     required=True,
    #     widget=form_model.TextInput(
    #         attrs={"placeholder": "Nombre/s", "class": "form-input"}
    #     ),
    # )
    # apellido = form_model.CharField(
    #     empty_value=False,
    #     required=True,
    #     widget=form_model.TextInput(
    #         attrs={"placeholder": "", "class": "form-input"}
    #     ),
    # )

    # edad = form_model.IntegerField(
    #     label="Edad",
    #     required=True,
    #     widget=form_model.NumberInput(
    #         attrs={"placeholder": "Edad", "class": "form-input"}
    #     ),
    # )

    # dni = form_model.CharField(
    #     empty_value=False,
    #     required=True,
    #     widget=form_model.TextInput(
    #         attrs={"placeholder": "Documento", "class": "form-input"}
    #     ),
    # )

    password = form_model.CharField(
        empty_value=False,
        required=False,
        widget=form_model.PasswordInput(
            attrs={"placeholder": "Contraseña actual", "class": "form-input"}
        ),
    )

    new_password = form_model.CharField(
        empty_value=False,
        required=False,
        widget=form_model.PasswordInput(
            attrs={"placeholder": "Nueva contraseña", "class": "form-input"}
        ),
    )

    new_re_password = form_model.CharField(
        empty_value=False,
        required=False,
        widget=form_model.PasswordInput(
            attrs={"placeholder": "Repita la nueva contraseña", "class": "form-input"}
        ),
    )

    class Meta:
        model = User
        fields = ["nombre", "apellido", "edad", "dni"]
        widgets = {
            "nombre": form_model.TextInput(
                attrs={"placeholder": "Nombre/s", "class": "form-input"}
            ),
            "apellido": form_model.TextInput(
                attrs={"placeholder": "Apellido/s", "class": "form-input"}
            ),
            "edad": form_model.NumberInput(
                attrs={"placeholder": "Edad", "class": "form-input"}
            ),
            "dni": form_model.TextInput(
                attrs={"placeholder": "Documento", "class": "form-input"}
            ),
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)
        if user_id is not None:
            user_data = User.objects.filter(pk=user_id).values()[0]
            self.fields["nombre"].initial = user_data["nombre"]
            self.fields["apellido"].initial = user_data["apellido"]
            self.fields["edad"].initial = user_data["edad"]
            self.fields["dni"].initial = user_data["dni"]

    # def clean(self) -> dict[str, Any]:
    #     # print(self["password"].value())
    #     # clean_data  = super().clean()
    #     # clean_data["password"] = self["password"].value()
    #     print(self["password"].value())
    #     return {}
    def is_valid(self, request) -> bool:
        super().is_valid()
        final_validation = {"bool": False, "txt": ""}
        user_data = User.objects.filter(pk=request.user.pk).values()[0]

        to_erase = []

        for k in self.cleaned_data:
            if k.find("password") == -1 and (
                self.cleaned_data[k] == False or self.cleaned_data[k] == user_data[k]
            ):
                to_erase.append(k)

        for k in to_erase:
            try:
                self.cleaned_data.pop(k)
            except:
                False

        pass_validations = validate_password(
            oldp=self.cleaned_data["password"],
            newp=self.cleaned_data["new_password"],
            renewp=self.cleaned_data["new_re_password"],
            username=user_data["username"],
            request=request,
        )

        if not pass_validations["bool"]:
            self.cleaned_data.pop("password")
            self.cleaned_data.pop("new_re_password")
            self.cleaned_data.pop("new_password")

        for err in pass_validations["txt"]:
            self.add_error(field=err["field"], error=err["txt"])
            # self.add_error({
            #     "field": "asdasd",
            #     "error" : "asasdaad"
            # })

        if len(self.cleaned_data) == 0:
            return pass_validations["bool"]
        else:
            return True

    # def save(self, *args, **kwargs):
    #     data = self.cleaned_data
    #     original = User.objects.filter(pk=data["id"]).values()[0]
    #     changed = {}
    #     print(original)
        # validate_password(
        #     oldp= data["password"],
        #     newp= data["new_password"],
        #     renewp= data["new_re_password"],
        #     user= original["username"]
        # )

        # for k in data:

        #     if k.find('password') == -1:
        #         # print("password")
        #         # print(data[k])
        #         1
        # print("no password")
        # print(data[k])
        # if k.find('password') != -1 and data[k] != original[k]:
        #     print(data[k])
        # if k == "dni":
        #     if data["dni"] != original["dni"]:
        # else:
        #     1

    # def __init__(self, data: Mapping[str, Any] | None = ..., files: Mapping[str, Any] | None = ..., auto_id: bool | str | None = ..., prefix: str | None = ..., initial: Mapping[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., field_order: Any | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
    #     super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order, use_required_attribute, renderer)
    #     print("teno miedo")

    # password = form_model.CharField(
    #     empty_value=False,
    #     required=True,
    #     widget=form_model.PasswordInput(attrs={"placeholder": "Contraseña actual"}),
    # )


# class Meta:
#     # model = User
#     # fields = ("nombre", "apellido", "edad")
#     # widgets= {
#     #     'nombre': form_model.TextInput(attrs={"initial": "Perrito"})
#     # }
#     # initials= {
#     #     'nombre': "xperrito"
#     # }

# cosa = {
#     "username": "pecdrito",
#     "apellido": "Asd",
#     "dni": "12312412",
#     "edad": 123,
#     "password": "asd",
# }
# per = User(**cosa)
# per.set_password(raw_password=per.password)
# print(123)
# print(per.password)
