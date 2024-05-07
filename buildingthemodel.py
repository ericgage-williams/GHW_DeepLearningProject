from ultralytics import YOLO
import torch
import os

model = YOLO("yolov8m.pt")
model.train(data="data.yaml", epochs=30)
<<<<<<< HEAD
torch.save(model.state_dict, "./New_model.pt")
=======
torch.save(model.state_dict, "new_model.pt")
>>>>>>> 773b212225a72906bd4f865c3d3f791b18140f2e
