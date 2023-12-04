# def user_is_logged():
#     print("UN USUARIO ESTA LOGEADO!!")
#     return args, kargs


# *args, **kargs
from apps.modules.add_to_tuple import add_tuple

def user_is_logged2(request):
    stade = False
    try:
      stade=  request.user.is_authenticated
    except KeyError as error:
        """"""
    except Exception as error2:
        print(error2)
    return stade


def user_is_logged(request):
    stade = False
    try:
        request.session["pk"]
        stade = True
    except KeyError as error:
        """"""
    except Exception as error2:
        print(error2)
    return stade


    # def user_is_logged(origin):
    #     print("asdassdsd")
    #     def wrapper(request,slugs,*args, **kargs):
    #         stade = False
    #         try:
    #             args[0].session["pk"]
    #             stade = True
    #         except KeyError as error:
    #             ""
    #         except Exception as error2:
    #             print(error2)

    #         args = add_tuple(args, stade)
    #         return origin(*args, **kargs)

    #     return wrapper

    try:
        request.session["pk"]
        stade = True
    except KeyError as error:
        """"""
    except Error as error2:
        print(error2)
