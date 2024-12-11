from sqlalchemy import create_engine
import pandas as pd
import smtplib
import email.message
import schedule
import time


def enviar_email():
    # Conectar ao banco de dados
    engine1 = create_engine('mysql://root:senai%40134@127.0.0.1/bd_medidoreliane')
    engine2 = create_engine('mysql://root:senai%40134@127.0.0.1/bd_medidor')

    #query a ser requisitada
    query_dados = "SELECT * FROM tb_registro"
    query_users = "SELECT email FROM tb_usuario"

    # Use pandas para ler os dados do banco de dados
    dados = pd.read_sql(query_dados, engine1)
    usuarios = pd.read_sql(query_users, engine2)
    
    #transforma dados
    tempo_registro = dados["tempo_registro"].tail(1)
    temperatura = dados["temperatura"].tail(1)
    pressao = dados["pressao"].tail(1)
    altitude = dados["altitude"].tail(1)
    umidade = dados["umidade"].tail(1)
    co2 = dados["co2"].tail(1)
    poeira = dados["poeira"].tail(1)
    
    users = ""
    for _, row in usuarios.iterrows():
        user = ",".join(map(str, row))  # Converte cada elemento para string e junta com vírgulas
        users += user + ", "
    
    print(users)
    #Gerar corpo do email
    corpo_email = f"""
    <p>Data: {tempo_registro}</p>
    <ul>
        <li>Temperatura: {temperatura} °C</li>
        <li>Pressão: {pressao} Pa</li>
        <li>Altitude: {altitude} m</li>
        <li>Umidade: {umidade} %</li>
        <li>CO2: {co2} ppm</li>
        <li>Poeira: {poeira} µg/m³</li>
    </ul>
    <hr>
    """
    #Envio do email
    msg = email.message.Message()
    msg['Subject'] = "Indicadores de Sensores"
    msg['From'] = 'projetosenai.cd24@gmail.com'
    msg['To'] = users
    password = "cdol xorh tmlf inpz"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'].split(','), msg.as_string().encode('utf-8'))
    s.quit()
    print("Email enviado")


if __name__ == "__main__":
    enviar_email()

schedule.every().day.at("21:57").do(enviar_email)
schedule.every().day.at("20:06").do(enviar_email)

while True:
    schedule.run_pending()  
    time.sleep(1)