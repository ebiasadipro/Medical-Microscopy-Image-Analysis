import torch
from PIL import Image
from torchvision import transforms


def predict(image_path, model):

    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])

    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)

    model.eval()

    with torch.no_grad():
        output = model(image)

    prediction = torch.argmax(output)

    return prediction.item()


if __name__ == "__main__":
    print("Prediction pipeline ready.")
