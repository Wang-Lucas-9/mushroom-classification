import albumentations as A
def augment_image(image):
        transform = A.Compose([
            A.HorizontalFlip(p=0.5),
            A.VerticalFlip(p=0.3),
            A.Rotate(limit=30, p=0.5),
            A.RandomBrightnessContrast(p=0.3),
            A.GaussianBlur(p=0.3),
            A.CoarseDropout(max_holes=8, max_height=8, max_width=8, p=0.3),
        ])
        return transform(image=image)['image']