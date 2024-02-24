# This code creates a program to record video from the built-in camera and simultaneously record
# and transform audio to create a dramatic voice changer.
# The result is a video file in which the video is accompanied by a modified audio accompaniment,
# with a shifted timbre to achieve a specific voice effect (for example, a female voice)
# Task
# 1. Read the video
# 2. Take a video from the camera and save it to a file
# 3. Read the sound as a separate file
# 4. Change the sound. For example, switch to bass or speak to others voice
# 5. Overlay this transformed sound on the video.
# 6. Make the first slide - performed by the IT-41 group student Mykola L. Ivanov.
# 7. At the end of the date, “Thank you for your attention

import cv2
import pyaudio
import wave
import moviepy.editor as mp
import threading
import os
from pydub import AudioSegment
import numpy as np

# Global variables for thread control
recording = True
audioRecording = True
output_file = "output_file.avi"
output_tex = "test"


# Function to create a slide with text using OpenCV
def create_slide(text, is_thank_you=False):
    # Create a black image
    img = np.zeros((480, 640, 3), dtype=np.uint8)

    # Add text to the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_thickness = 2

    if is_thank_you:
        font_color = (0, 255, 0)  # Green color for "Thank you" slide
        font_size = 1
    else:
        font_color = (0, 0, 255)  # Red color for the initial slide
        font_size = 1.5  # Larger font size for the initial slide

    lines = text.split('\n')
    y_offset = 0
    for line in lines:
        text_size = cv2.getTextSize(line, font, font_size, font_thickness)[0]
        text_position = ((img.shape[1] - text_size[0]) // 2, int((img.shape[0] + text_size[1]) // 2 + y_offset))
        cv2.putText(img, line, text_position, font, font_size, font_color, font_thickness)
        y_offset += text_size[1] + 5  # Adjust for spacing between lines

    return img


# Function to transform audio (change pitch, speed, etc.)
def transform_audio(audio_path):
    sound = AudioSegment.from_file(audio_path)

    # Decrease pitch by 3 semitones for a Darth Vader-like voice
    pitch_shift_semitones = -3
    transformed_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * (2 ** (pitch_shift_semitones / 12.0)))
    })

    transformed_audio_path = "transformed_audio.wav"
    transformed_sound.export(transformed_audio_path, format="wav")

    return transformed_audio_path


# Function to apply red filter to the frame
def apply_red_filter(frame):
    red_filter = np.zeros_like(frame)
    red_filter[:, :, 2] = frame[:, :, 2]  # Keep only the red channel, set others to 0
    return red_filter


# Function to record and transform audio
def record_and_transform_audio():
    global audioRecording, recording
    audio_format = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    chunk = 1024
    audio_filename = 'audio.wav'

    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=chunk)
    frames = []
    while audioRecording:
        audio_data = stream.read(chunk)
        frames.append(audio_data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(audio_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    # Apply voice transformation
    transformed_audio_path = transform_audio(audio_filename)

    return transformed_audio_path


# Record and transform audio thread
audio_thread = threading.Thread(target=record_and_transform_audio)
audio_thread.start()

# Create initial slide
first_slide_text = "Performed by a student of IT-33\nKaskiv Volodymyr"
first_slide_img = create_slide(first_slide_text, is_thank_you=False)


# Record video function
def record_video():
    global recording, output_file, audioRecording
    cap = cv2.VideoCapture(0)  # 0 - вбудована камера

    if not cap.isOpened():
        print("Помилка: не вдалося відкрити камеру.")
        recording = False
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    if not out.isOpened():
        print("Помилка: не вдалося відкрити вихідний відеофайл.")
        recording, audioRecording = False, False
        return

    # Introduce a delay before starting video recording
    video_start_delay = 5  # Specify the desired delay in seconds
    cv2.waitKey(video_start_delay * 1000)  # Convert seconds to milliseconds

    # Add the initial slide to the video with a longer duration
    initial_slide_duration = 100  # Specify the desired duration in frames
    for _ in range(initial_slide_duration):
        out.write(first_slide_img)

    while recording:
        ret, frame = cap.read()
        if not ret:
            break

        # Apply red filter to the frame
        filtered_frame = apply_red_filter(frame)

        out.write(filtered_frame)
        cv2.imshow('Video Recording', filtered_frame)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:
            recording, audioRecording = False, False
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Start recording video thread
video_thread = threading.Thread(target=record_video)
video_thread.start()

# Wait for the threads to finish
video_thread.join()
audio_thread.join()

# Create the "Thank you" slide
last_slide_text = "Thank you"
last_slide_img = create_slide(last_slide_text, is_thank_you=True)

# Replace the last frame in the output video with the "Thank you" slide
video_clip = mp.VideoFileClip(output_file)
last_frame_time = video_clip.duration  # Append the "Thank you" slide at the end

# Create an ImageClip from the "Thank you" slide
last_slide_clip = mp.ImageClip(last_slide_img, duration=last_frame_time)

# Overlay the "Thank you" slide at the end of the video
final_clip = mp.concatenate_videoclips([video_clip, last_slide_clip])

# Continue with the rest of the code
audio_clip = mp.AudioFileClip('transformed_audio.wav')
final_clip = final_clip.set_audio(audio_clip)
final_output = output_tex + ".mp4"
final_clip.write_videofile(final_output, codec='libx264', audio_codec='aac')

# Display paths to output files
current_directory = os.getcwd()
output_file_path = os.path.join(current_directory, output_file)
final_output_path = os.path.join(current_directory, final_output)

print("Шлях до вихідного відеофайлу:", output_file_path)
print("Шлях до фінального відеофайлу:", final_output_path)

