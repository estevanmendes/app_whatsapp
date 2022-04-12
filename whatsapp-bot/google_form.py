import requests


def post_despesa(valor,subcategoria,especificacao):
    url = "https://docs.google.com/forms/d/e/10PwFbdctcSdEUJQKDuT9t1RWimwXx-TKX8cRdoabahc/formResponse"
    form_data = {"entry.1329131462":"Despesa",
                "entry.375738980":valor,
                "entry.600766828":subcategoria,
                "":especificacao            
                }
    response=requests.post(url, data=form_data)
    return response


def post_receita(valor,subcategoria,especificacao):
    url = "https://docs.google.com/forms/d/e/1QlTR6x2V_b0YKJ2wyGORvH6ewmS7S6V9a4UKwqe-254/formResponse"
    form_data = {"entry.1329131462":"Receita",
                "entry.375738980":valor,
                "entry.600766828":subcategoria,
                "entry.487388316":especificacao            
                }
    response=requests.post(url, data=form_data)
    return response                

def post_reserva(valor,subcategoria,especificacao):
    url = "https://docs.google.com/forms/d/e/1hJC-EapqmL6zSgPJ4O9DHSYlO1LP-V8vbBsnKkjFkQg/formResponse"

    form_data = {"entry.1329131462":"Reserva",
                "entry.375738980":valor,
                "entry.904255864":subcategoria,
                "entry.904255864.other_option_response":especificacao            
                }
    response=requests.post(url, data=form_data)
    return response
