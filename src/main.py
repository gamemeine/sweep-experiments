import os
import wandb
import yaml

from train import train

# to disable wandb-core
wandb.require("legacy-service")


def create_sweep():
    config_path = os.path.join(os.path.dirname(__file__), "sweep_config.yaml")
    with open(config_path, "r") as f:
        sweep_config = yaml.safe_load(f)

    return wandb.sweep(sweep=sweep_config)


def run_sweep(sweep_id):
    wandb.agent(
        sweep_id=sweep_id,
        function=train,
        count=5,
    )


if __name__ == "__main__":
    sweep_id = create_sweep()
    run_sweep(sweep_id)
