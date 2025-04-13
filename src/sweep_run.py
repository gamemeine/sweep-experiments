import wandb
from train import train


def run_sweep(sweep_id, count=5):
    wandb.agent(sweep_id, train, count=count)
