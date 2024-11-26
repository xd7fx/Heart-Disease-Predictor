from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode

class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

import streamlit as st

st.title("Webcam Streamlit App")
st.markdown("This app captures video from your webcam.")

webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]},  # Default STUN server
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False,  # تعطيل الصوت إذا لم يكن مطلوباً
    },
    video_transformer_factory=VideoProcessor,
)
