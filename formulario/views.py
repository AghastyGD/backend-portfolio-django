from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect

def enviar_mensagem(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']

        # Configuração do e-mail
        remetente = email  # Usando o e-mail do remetente como o remetente do e-mail
        destinatario_host = 'augustodomingosvasco@gmail.com' 

        email_remessa_host = EmailMessage(
            assunto,
            f"Mensagem de {nome}\n\n{mensagem}",
            remetente,
            [destinatario_host],
            reply_to=[remetente]
        )

        # Envio do e-mail para mim
        email_remessa_host.send()

        return render(request, 'mensagem_enviada.html')

    return render(request, 'index.html')

    
# Requisição para as paginas dentro da pasta Template
def projetos_python(request):
  return render(request, 'projetos-python.html')
  
def projetos_designer(request):
  return render(request, 'projetos-designer-grafico.html')
  
def projetos_web(request):
  return render(request, 'projetos-html-css-javascript.html')

def projetos_django(request):
  return render(request, 'projetos-django.html')
  