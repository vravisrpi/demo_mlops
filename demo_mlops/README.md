This is Demo Project for MLOps Implementation for On-prem. It uses all the open source platforms like git, DVC, MLFlow etc. 

wine-quality.csv

C:\Users\A622783\OneDrive - Atos\Documents\AIAP\demo-mlops\demo_mlops>python src/get_data.py --config="C:\Users\A622783\OneDrive - Atos\Documents\AIAP\demo-mlops\demo_mlops\params.yaml"

mlflow server --backend-store-uri sqlite:///mydb.sqlite --default-artifact-root .\mlruns

mlflow models serve -m .\mlruns/4/7d15038df0894dc6b6a9811fbc183bfe/artifacts/sklearn-model -h 0.0.0.0 -p 8001
