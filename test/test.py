import requests

API_URL = "http://localhost:8888/upscale/"
IMAGE_PATH = "ivy_plant.jpg"  # Replace with the path to your test PNG image
SCALE_FACTOR = 2

def test_api():
    with open(IMAGE_PATH, "rb") as image_file:
        files = {"file": ("ivy_plant.png", image_file, "image/png")}
        params = {"scale_factor": SCALE_FACTOR}
        
        response = requests.post(API_URL, files=files, params=params)

        if response.status_code == 200:
            with open("upscaled_api_image.png", "wb") as out_file:
                out_file.write(response.content)
            print("Upscaled image saved as 'upscaled_api_image.png'")
        else:
            print(f"Failed to upscale image: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_api()