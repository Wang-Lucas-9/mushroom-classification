import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from Features_Ex import Feature_Extractor_Factory
class DataLoader:
    def __init__(self, dataset_path, feature_extractors):
        """
        dataset_path: Đường dẫn đến tập dữ liệu (chứa các thư mục con, mỗi thư mục là một loại nấm).
        feature_extractors: List các hàm trích xuất đặc trưng (có thể chọn nhiều phương pháp).
        """
        self.dataset_path = dataset_path
        self.feature_extractors = feature_extractors  
        self.label_encoder = LabelEncoder()  

    def load_data(self, test_size=0.2, random_state=42):
        X, y = [], []
        labels = []

        for class_folder in os.listdir(self.dataset_path):
            class_path = os.path.join(self.dataset_path, class_folder)
            if os.path.isdir(class_path):
                labels.append(class_folder)  # Lưu lại tên lớp

                for image_file in os.listdir(class_path):
                    image_path = os.path.join(class_path, image_file)
                    image = cv2.imread(image_path)

                    if image is None:
                        continue  

                    # Kết hợp nhiều đặc trưng
                    features = np.hstack([Feature_Extractor_Factory.extract_feature(extractor,image) for extractor in self.feature_extractors])
                    X.append(features)
                    y.append(class_folder)  # Nhãn là tên thư mục con

        # Chuyển nhãn từ tên thư mục thành số nguyên
        y = self.label_encoder.fit_transform(y)
        
        X = np.array(X)
        y = np.array(y)

        return train_test_split(X, y, test_size=test_size, random_state=random_state), self.label_encoder
