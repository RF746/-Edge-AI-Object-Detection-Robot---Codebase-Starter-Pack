## 🧠 Python Script: `object_detection.py`


```python
import cv2
import numpy as np
import tensorflow as tf
import time


# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="mobilenet_v2.tflite")
interpreter.allocate_tensors()


input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


cap = cv2.VideoCapture(0)


labels = {0: "background", 1: "person", 2: "bicycle", 3: "car"}


while True:
ret, frame = cap.read()
if not ret:
break


input_shape = input_details[0]['shape']
img = cv2.resize(frame, (input_shape[2], input_shape[1]))
input_data = np.expand_dims(img.astype(np.uint8), axis=0)


interpreter.set_tensor(input_details[0]['index'], input_data)
interpreter.invoke()


output_data = interpreter.get_tensor(output_details[0]['index'])
prediction = np.argmax(output_data)


label = labels.get(prediction, "Unknown")
cv2.putText(frame, f"Detected: {label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv2.imshow("Edge AI Robot", frame)


# Optional: Send command over UART to the MCU
# import serial
# ser = serial.Serial('/dev/ttyUSB0', 9600)
# if label == "person":
# ser.write(b"avoid\n")


if cv2.waitKey(1) & 0xFF == ord('q'):
break


cap.release()
cv2.destroyAllWindows()
```


---
