import cv2 

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret: # no more frames to read
            break
        frames.append(frame)
    cap.release()
    return frames
    
def save_video(output_video_frames, output_video_path): #to save the video
    fourcc = cv2.VideoWriter_fourcc(*'mJPG') #tells which codec to use and how to compress/encode video
    out = cv2.VideoWriter(output_video_path, fourcc, 24 ,(output_video_frames[0].shape[1], output_video_frames[0].shape[0]))#capture video frame by frame and saving it in the output path
    for frame in output_video_frames:
        out.write(frame)
    out.release


        