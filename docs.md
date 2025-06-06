# WandB Sweep Configuration: New `metric.summary` Options

This document describes the newly added `metric.summary` values—`last`, `maximize`, and `minimize`—which return the global last value, maximum value, or minimum value of a metric in summary. Use these options to control how WandB evaluates and reports metrics during sweeps.

## 1. Introduction

In WandB sweeps, the `metric.summary` field specifies how to aggregate a metric across an entire run. Previously, common options included aggregation methods such as `mean`, `median`, etc. We have introduced three new summary modes:

- `last`: Returns the final (most recent) value of the metric at the end of the run. It is the default behavior.
- `maximize`: Returns the global maximum value observed for the metric throughout the run.
- `minimize`: Returns the global minimum value observed for the metric throughout the run.

These additions give you greater flexibility when defining optimization targets for your hyperparameter sweeps (e.g., optimizing based on the best validation accuracy seen, rather than the last reported one).

## 2. Configuration Schema

Below is the minimal YAML schema for defining a sweep with the new `metric.summary` modes. You can include these new summary types under the `project`, `method`, and `metric` sections as usual.

```yaml
method: bayes

metric:
  name: <METRIC_NAME>
  goal: maximize|minimize
  summary: last|maximize|minimize

parameters:
  learning_rate:
    min: 0.0001
    max: 0.1
  batch_size:
    values: [32, 64, 128]
```

The JSON equivalent of the above YAML configuration would look like this:

```json
{
  "method": "bayes",
  "metric": {
    "name": "<METRIC_NAME>",
    "goal": "maximize|minimize",
    "summary": "last|maximize|minimize"
  },
  "parameters": {
    "learning_rate": {
      "min": 0.0001,
      "max": 0.1
    },
    "batch_size": {
      "values": [32, 64, 128]
    }
  }
}
```