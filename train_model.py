import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('data.csv')

le_interest = LabelEncoder()
le_skills = LabelEncoder()
le_edu = LabelEncoder()
le_career = LabelEncoder()

df['interests'] = le_interest.fit_transform(df['interests'])
df['skills'] = le_skills.fit_transform(df['skills'])
df['education_level'] = le_edu.fit_transform(df['education_level'])
df['career'] = le_career.fit_transform(df['career'])

X = df[['interests', 'skills', 'education_level']]
y = df['career']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
joblib.dump(le_interest, 'le_interest.pkl')
joblib.dump(le_skills, 'le_skills.pkl')
joblib.dump(le_edu, 'le_edu.pkl')
joblib.dump(le_career, 'le_career.pkl')
