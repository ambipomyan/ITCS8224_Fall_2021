from model import MedT
import torch
from torchinfo import summary

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
img_size = 128;
model = MedT(img_size = img_size, imgchan = 3, num_classes=4).to(device)
sizes = [(1, 3, img_size, img_size)]
# sizes = [(1, 4, 240, 240, 160), (1, 4, 120, 120, 80)]
for size in sizes:
    x = torch.randn(size=size, dtype=torch.float32).to(device)
    with torch.no_grad():
        out = model(x)

    print(f'Out: {out.shape}')
    t = summary(model, size)
