import numpy as np
from skfuzzy import control as ctrl
import skfuzzy.defuzzify as defuzz

# Definindo as variáveis linguísticas para os sintomas e doenças
sintomas = ctrl.Antecedent(np.arange(0, 11, 1), 'sintomas')
doenca = ctrl.Consequent(np.arange(0, 101, 1), 'doenca')

# Mapeando as funções de pertinência para os sintomas
sintomas['aumento_sede'] = ctrl.trimf(sintomas.universe, [0, 0, 5])
sintomas['aumento_fome'] = ctrl.trimf(sintomas.universe, [0, 5, 10])
sintomas['perda_peso'] = ctrl.trimf(sintomas.universe, [0, 5, 10])
sintomas['fadiga'] = ctrl.trimf(sintomas.universe, [0, 0, 7])
sintomas['visao_embarcada'] = ctrl.trimf(sintomas.universe, [0, 0, 5])

# Mapeando as funções de pertinência para a doença
doenca['diabetes_tipo_2'] = ctrl.trimf(doenca.universe, [0, 0, 100])

# Regras fuzzy
regra1 = ctrl.Rule(sintomas['aumento_sede'] | sintomas['aumento_fome'] | sintomas['perda_peso'] | sintomas['fadiga'] | sintomas['visao_embarcada'], doenca['diabetes_tipo_2'])

# Sistema de controle
sistema_ctrl = ctrl.ControlSystem([regra1])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Função para inferir a doença com base nos sintomas fornecidos pelo usuário
def inferir_doenca_fuzzy(aumento_sede, aumento_fome, perda_peso, fadiga, visao_embarcada):
    sistema.input['sintomas'] = aumento_sede, aumento_fome, perda_peso, fadiga, visao_embarcada
    sistema.compute()
    return defuzz.centroid(doenca.universe, sistema.output['doenca'])

# Função para interagir com o usuário
def interagir_usuario_fuzzy():
    print("Olá! Como posso ajudar você hoje?")
    print("Por favor, classifique de 0 a 10 a intensidade dos seguintes sintomas:")
    aumento_sede = float(input("Aumento da sede: "))
    aumento_fome = float(input("Aumento da fome: "))
    perda_peso = float(input("Perda de peso: "))
    fadiga = float(input("Fadiga: "))
    visao_embarcada = float(input("Visão embaçada: "))
    
    resultado_fuzzy = inferir_doenca_fuzzy(aumento_sede, aumento_fome, perda_peso, fadiga, visao_embarcada)
    print("Baseado nos sintomas fornecidos, a probabilidade de você ter diabetes tipo 2 é de aproximadamente", resultado_fuzzy, "%.")

# Execução do chatbot fuzzy
interagir_usuario_fuzzy()
