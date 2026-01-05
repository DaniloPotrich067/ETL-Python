from datetime import datetime
import pandas as pd

#--------------------------------------EXTRACT--------------------------------------#
data = "C:/Users/PC-DANILO/Downloads/ETL Python/Data/people-100.csv"
df = pd.read_csv(data)
#--------------------------------------EXTRACT--------------------------------------#

#--------------------------------------TRANSFORM------------------------------------#
def data_standardization(df):
    df['First Name'] = df['First Name'].str.title()
    df['Last Name'] = df['Last Name'].str.title()
    df['Full Name'] = df['First Name'] + " " + df['Last Name']
    df['Date of birth'] = pd.to_datetime(df['Date of birth'])
    df['Age'] = df['Date of birth'].apply(lambda x: datetime.now().year - x.year)
    df['Sex'] = df['Sex'].map({'Male': 'M', 'Female': 'F'})
    df = df[df['Email'].str.contains('@')]
    return df

stand_df = data_standardization(df)
#--------------------------------------TRANSFORM------------------------------------#

#-------------------------------------LOAD------------------------------------------#
df.to_csv("Data/people_clean.csv", index=False)
print("Transformações aplicadas com sucesso!")
print(df.head())
#-------------------------------------LOAD------------------------------------------#
