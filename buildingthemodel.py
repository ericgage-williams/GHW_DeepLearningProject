from ultralytics import YOLO
import torch
import os
from IPython.display import display, Image

model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=30)
torch.save(model.state_dict, "new_model.pt")