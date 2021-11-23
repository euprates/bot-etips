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
        if eh_primeira_mensagem == True or mensagem in ('começar', 'Começar','comecar','Comecar'):
            return f'''Olá Seja bem vindo(a) ao Bot do E-Vip Tips, Digite o número da sua dúvida, gostaria de saber sobre:{os.linesep}1 - Como Funciona o Grupo Vip?{os.linesep}2 - Qual o Valor do Grupo Vip?{os.linesep}3 -  Posso cancelar a qualquer momento?{os.linesep}4 - Entrar em contato com o Administrador para uma dúvida específica!'''
        if mensagem == '1':
            return f'''O grupo Vip funciona com entradas diárias de sinais para os jogos de futebol virtual da Bet365, os sinais contém o link que envia você diretamente para o jogo. Caso seja iniciante você receberá um curso de como operar :){os.linesep}Posso lhe ajudar em mais alguma coisa?(s/n)
            '''
        elif mensagem == '2':
            return f'''O Grupo Vip está com o valor promocional de 29,99$ (Valor Mensal){os.linesep}Você quer adquirir o Vip?(Digite: comprar)
            '''
        elif mensagem == '3':
            return f'''Com certeza, mas aposto que você irá ficar conosco por um bom tempo :){os.linesep}Você quer adquirir o Vip?(Digite: Comprar)'''
        elif mensagem == '4':
            return f'''Certo, esse é o contato via whatsapp: wa.me/5522999645659 o Suporte irá tirar suas dúvidas :){os.linesep}Posso lhe ajudar em mais alguma coisa?(s/n)'''
        
        
        elif mensagem.lower() in ('s', 'sim'):
            return 'Como o Bot Vip pode lhe ajudar? Digite "Começar"'
        elif mensagem.lower() in ('n', 'não'):
            return '''Você quer adquirir o Vip? '''
        elif mensagem.lower() in ('comprar'):
          return f'''Digite a da forma de pagamento:{os.linesep}Pix {os.linesep}Cartão{os.linesep}Boleto{os.linesep}'''    
        
        elif mensagem == 'Boleto':
          return '''Atenção no boleto você só terá acesso após 1 a 3 dias úteis
          Clique no Link: https://link.pagar.me/lSkd2N5cdt '''
        elif mensagem == 'Cartão':
          return '''Atenção Faça o pagamento para Link:
          Clique no Link: sem link por enquanto '''   
        elif mensagem == 'Pix':
          return '''Atenção Faça o pagamento para o Pix:
          Clique no Link: https://nubank.com.br/pagar-cobranca/8h7ue/6rLkgj9Zgr 
          '''


        else:
            return 'Como o Bot Vip pode lhe ajudar? Digite "Começar"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()