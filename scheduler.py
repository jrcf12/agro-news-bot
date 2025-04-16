import schedule
import time
import subprocess

def executar_bot():
    subprocess.run(["python", "agro_bot.py"])

# Agendando para rodar a cada 2 horas entre 8h e 18h
schedule.every().day.at("08:00").do(executar_bot)
schedule.every().day.at("10:00").do(executar_bot)
schedule.every().day.at("12:00").do(executar_bot)
schedule.every().day.at("14:00").do(executar_bot)
schedule.every().day.at("16:00").do(executar_bot)
schedule.every().day.at("18:00").do(executar_bot)

while True:
    schedule.run_pending()
    time.sleep(60)
