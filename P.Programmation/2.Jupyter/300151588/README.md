# 2.Jupyter - 300150564

## Installation réalisée

- Chocolatey installé
- Miniforge3 installé
- Conda initialisé avec conda init powershell
- Environnement INF1093 créé (Python 3.12)
- JupyterLab installé via conda-forge

## Commandes utilisées

choco install miniforge3 -y
conda init powershell
conda create -n INF1093 python=3.12 -y
conda activate INF1093
conda install -c conda-forge jupyterlab -y
jupyter lab

## Vérification

conda --version
python --version
jupyter --version
