import os
from pathlib import Path
import logging

logging.basicConfig (level=logging.INFO)

project_name = "mlproject"

list_of_files= [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "app.py",

]

for file_path in list_of_files:
    file_dir, file_name = os.path.split(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir}")
    else:
        logging.info(f"Creating file: {file_name}")
    
    with open(file_path, 'w') as f:
        pass  # Create an empty file
        logging.info(f"Created file: {file_path}")
