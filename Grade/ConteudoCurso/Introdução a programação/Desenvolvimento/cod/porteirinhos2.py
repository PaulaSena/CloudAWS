from datetime import datetime, timedelta
import itertools

# Lista de meninos
participantes = ["Murilo", "Theo", "Miguel", "Guilherme"]

def obter_datas_janeiro_a_dezembro():
    datas = []
    data_atual = datetime(2024, 1, 1)  # Defina a data inicial como 1 de janeiro de 2024

    while data_atual.year == 2024:
        if data_atual.weekday() == 4 or data_atual.weekday() == 6:  # 4 representa sexta-feira, 6 representa domingo
            datas.append(data_atual.strftime("%d/%m/%Y\t%A"))
        
        data_atual += timedelta(days=1)

    return datas

def criar_agenda(participantes, datas):
    agenda = []

    for data in datas:
        data_parts = data.split("\t")
        data_str, dia_da_semana = data_parts[0], data_parts[1]

        manha, noite = itertools.permutations(participantes, 2).__next__()

        evento_manha = {"data": data_str, "dia_da_semana": dia_da_semana, "periodo": "Manhã", "participante": manha}
        evento_noite = {"data": data_str, "dia_da_semana": dia_da_semana, "periodo": "Noite", "participante": noite}

        agenda.extend([evento_manha, evento_noite])

    return agenda

# Teste as funções
datas_sexta_domingo = obter_datas_janeiro_a_dezembro()
agenda = criar_agenda(participantes, datas_sexta_domingo)

for evento in agenda:
    print(f"{evento['data']} ({evento['dia_da_semana']}, {evento['periodo']}): {evento['participante']}")
