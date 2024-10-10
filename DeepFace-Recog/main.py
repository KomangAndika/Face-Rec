from deepface import DeepFace
import json

result = DeepFace.verify(img1_path="/Users/komangandikawirasantosa/Face-Rec/DeepFace-Recog/Photos/Barron.png",img2_path="/Users/komangandikawirasantosa/Face-Rec/DeepFace-Recog/Photos/TrumpMew1.png")
print(json.dumps(result,indent=2))