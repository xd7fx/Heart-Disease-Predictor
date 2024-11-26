import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration
import cv2
import numpy as np
import av

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        # تحميل نموذج الكشف عن الوجه
        self.face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def recv(self, frame):
        try:
            # تحويل الإطار إلى صيغة BGR
            img = frame.to_ndarray(format="bgr24")

            # تحويل الصورة إلى تدرج الرمادي للتعرف على الوجه
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

            # رسم مستطيلات حول الوجوه المكتشفة
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # إعادة الصورة إلى صيغة RGB للعرض
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return av.VideoFrame.from_ndarray(img, format="rgb24")
        
        except Exception as e:
            print(f"Error: {e}")
            return frame

# إعداد Streamlit
st.title("Webcam Real-Time Face Detection")
st.markdown("This app detects faces in real-time using your webcam.")

# إعداد WebRTC
webrtc_streamer(
    key="example",
    video_processor_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
)
