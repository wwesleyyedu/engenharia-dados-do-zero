from datetime import datetime


def log(mensagem):
    agora = datetime.now()
    print(f"[{agora}] {mensagem}")
