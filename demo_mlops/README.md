This is Demo Project for MLOps Implementation for On-prem. It uses all the open source platforms like git, DVC, MLFlow etc. 

wine-quality.csv

C:\Users\A622783\OneDrive - Atos\Documents\AIAP\demo-mlops\demo_mlops>python src/get_data.py --config="C:\Users\A622783\OneDrive - Atos\Documents\AIAP\demo-mlops\demo_mlops\params.yaml"

mlflow server --backend-store-uri sqlite:///mydb.sqlite --default-artifact-root .\mlruns

mlflow models serve -m .\mlruns/4/7d15038df0894dc6b6a9811fbc183bfe/artifacts/sklearn-model -h 0.0.0.0 -p 8001

# dvc refernce blog###
https://towardsdatascience.com/the-ultimate-guide-to-building-maintainable-machine-learning-pipelines-using-dvc-a976907b2a1b

# dvc command to repro the pipeline 
dvc repro

# dvc run cmd to create the pipeline #stage 1
dvc run -n load_data  -d src/get_data.py -d src/load_data.py -d data_source/winequality.csv -o data/raw/winequality.csv  python src/load_data.py --config=params.yaml

# dvc run cmd to create the pipeline #stage 2
dvc run -n load_data  -d src/get_data.py -d src/load_data.py -d data_source/winequality.csv -o data/raw/winequality.csv  python src/load_data.py --config=params.yaml


### dvc command to draw the DAG###
dvc dag

### dvc command to show metrics ###

dvc metrics show

### dvc params diff  Commited params vs current parms ###

dvc params diff
