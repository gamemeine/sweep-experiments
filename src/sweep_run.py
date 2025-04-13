import wandb
from train import train


def run_sweep(sweep_id):
    wandb.agent(
        sweep_id=sweep_id,
        function=train
    )