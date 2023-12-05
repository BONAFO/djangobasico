from typing import Any
from django.contrib.auth import forms
from apps.home.models import User
from django import forms as form_data


class Create_user_form(forms.UserCreationForm):
    error_css_class = "is-invalid"
    required_css_class = "required-field"

    class Meta:
        model = User
        fields = ("username", "nombre", "apellido", "dni", "edad")
        widgets = {
            "username": form_data.TextInput(attrs={"placeholder": "Nombre de usuario"}),
            "nombre": form_data.TextInput(attrs={"placeholder": "Nombre/s"}),
            "apellido": form_data.TextInput(attrs={"placeholder": "Apellido/s"}),
            "dni": form_data.TextInput(attrs={"placeholder": "Documento"}),
            "edad": form_data.TextInput(attrs={"placeholder": "Edad", "initial": 0}),
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["edad"].initial = 0

    # def is_valid(self) -> bool:
    #     validated = super().is_valid()
    #     # self.error_messages = {}

    #     field_list = []
    #     for field in self.fields.keys():
    #         field_list.insert(len(field_list), str(field))

    #     for field in field_list:
    #         try:
    #             if self.cleaned_data[field] == None:
    #                 # self.error_messages.update(
    #                 #     {field: field.upper() + " invalido o ya registrado."}
    #                 # )
    #                 self.add_error(
    #                     field=field,
    #                     error=field.capitalize() + " invalido o ya registrado.",
    #                 )
    #         except:
    #             # self.error_messages.update(
    #             #     {field: field.upper() + " invalido o ya registrado."}
    #             # )
    #             self.add_error(
    #                 field=field, error=field.capitalize() + " invalido o ya registrado."
    #             )
    #     try:
    #         if self.cleaned_data["password1"] != self.cleaned_data["password2"]:
    #             # self.error_messages.update(
    #             #     {"password": "Contraseñas invalidas o no coinciden."}
    #             # )
    #             self.add_error(
    #                 field="password1", error="Contraseñas invalidas o no coinciden."
    #             )
    #     except:
    #         # self.error_messages.update(
    #         #     {"password": "Contraseñas invalidas o no coinciden."}
    #         # )
    #         self.add_error(
    #             field="password1", error="Contraseñas invalidas o no coinciden."
    #         )

    #     return validated


class Login_User_Form(forms.AuthenticationForm):
    error_css_class = "is-invalid"
    required_css_class = "required-field"

    username = form_data.CharField(
        label="Nombre de Usuario",
        widget=form_data.TextInput(attrs={"placeholder": "Nombre de usuario"}),
    )
    password = form_data.CharField(label="Contraseña", widget=form_data.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")
        # widgets = {
        #     "username": form_data.TextInput(attrs={"placeholder": "Nombre de usuario"}),
        # }
