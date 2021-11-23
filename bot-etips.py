import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '2141956602:AAEDKn7ol49GoaXeapzGxc-hsFfZ7Lc7Zjo'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('come�ar', 'Come�ar','comecar','Comecar'):
            return f'''Ol� Seja bem vindo(a) ao Bot do E-Vip Tips, Digite o n�mero da sua d�vida, gostaria de saber sobre:{os.linesep}1 - Como Funciona o Grupo Vip?{os.linesep}2 - Qual o Valor do Grupo Vip?{os.linesep}3 -  Posso cancelar a qualquer momento?{os.linesep}4 - Entrar em contato com o Administrador para uma d�vida espec�fica!'''
        if mensagem == '1':
            return f'''O grupo Vip funciona com entradas di�rias de sinais para os jogos de futebol virtual da Bet365, os sinais cont�m o link que envia voc� diretamente para o jogo. Caso seja iniciante voc� receber� um curso de como operar :){os.linesep}Posso lhe ajudar em mais alguma coisa?(s/n)
            '''
        elif mensagem == '2':
            return f'''O Grupo Vip est� com o valor promocional de 29,99$ (Valor Mensal){os.linesep}Voc� quer adquirir o Vip?(Digite: comprar)
            '''
        elif mensagem == '3':
            return f'''Com certeza, mas aposto que voc� ir� ficar conosco por um bom tempo :){os.linesep}Voc� quer adquirir o Vip?(Digite: Comprar)'''
        elif mensagem == '4':
            return f'''Certo, esse � o contato via whatsapp: wa.me/5522999645659 o Suporte ir� tirar suas d�vidas :){os.linesep}Posso lhe ajudar em mais alguma coisa?(s/n)'''
        
        
        elif mensagem.lower() in ('s', 'sim'):
            return 'Como o Bot Vip pode lhe ajudar? Digite "Come�ar"'
        elif mensagem.lower() in ('n', 'n�o'):
            return '''Voc� quer adquirir o Vip? '''
        elif mensagem.lower() in ('comprar'):
          return f'''Digite a da forma de pagamento:{os.linesep}Pix {os.linesep}Cart�o{os.linesep}Boleto{os.linesep}'''    
        
        elif mensagem == 'Boleto':
          return '''Aten��o no boleto voc� s� ter� acesso ap�s 1 a 3 dias �teis
          Clique no Link: https://link.pagar.me/lSkd2N5cdt '''
        elif mensagem == 'Cart�o':
          return '''Aten��o Fa�a o pagamento para Link:
          Clique no Link: sem link por enquanto '''   
        elif mensagem == 'Pix':
          return '''Aten��o Fa�a o pagamento para o Pix:
          Clique no Link: https://nubank.com.br/pagar-cobranca/8h7ue/6rLkgj9Zgr 
          '''


        else:
            return 'Como o Bot Vip pode lhe ajudar? Digite "Come�ar"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()