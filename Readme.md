# Reproducing mlflow submodule error

This repository is a minimal example to show that `mlflow==1.30.0` does not correctly work with submodules (issue [here](https://github.com/mlflow/mlflow/issues/7241)) and demonstrates the fix (pull request [#7251](https://github.com/mlflow/mlflow/pull/7251))

The repo contains a dummy submodule with a `Readme.md`. The code in `main.py` checks whether the Readme exists and prints the content.

## 1. Scenario: Execution with official mlflow

We setup a mlflow environment in conda
```bash
conda create -n mlflow python=3.8.5
conda activate mlflow
pip install mlflow==1.30.0
```

Now we can run the code using
```bash
mlflow run https://github.com/JojoDevel/ml-flow-with-submodule.git
```

This results in an error as the submodule does not contain the `README.md` file.

```
Is submodule readme available? False
Content: 
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    with open(data_dir) as input_file:
FileNotFoundError: [Errno 2] No such file or directory: 'Dummy-Repo/README.md'
```

## 2. Scenario: Execution iwth fixed mlflow version

We setup a mlflow environment in conda with the fixed mlflow version
```bash
conda create -n mlflow-fixed python=3.8.5
conda activate mlflow-fixed
pip install git+https://github.com/JojoDevel/mlflow.git
```

Now we can run the code using
```bash
mlflow run https://github.com/JojoDevel/ml-flow-with-submodule.git
```

and get the expected output:
```
Is submodule readme available? True
Content: 
# Dummy-Repo
Dummy Repo with just a readme
```