from torchvision import datasets, transforms
import torch

def build_dataset(batch_size):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    dataset = datasets.MNIST(".", train=True, download=True, transform=transform)
    sub_dataset = torch.utils.data.Subset(dataset, indices=range(0, len(dataset), 5))
    loader = torch.utils.data.DataLoader(sub_dataset, batch_size=batch_size)

    return loader
