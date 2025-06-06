import os
import wandb
import yaml

from train import train

# to disable wandb-core
wandb.require("legacy-service")


def create_sweep(sweep_config=None):
    if sweep_config is None:
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

    sweep_config = {
        "method": "grid",
        "metric": {"name": "loss", "goal": "minimize", "summary": "minimize"},
        "parameters": {
            "batch_size": {"values": [32]},
            "fc_layer_size": {"values": [64, 128, 256]},
            "dropout": {"values": [0.1]},
            "optimizer": {"values": ["adam", "sgd"]}
        }
    }

    sweep_id = create_sweep()
    # sweep_id = create_sweep(sweep_config)
    run_sweep(sweep_id)
