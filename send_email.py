import pyautogui
import pyperclip

def send_email(destinatario, assunto, ticker, cot_max, cot_min, cot_at):
    destinatario = destinatario
    assunto = assunto
    mensagem = f'''
    Prezado Gestor,

    Seguem as análises da ação: {ticker}, referente aos últimos seis meses.

    - Cotação máxima: $ {round(cot_max,2)}
    - Cotação mínima: $ {round(cot_min,2)}
    - Cotação atual: $ {round(cot_at,2)}

    Atenciosamente,

    Paulo Jonas

    '''

    return destinatario, assunto, mensagem
