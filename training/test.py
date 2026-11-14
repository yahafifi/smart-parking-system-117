from ultralytics import YOLO

model = YOLO('yolo26n.pt')

for i, layer in enumerate(model.model.model):
    print(
        f'layer: {i}',
        f'{layer.__class__.__name__}',
        f'From = {layer.f}'
    )