import pandas as pd
data = "./Base_Dados/2.5Consultasrealizadasporespecialidades_maio22aoutubro2022.csv"
df = pd.read_csv(data, usecols=['mes', 'especialidade'])


for coluns in df.columns:
    coluna_mes = df['mes']
    coluna_especialidade = df['especialidade']
    # Escrevendo em uma nova csv
    df.to_csv("./New_Base_1.csv")
    
