import streamlit as st
from identify import Identify  # Import the Identify class

st.set_page_config(page_title="Face Recog App", page_icon=":mahjong:")

def main():
    st.title("Face Recog App")
    st.divider()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Process the image
        st.write("Identifying the face...")

        # Instantiate the Identify class and run the identification
        identify = Identify()
        result = identify.identify_face(uploaded_file)

        # Show the result of identification
        if result:
            st.success(f"Face identified: {result}")
        else:
            st.error("No match found or an error occurred.")
        
if __name__ == "__main__":
    main()
