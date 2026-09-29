import os
import cv2
import numpy as np
import pandas as pd
import time
from google import genai
from sklearn.ensemble import RandomForestClassifier
from gtts import gTTS
from django.conf import settings

# 1. INITIALIZE GEMINI API
API_KEY = os.environ.get("FearKey")
client = genai.Client(api_key=API_KEY) if API_KEY else None

# 2. TRAIN THE BIOMETRIC ML MODEL ON STARTUP
np.random.seed(42)
n_samples = 3000
train_hr, train_focus = (
    np.random.uniform(60, 190, n_samples),
    np.random.uniform(0, 100, n_samples),
)
train_hrv, train_gsr = (
    np.random.uniform(10, 80, n_samples),
    np.random.uniform(1.0, 10.0, n_samples),
)
train_labels = []

for hr, focus, hrv, gsr in zip(train_hr, train_focus, train_hrv, train_gsr):
    intensity = hr - (focus * 0.3) - (hrv * 0.4) + (gsr * 3)
    if intensity < 50:
        train_labels.append(1)
    elif intensity < 75:
        train_labels.append(2)
    elif intensity < 100:
        train_labels.append(3)
    elif intensity < 125:
        train_labels.append(4)
    elif intensity < 150:
        train_labels.append(5)
    elif intensity < 175:
        train_labels.append(6)
    else:
        train_labels.append(7)

X = pd.DataFrame(
    {"HeartRate": train_hr, "Focus": train_focus, "HRV": train_hrv, "GSR": train_gsr}
)
ml_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
ml_classifier.fit(X, np.array(train_labels))

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


class AscendAgent:
    def __init__(self):
        self.ml_model = ml_classifier
        self.client = client

    def analyze_frame(self, frame, previous_fear, last_center):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        raw_fear = previous_fear
        new_center = last_center

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            new_center = (int(x + w // 2), int(y + h // 2))

            if last_center:
                movement = np.sqrt(
                    (new_center[0] - last_center[0]) ** 2
                    + (new_center[1] - last_center[1]) ** 2
                )
                if movement > 10:
                    raw_fear = min(100.0, previous_fear + 8.0)
                else:
                    raw_fear = max(10.0, previous_fear - 3.0)
        else:
            raw_fear = min(100.0, previous_fear + 1.0)

        current_fear_cv = (previous_fear * 0.8) + (raw_fear * 0.2)
        return current_fear_cv, new_center

    def perceive(self, hr, focus, hrv, gsr):
        input_data = pd.DataFrame(
            [[hr, focus, hrv, gsr]], columns=["HeartRate", "Focus", "HRV", "GSR"]
        )
        return self.ml_model.predict(input_data)[0]

    def actuate_override(self, fear_choice, level_choice):
        """Standard synchronous call to avoid Django thread locks"""
        prompt = f"The user's face is showing '{level_choice}' during a {fear_choice} simulation. Write exactly 2 short, empowering sentences to display. Focus on grounding them."
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            script = response.text

            audio_dir = os.path.join(settings.BASE_DIR, "static", "media", "audio")
            os.makedirs(audio_dir, exist_ok=True)
            filename = f"intervention_{int(time.time())}.mp3"
            filepath = os.path.join(audio_dir, filename)

            tts = gTTS(text=script, lang="en", slow=False)
            tts.save(filepath)

            return script, f"/static/media/audio/{filename}"
        except Exception as e:
            print(e)
            return "Breathing protocols engaged. You are safe.", None
