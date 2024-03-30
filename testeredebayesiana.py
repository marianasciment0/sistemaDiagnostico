from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Inicialização do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Função para pré-processamento de texto
def preprocess_text(text):
    # Tokenização
    tokens = word_tokenize(text)
    # Remoção de stopwords
    stop_words = set(stopwords.words('portuguese'))  # Alteração para stopwords em português
    tokens = [word for word in tokens if word.lower() not in stop_words]
    # Lematização
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Função para diagnóstico
def diagnose(symptoms):
    # Definição da rede bayesiana
    model = BayesianNetwork([('Polydipsia', 'Diabetes'), ('Polyphagia', 'Diabetes'), ('Polyuria', 'Diabetes')])
    cpd_polydipsia = TabularCPD(variable='Polydipsia', variable_card=2, values=[[0.7], [0.3]])
    cpd_polyphagia = TabularCPD(variable='Polyphagia', variable_card=2, values=[[0.6], [0.4]])
    cpd_polyuria = TabularCPD(variable='Polyuria', variable_card=2, values=[[0.8], [0.2]])
    cpd_diabetes = TabularCPD(variable='Diabetes', variable_card=2, 
                               evidence=['Polydipsia', 'Polyphagia', 'Polyuria'], 
                               values=[[0.9, 0.6, 0.7, 0.2, 0.3, 0.4, 0.1, 0.8], 
                                       [0.1, 0.4, 0.3, 0.8, 0.7, 0.6, 0.9, 0.2]], 
                               evidence_card=[2, 2, 2])
    model.add_cpds(cpd_polydipsia, cpd_polyphagia, cpd_polyuria, cpd_diabetes)
    
    # Inferência na rede bayesiana
    infer = VariableElimination(model)
    query_result = infer.query(variables=['Diabetes'], evidence={'Polydipsia': symptoms['Polydipsia'], 
                                                                 'Polyphagia': symptoms['Polyphagia'], 
                                                                 'Polyuria': symptoms['Polyuria']})
    # Retornar o diagnóstico
    return query_result

# Função principal do chatbot
def main():
    print("Bem-vindo ao Chatbot de Diagnóstico de Diabetes!")
    print("Por favor, forneça algumas informações sobre seus sintomas.")

    # Coletar informações do usuário
    polydipsia = input("Você está sentindo mais sede? (sim/não): ").lower()
    polyphagia = input("Você está sentindo mais fome? (sim/não): ").lower()
    polyuria = input("Você está urinando com mais frequência? (sim/não): ").lower()

    # Pré-processamento de sintomas
    symptoms = {
        'Polydipsia': 1 if polydipsia == 'sim' else 0,
        'Polyphagia': 1 if polyphagia == 'sim' else 0,
        'Polyuria': 1 if polyuria == 'sim' else 0
    }

    # Realizar o diagnóstico
    result = diagnose(symptoms)

    # Exibir o diagnóstico para o usuário
    print("\nCom base nos sintomas fornecidos, o diagnóstico mais provável é:")
    print("Diabetes: {:.0f}%".format(result.values[1] * 100))
    print("Não Diabetes: {:.0f}%".format(result.values[0] * 100))

if __name__ == "__main__":
    main()
