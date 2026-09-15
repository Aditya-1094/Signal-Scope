import streamlit as st
import tempfile
import os
import hashlib
from pathlib import Path
from PIL import Image

from src.predict import predict_image


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Signal-Scope",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #0e1117;
    }

    /* Main title */
    h1 {
        text-align: center;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #9aa4b2;
        margin-bottom: 2rem;
        font-size: 1.05rem;
    }

    /* Make buttons look cleaner */
    .stButton > button {
        border-radius: 10px;
        height: 3rem;
        font-weight: 600;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: #161b22;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #30363d;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #161b22;
        border-radius: 12px;
        padding: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "current_file_hash" not in st.session_state:
    st.session_state.current_file_hash = None

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "confidence" not in st.session_state:
    st.session_state.confidence = None


# ============================================================
# HEADER
# ============================================================

st.title("🔍 Signal-Scope")

st.markdown(
    '<div class="subtitle">'
    'Telling Real From Synthetic in the Age of Generative Media'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# UPLOAD SECTION
# ============================================================

st.subheader("📤 Upload Image")

uploaded_file = st.file_uploader(
    "Choose an image to analyze",
    type=["jpg", "jpeg", "png", "webp"],
    help="Upload a real or AI-generated image."
)


# ============================================================
# NO IMAGE
# ============================================================

if uploaded_file is None:

    st.info(
        "🔍 **Awaiting Image**\n\n"
        "Upload an image above to begin analysis."
    )

    st.stop()


# ============================================================
# READ IMAGE
# ============================================================

image_bytes = uploaded_file.getvalue()

# Hash the actual image contents.
# This is better than checking only filename because two
# different images can have the same filename.

file_hash = hashlib.sha256(image_bytes).hexdigest()


# ============================================================
# DETECT NEW IMAGE
# ============================================================

if st.session_state.current_file_hash != file_hash:

    # New image selected.
    st.session_state.current_file_hash = file_hash

    # IMPORTANT:
    # Clear the previous prediction immediately.
    st.session_state.prediction = None
    st.session_state.confidence = None


# ============================================================
# IMAGE INFORMATION
# ============================================================

try:

    image = Image.open(
        uploaded_file
    )

    width, height = image.size

    image_format = image.format or "Unknown"

except Exception:

    st.error(
        "Unable to read this image."
    )

    st.stop()


file_size_mb = len(image_bytes) / (1024 * 1024)


# ============================================================
# MAIN TWO-COLUMN UI
# ============================================================

left_column, right_column = st.columns(
    2,
    gap="large"
)


# ============================================================
# LEFT COLUMN — IMAGE
# ============================================================

with left_column:

    with st.container(border=True):

        st.subheader("📷 Current Image")

        st.image(
            image,
            use_container_width=True
        )

        st.caption(
            f"📄 **{uploaded_file.name}**"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Dimensions",
                f"{width} × {height}"
            )

        with col2:
            st.metric(
                "Format",
                image_format
            )

        with col3:
            st.metric(
                "Size",
                f"{file_size_mb:.2f} MB"
            )


# ============================================================
# RIGHT COLUMN — ANALYSIS
# ============================================================

with right_column:

    with st.container(border=True):

        st.subheader("🧠 Analysis")


        # ----------------------------------------------------
        # WAITING FOR ANALYSIS
        # ----------------------------------------------------

        if st.session_state.prediction is None:

            st.info(
                f"**Ready to analyze**\n\n"
                f"Current image: `{uploaded_file.name}`"
            )

            st.write(
                "The image will be analyzed using "
                "Signal-Scope's EfficientNet-B0 model."
            )

            analyze_button = st.button(
                "🔎 Analyze Image",
                use_container_width=True,
                type="primary"
            )


            # ------------------------------------------------
            # START ANALYSIS
            # ------------------------------------------------

            if analyze_button:

                suffix = Path(
                    uploaded_file.name
                ).suffix


                temp_image_path = None

                try:

                    # ----------------------------------------
                    # CREATE TEMPORARY IMAGE
                    # ----------------------------------------

                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=suffix
                    ) as temp_file:

                        temp_file.write(
                            image_bytes
                        )

                        temp_image_path = temp_file.name


                    # ----------------------------------------
                    # MODEL ANALYSIS
                    # ----------------------------------------

                    with st.spinner(
                        f"🔍 Analyzing `{uploaded_file.name}`..."
                    ):

                        prediction, confidence = predict_image(
                            temp_image_path
                        )


                    # ----------------------------------------
                    # SAVE RESULT
                    # ----------------------------------------

                    st.session_state.prediction = prediction
                    st.session_state.confidence = float(
                        confidence
                    )


                except Exception as e:

                    st.error(
                        f"Analysis failed: {e}"
                    )


                finally:

                    # ----------------------------------------
                    # CLEAN TEMP FILE
                    # ----------------------------------------

                    if (
                        temp_image_path is not None
                        and os.path.exists(temp_image_path)
                    ):

                        os.remove(
                            temp_image_path
                        )


                # Refresh UI so result appears cleanly.
                if st.session_state.prediction is not None:
                    st.rerun()


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        else:

            prediction = st.session_state.prediction

            confidence = st.session_state.confidence


            # -----------------------------------------------
            # RESULT HEADER
            # -----------------------------------------------

            st.success(
                "✓ Analysis Complete"
            )

            st.caption(
                f"RESULT FOR: `{uploaded_file.name}`"
            )


            st.divider()


            # -----------------------------------------------
            # PREDICTION
            # -----------------------------------------------

            if prediction == "AI-generated":

                st.error(
                    "🤖 LIKELY AI-GENERATED"
                )

            else:

                st.success(
                    "📷 LIKELY REAL"
                )


            # -----------------------------------------------
            # CONFIDENCE
            # -----------------------------------------------

            st.metric(
                "Model Confidence",
                f"{confidence * 100:.1f}%"
            )

            st.progress(
                min(max(confidence, 0.0), 1.0)
            )


            # -----------------------------------------------
            # INTERPRETATION
            # -----------------------------------------------

            if confidence >= 0.90:

                confidence_text = "Very high confidence"

            elif confidence >= 0.75:

                confidence_text = "High confidence"

            elif confidence >= 0.60:

                confidence_text = "Moderate confidence"

            else:

                confidence_text = "Low confidence"


            st.caption(
                f"● {confidence_text}"
            )


            st.divider()


            # -----------------------------------------------
            # RESPONSIBLE AI MESSAGE
            # -----------------------------------------------

            st.warning(
                "This result represents a model-estimated "
                "likelihood and should not be treated as "
                "definitive proof of an image's origin."
            )


            # -----------------------------------------------
            # ANALYZE AGAIN
            # -----------------------------------------------

            if st.button(
                "↻ Analyze This Image Again",
                use_container_width=True
            ):

                st.session_state.prediction = None
                st.session_state.confidence = None

                st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Signal-Scope • Real vs Synthetic Image Detection"
)