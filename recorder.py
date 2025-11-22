#!/home/juan/venv/bin/python3
import cv2
import time
import os

def record_video(output_directory, duration=10):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Create a unique filename based on the current time
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_directory, f"video_{timestamp}.avi")

    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera, adjust if needed

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))  # Adjust resolution if needed

    print(f"Recording video to: {output_file}")

    start_time = time.time()

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break

        # Write the frame to the output file
        out.write(frame)

    # Release everything when done
    cap.release()
    out.release()

    print("Video recording complete.")

if __name__ == "__main__":
    # Specify the output directory on your external SSD
    external_ssd_directory = "/mnt/external_ssd"

    # Specify the duration of the video recording (in seconds)
    recording_duration = 8 * 60 * 60  # 8 hours

    # Record video
    record_video(external_ssd_directory, duration=recording_duration)
