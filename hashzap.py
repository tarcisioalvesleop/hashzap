# Flet (site, programas)
# pip install flet

# Titulo Hashzap
# botao de iniciar o chat
    # Popup
        # Bem vindo ao hashtag
        # Escreva seu nome
        # Entrar no chat
#Chat
    # Lira entrou no chat
    # Mensagens do usuário
    # campo para enviar mensagem
    # Botao de enviar


import flet as ft
from datetime import datetime
from pytz import timezone

def horario_atual():
    data_hora = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_hora_brasil = data_hora.astimezone(fuso_horario)
    data_hora_texto = data_hora_brasil.strftime('%d/%m/%Y %H:%M:%S')
    return data_hora_texto

def main(pagina):
    texto = ft.Text("Hashzap")

    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()
    
    # função do tunel de comunicação
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    # tunel de cominucação para várias pessoas visualizarem ao mesmo tempo
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{horario_atual()} {nome_usuario.value}: {campo_mensagem.value}"           
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui.", on_submit = enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click = enviar_mensagem)

    def entrar_chat(evento):
        # feche o popup
        popup.open = False
        # retirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        #adicionar o nosso chat
        pagina.add(chat)
        # criar o campo de  enviar mensagem e botao de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
            )
        pagina.add(linha_mensagem)
        texto = f"{horario_atual()} - {nome_usuario.value} entrou no chat."
        pagina.pubsub.send_all(texto)
        
        pagina.update()

    popup = ft.AlertDialog(open=False,
        modal=True, 
        title=ft.Text("Bem vindo ao Hashzap"),
        content = nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click = entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    

    pagina.add(texto)
    pagina.add(botao_iniciar)

# flet, iniciando o aplicativo
#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)