import cv2
import requests
import numpy as np

request = requests.get('https://www.youtube.com/watch?v=eUWslTyT5CU', stream=True)

def get_frame_from_stream(request):
    if(request.status_code == 200):
        bytes_buffer = bytes()
        for chunk in request.iter_content(chunk_size=1024):
            bytes_buffer += chunk
            a = bytes_buffer.find(b'\xff\xd8')
            b = bytes_buffer.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_buffer[a:b + 2]
                bytes_buffer = bytes_buffer[b + 2:]
                img = cv2.imdecode(np.fromstring(
                    jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                return img

    else:
        print("Received unexpected status code {}".format(r.status_code))
        return None

img = get_frame_from_stream(request)
while True:
    if img is not None:
        img = get_frame_from_stream(request)
        cv2.imshow('Live Stream', img)
        cv2.waitKey(0)
    else:
        break
