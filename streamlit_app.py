from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode

# Class for Video Processor
class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

# Streamlit UI
import streamlit as st

st.title("Webcam Streamlit App")
st.markdown("This app captures video from your webcam.")

webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,  # Enables sending and receiving video
    video_transformer_factory=VideoProcessor,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    },
    media_stream_constraints={
        "video": True,  # Force video input
        "audio": False,  # Disable audio input if not needed
    },
)
