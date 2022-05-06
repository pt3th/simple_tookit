'''
ref: https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
'''
from sim_utils.utils import *
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from skimage import io, transform
import cv2

class CustomDataset(Dataset):

    def __init__(self, dataset_info, transform=None):
        self.dataset_info = dataset_info
        self.transform = transform

    def __len__(self):
        return len(self.dataset_info)

    def __getitem__(self, idx):
        record_idx = self.dataset_info[idx]
        img_name = record_idx['img_name']
        image = io.imread(img_name)

        if self.transform:
            image = self.transform(image)

        annotations = record_idx["annotations"]
        return image, annotations


if __name__ == "__main__":
    data_transform = transforms.Compose([
        # transforms.RandomSizedCrop(224),
        # transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    dataset_info = "put the dataset info here"
    custom_dataset = CarlaSegmentationDataset(dataset_info, transform=data_transform)
    dataset_loader = torch.utils.data.DataLoader(custom_dataset, batch_size=8, shuffle=True, num_workers=4)
    
    #iterate over batchs
    for i, inputs in enumerate(dataset_loader):
        images, annotations = inputs[0], inputs[1]
        
        #model output
        #model loss
        #optimization
        #...




