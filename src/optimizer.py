import torch.optim as optim


def build_optimizer(network, optimizer_name, learning_rate):
    if optimizer_name == "sgd":
        return optim.SGD(network.parameters(), lr=learning_rate, momentum=0.9)
    elif optimizer_name == "adam":
        return optim.Adam(network.parameters(), lr=learning_rate)
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_name}")
