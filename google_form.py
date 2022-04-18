import requests


def post_despesa(valor,subcategoria,especificacao,pagamento):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPITRuasiOIB04gC4_fD3SC3Q-449HlGC-1gUTLtGZRXurQ/formResponse"
    form_data = {"entry.1329131462":"Despesa",
                "entry.375738980":valor,
                "entry.2019213725":subcategoria,
                "entry.261790289":especificacao,
                "entry.158565019":pagamento,
                "entry.2061799446":0            
                }
    response=requests.post(url, data=form_data)
    return response.status_code


def post_receita(valor,subcategoria,especificacao,pagamento=None):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfwAyvm29dBhSe0COjV41P8XQOBixCuDZ1rcPJwzdOeHjKDtg/formResponse"
    form_data = {"entry.1329131462":"Receita",
                "entry.375738980":valor,
                "entry.600766828":subcategoria,
                "entry.487388316":especificacao            
                }
    response=requests.post(url, data=form_data)
    return response.status_code               

def post_reserva(valor,subcategoria,especificacao,pagamento=None):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSf4S5P7Tv0AWIY6wNgmqXFAutvuy5Q19U0YT1TXb4WE3uDHZw/formResponse"

    form_data = {"entry.1329131462":"Reserva",
                "entry.375738980":valor,
                "entry.904255864":subcategoria,
                "entry.904255864.other_option_response":especificacao            
                }
    response=requests.post(url, data=form_data)
    return response.status_code
