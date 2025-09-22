from PIL import Image
import torch
import timm
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

# Load a pre-trained model
model = timm.create_model('resnet18', pretrained=True)
model.eval()

# Set up image transformation
config = resolve_data_config({}, model=model)
transform = create_transform(**config)

# Load local image
img = Image.open(r"C:\Users\ednai\Downloads\newTest\dog.jpg").convert('RGB')
tensor = transform(img).unsqueeze(0) # transform and add batch dimension

# Run inference
with torch.inference_mode():
    out = model(tensor)
probabilities = torch.nn.functional.softmax(out[0], dim=0)
print(probabilities.shape)
# prints: torch.Size([1000])

# Get imagenet class mappings from local file
# Note: The imagenet_classes.txt file should be in the same directory
try:
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    print(f"Loaded {len(categories)} ImageNet categories from local file")
except FileNotFoundError:
    print("imagenet_classes.txt not found. Please ensure the file is in the current directory.")
    # Fallback to sample categories
    categories = [f"class_{i}" for i in range(1000)]

# Print top categories per image
top5_prob, top5_catid = torch.topk(probabilities, 5)
for i in range(top5_prob.size(0)):
    print(categories[top5_catid[i]], top5_prob[i].item())
# prints class names and probabilities like:
# [('Samoyed', 0.6425196528434753), ('Pomeranian', 0.04062102362513542), ('keeshond', 0.03186424449086189), ('white wolf', 0.01739676296710968), ('Eskimo dog', 0.011717947199940681)]