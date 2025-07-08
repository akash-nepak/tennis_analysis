from ultralytics import YOLO

model = YOLO('/home/akash-1/TENNIS_ANALYSIS/training/runs/detect/train4/weights/best.pt')

result = model.track('/home/akash-1/TENNIS_ANALYSIS/input_videos/input_video.mp4',conf = 0.2,save =True)

print(result)

print("boxes:")
for box in result[0].boxes:
    print(box)