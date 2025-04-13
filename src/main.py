import argparse
from sweep_run import run_sweep
from train import train
import os
import wandb


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['train', 'sweep'], default='train')
    parser.add_argument('--sweep_id', type=str, help='WandB sweep ID')
    args = parser.parse_args()

    if args.mode == 'train':
        default_config = {
        "batch_size": 64,
        "fc_layer_size": 128,
        "dropout": 0.3,
        "optimizer": "adam",
        "learning_rate": 0.001,
        "epochs": 5
    }
        train(config=default_config)
    elif args.mode == 'sweep':
        if not args.sweep_id:
            raise ValueError("Sweep ID is required in sweep mode.")
        run_sweep(args.sweep_id)
