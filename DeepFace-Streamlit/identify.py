from deepface import DeepFace
from PIL import Image
import io

class Identify:
    def __init__(self):
        # You can set any model you prefer in DeepFace or use the default one
        self.model_name = "VGG-Face"  # Default model (You can also use "Facenet", "OpenFace", "DeepFace")

    def identify_face(self, uploaded_file):
        try:
            # Load the uploaded image into memory
            image = Image.open(uploaded_file)
            image_bytes = io.BytesIO()
            image.save(image_bytes, format="JPEG")

            # Convert image to a format suitable for DeepFace
            image_bytes.seek(0)
            
            # Perform face recognition (you can provide a database of faces for comparison)
            result = DeepFace.analyze(img_path=image_bytes, actions=['emotion', 'age', 'gender'])

            # Return the identified results (can be customized based on needs)
            return result['dominant_emotion'], result['age'], result['gender']
        except Exception as e:
            print(f"Error: {e}")
            return None
