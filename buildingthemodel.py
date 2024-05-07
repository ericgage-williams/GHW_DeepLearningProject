from ultralytics import YOLO
import torch
import os

model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=30)
torch.save(model.state_dict, "./New_model.pt")
