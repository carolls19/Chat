#Título Chat
#Botão iniciar chat
    #pop up/alerta/modal
        #Título: "Bem-vindo ao Chat"
        #Campo de texto: Escreva seu nome no chat
        #Botão: Entrar no chat
            #Sumir com o título e o botão inicial
            #Fechar o pop up 
            #Criar o chat (com mensagem de "nome do usuário entrou no chat")
            #Embaixo do chat: 
                #Campo de texto: Digite sua mensagem
                #Botão enviar
                    #Aparece a mensagem no chat com  nome do usuário

#principais pacotes para criar sites no python: flask, django, fast api, tonado e flet
#Flet - aplicativo/site/programa de computador

#importar o flet 

import flet as ft

#criar a função principal do sistema

def main (pagina):
    #criar algo   
    titulo = ft.Text("Chat")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #cria o túnel de comunicação
   
    
    titulo_janela = ft.Text("Bem vindo ao chat")

    campo_nome = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem(evento):
        texto = f"{campo_nome.value}: {texto_mensagem.value}"
        #enviar mensagem no formato usuario: mensagem 
        #enviar mensagem no túnel
        pagina.pubsub.send_all(texto)
        # limpar o campo mensagem
        texto_mensagem.value = ""
        pagina.update()

#arquivo = ft.FilePicker() -> para adicionar imagem no chat

    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    #Colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    def entrar_chat(evento):
        
        #tirar o titulo da página
        pagina.remove(botao_iniciar) 
        #tirar o botao_iniciar 
        pagina.remove(titulo)
        #fechar o popup/janela
        janela.open = False
        #criar o chat 
        pagina.add(chat)      
        #adicionar linha de mensagem 
        pagina.add(linha_mensagem)
        #adicionar mensagem: usuario entrou no chat
        texto_entrou =  f"{campo_nome.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou)
        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    
    janela = ft.AlertDialog(title = titulo_janela, content = campo_nome, actions = [botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.FilledButton("Iniciar Chat", on_click = abrir_popup)
    
    #colocar o algo na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

#executar o sistema
ft.app(main, view = ft.WEB_BROWSER)