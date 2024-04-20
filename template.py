import os
from pathlib import Path
import logging

name = "mlproj"

list_of_file = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    f"src/{name}/components/__init__.py",
    f"src/{name}/components/data_ingestion.py",
    f"src/{name}/components/data_transformation.py",
    f"src/{name}/components/model_trainer.py",
    f"src/{name}/components/model_evaluation.py",
    f"src/{name}/pipeline/__init__.py",
    f"src/{name}/pipeline/data_ingestion_pipeline.py",
    f"src/{name}/pipeline/prdiction_pipeline.py",
    f"src/{name}/pipeline/training_pipeline.py",
    f"src/{name}/utils/utils.py",
    f"src/{name}/utils/__init__.py",
    f"src/{name}/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/expirements.ipynb"

]

for file in list_of_file:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass