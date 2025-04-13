# sweep-experiments

## Setup

To get started with the project, follow these steps:

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install local version of `wandb`:
    ```bash
    pip install -e /path/to/local/wandb
    ```

Voila! You are ready to go!

## Running a sweep
1. Define parameters you want to measure during training in sweep_config.yaml

2. Load your config:
    ```bash
    wandb sweep sweep_config.yaml
    ```
3. Run the app:
     ```bash
    python main.py --sweep_id <username>/<project_name>/<sweep_id>
    ```
