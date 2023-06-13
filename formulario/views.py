from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect

def enviar_mensagem(request):
  if request.method == 'POST':
    nome = request.POST['nome']
    email = request.POST['email']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    send_mail ('Contacto', mensagem, 'settings.EMAIL_HOST_USER',[email, 'example@gmail.com'], fail_silently = False)
    
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