import torch.nn as nn

class SymbolClassifierCNN(nn.Module):
    def __init__(self, num_classes):
        super(SymbolClassifierCNN, self).__init__()

        self.pool = nn.MaxPool2d(2, 2)
        self.conv1 = nn.Conv2d(1, 4, 5, padding=1)
        self.conv2 = nn.Conv2d(4, 16, 5, padding=1)
        self.conv3 = nn.Conv2d(16, 32, 5, padding=1)

        self.fc1 = nn.Linear(32 * 17 * 15, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = self.pool(nn.functional.relu(self.conv3(x)))
        x = x.view(x.size(0), -1)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x
