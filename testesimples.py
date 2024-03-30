# Base de Conhecimento
base_conhecimento = {
    "diabetes_tipo_2": {
        "sintomas": ["aumento da sede", "aumento da fome", "perda de peso inexplicada", "fadiga", "visão embaçada"],
        "fatores_risco": ["obesidade", "sedentarismo", "histórico familiar"]
    },
    # Adicione mais doenças e informações conforme necessário
}

# Função para inferir a doença com base nos sintomas fornecidos pelo usuário
def inferir_doenca(sintomas):
    doencas_possiveis = []
    for doenca, info in base_conhecimento.items():
        sintomas_doenca = info["sintomas"]
        if all(sintoma in sintomas for sintoma in sintomas_doenca):
            doencas_possiveis.append(doenca)
    return doencas_possiveis

# Função para interagir com o usuário
def interagir_usuario():
    print("Olá! Como posso ajudar você hoje?")
    print("Por favor, liste os sintomas que está experimentando, separados por vírgulas.")
    sintomas_usuario = input().lower().split(", ")
    doencas_diagnosticadas = inferir_doenca(sintomas_usuario)
    if doencas_diagnosticadas:
        print("Com base nos sintomas fornecidos, parece que você pode estar sofrendo de:")
        for doenca in doencas_diagnosticadas:
            print("- " + doenca)
            print("Diabetes tipo 2 é uma condição crônica na qual o corpo não produz insulina suficiente ou não consegue usar adequadamente a insulina que produz. ")
        print(" Um possível tratamento seria insulina, dieta e exercícios, mas recomendo que você consulte um médico para um diagnóstico preciso e tratamento adequado.")
    else:
        print("Não foi possível identificar uma doença com base nos sintomas fornecidos.")
        print("Recomendo que você consulte um médico para uma avaliação mais detalhada.")

# Execução do chatbot
interagir_usuario()
