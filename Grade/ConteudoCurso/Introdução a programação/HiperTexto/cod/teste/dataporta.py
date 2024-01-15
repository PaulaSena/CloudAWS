from datetime import datetime, timedelta

def obter_datas_janeiro_a_dezembro():
    datas = []
    data_atual = datetime(2024, 1, 1)  # Defina a data inicial como 1 de janeiro de 2024

    while data_atual.year == 2024:
        if data_atual.weekday() == 4 or data_atual.weekday() == 6:  # 4 representa sexta-feira, 6 representa domingo
            datas.append(data_atual.strftime("%d/%m/%Y\t%A"))
        
        data_atual += timedelta(days=1)

    return datas

# Teste a função
datas_sexta_domingo = obter_datas_janeiro_a_dezembro()

for data in datas_sexta_domingo:
    print(data)
