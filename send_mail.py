import mysql.connector
import smtplib
import email.message
import schedule
import time


def enviar_email():
    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="senai@134",
        db="bd_medidor"
    )
    
    cursor = conn.cursor()
    query = "SELECT temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro FROM tb_registro"
    cursor.execute(query)
    
    # Obter os dados
    registros = cursor.fetchall()
    cursor.close()
    conn.close()

    #Gerar corpo do email
    temperatura, pressao, altitude, umidade, co2, poeira, tempo_registro = registros[-1]
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
    msg['From'] = 'noreply.ecosystemcall@gmail.com'
    msg['To'] = 'noreply.ecosystemcall@gmail.com'
    password = "ugtfjofbzmglyssy"
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

schedule.every().day.at("20:05").do(enviar_email)
schedule.every().day.at("20:06").do(enviar_email)

while True:
    schedule.run_pending()  
    time.sleep(1)