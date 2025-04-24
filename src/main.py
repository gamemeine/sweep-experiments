import argparse
from sweep_run import run_sweep
import wandb

# to disable wandb-core
wandb.require("legacy-service")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--sweep_id', type=str, required=True, help='WandB sweep ID')
    args = parser.parse_args()

    run_sweep(args.sweep_id)
