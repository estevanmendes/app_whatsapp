from flask import Flask, request, Response
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
import string
from google_form import post_despesa,post_receita,post_reserva

    
def delete_files():
    try:
        os.remove('categoria.txt')
    except:
        pass
    try:
        os.remove('valor.txt')
    except:
        pass
    try:
        os.remove('subcategoria.txt')
    except:
        pass
    try:
        os.remove('especificacao.txt')
    except:
        pass





def set_categoria(categoria):
    with open('categoria.txt','w+') as f:
        f.write(categoria)
        f.close()

def get_categoria():
    with open('categoria.txt','r') as f:
        categoria=f.read()
        f.close()
    return categoria

def set_valor(valor):
    with open('valor.txt','w+') as f:
        f.write(valor)
        f.close()

def get_valor():
    with open('valor.txt','r') as f:
        valor=f.read()
        f.close()
    return valor

def set_subcategoria(subcategoria):
    with open('subcategoria.txt','w+') as f:
        f.write(subcategoria)
        f.close()

def get_subcategoria():
    with open('subcategoria.txt','r') as f:
        subcategoria=f.read()
        f.close()
    return subcategoria

def set_especificacao(especificacao):
    with open('especificacao.txt','w+') as f:
        f.write(especificacao)
        f.close()
def get_especificacao():
    with open('especificacao.txt','r') as f:
        especificacao=f.read()
        f.close()
    return especificacao

def letter2key(categoria,letter):
    dict_despesa={'a':'Educação','b':'Lazer','c':'Comida','d':'Uber','e':'1001','f':'Lanche','g':'Outro','h':'Internet','i':'Onibus','j':'Cartao','k':'roupa','l':'farmacia'}
    dict_receita={'a':'Salário','b':'IC','c':'Flash','d':'Outro'}
    dict_reserva={'a':'Poupança','b':'Investimento','c':'Outro'}
    if 'despesa' in categoria:
        return dict_despesa[letter]
    elif 'receita' in categoria:
        return dict_receita[letter]
    else:
        return dict_reserva[letter]


def post_form(categoria,valor,subcategoria,especificacao):
    if 'despesa' in categoria:
        post_despesa(valor,subcategoria,especificacao)
    if 'receita' in categoria:
        post_receita(valor,subcategoria,especificacao)
    else:
        post_reserva(valor,subcategoria,especificacao)
    
    
def text_answer(text,end=True):
    sentence_end='\nPara encerrar o log finaceiro escreve "fim"'
    resp = MessagingResponse()
    text=text
    msg = resp.message()
    if end:
        msg.body(text+sentence_end)
    else:
        msg.body(text)
    return Response(str(resp), mimetype="application/xml")

def msg_financas():    
    text='*Digite o  que você deseja Resgistrar*:\nDespesa, \nReceita, \nReserva'
    return text_answer(text)

def msg_valor():    
    text='Digite o valor em reais, utilizando o ponto para separar a casa decimal'
    return text_answer(text)


def msg_despesa():
    text='*Digite a categoria da despesa*:\na - Educação,\nb - Lazer,\nc - Comida\nd - Uber,\ne - 1001,\nf - Lanche,\ng - Outro,\nh - Internet,\ni - Onibus,\nj - Cartao,\nk - Roupa,\nl - farmacia'    
    return text_answer(text)

def msg_receita():    
    text='*Digite a categoria da receita*:\na - Salário,\nb - IC,\nc - Flash,\nd - Outro'    
    return text_answer(text)

def msg_reserva():
    text='*Digite a categoria da reserva*:\na - Poupança,\nb - Investimento,\nc - Outro'    
    return text_answer(text)

def msg_summary(type='a'):
    categoria= get_categoria()
    valor=get_valor()
    subcategoria=get_subcategoria()
    especificacao=get_especificacao
    post_form(categoria,valor,subcategoria,especificacao)
    if type=='a':
        text=f'As seguintes informações foram armazenadas:\n*R${valor}*\n*{categoria}*\n*{subcategoria}*'
    else:
        text=f'As seguintes informações foram armazenadas:\n*R${valor}*\n*{categoria}*\n*{subcategoria}*\n*{especificacao}*'
    delete_files()
    return text_answer(text,end=False)
    
def msg_especifique():
    text='*Especifique abaixo*'
    return text_answer(text)

def final():
    text='*Log financeiro encerrado*'
    return text_answer(text,end=False)

app = Flask(__name__)


@app.route('/controle', methods=['POST'])
def main():
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg)

    if 'finanças' in incoming_msg or 'financas' in incoming_msg:
        answer=msg_financas()
        print(incoming_msg)

    elif 'despesa' in incoming_msg or 'receita' in incoming_msg or 'reserva' in incoming_msg:
        answer=msg_valor()
        set_categoria(incoming_msg)
        with open('categoria.txt','w+') as f:
            f.write(incoming_msg)
            f.close()
            
    elif incoming_msg.replace('.','').isdigit():
        valor=incoming_msg
        set_valor(valor)        
        categoria=get_categoria()

        if 'despesa' in categoria:     
            answer=msg_despesa()
        
        elif 'receita' in categoria:     
            answer=msg_receita()
        
        elif 'reserva' in categoria:
            answer=msg_reserva()

    elif incoming_msg in list(string.ascii_lowercase):
        categoria=get_categoria()
        subcategoria=letter2key(categoria,incoming_msg)
        set_subcategoria(subcategoria)
        set_especificacao('')
        if subcategoria=='Outro':
            answer=msg_especifique()

        else:
            
            answer=msg_summary(type='a')

    elif 'fim' in incoming_msg:
        print('delete')
        delete_files()
        answer=final() 

    elif os.path.isfile('especificacao.txt'):
        set_especificacao(incoming_msg)
        
        answer=msg_summary('b')

    else:
        answer=msg_financas()
        print(incoming_msg)

    return answer



if __name__ == '__main__':
   app.run(debug=True)

