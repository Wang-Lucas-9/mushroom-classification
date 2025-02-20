import cv2
import numpy as np

class Feature_Extractor_Factory:


    @staticmethod #Static method giúp có thể gọi trực tiếp hàm này mà ko cần tạo object
    # Hàm trích xuất histogram màu từ ảnh - Các tham số có thể điều chỉnh: bins
    def extract_color_histogram(image, bins=(8, 8, 8)): 
        hist_lab = cv2.calcHist([cv2.cvtColor(image, cv2.COLOR_BGR2LAB)], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        hist_hsv = cv2.calcHist([cv2.cvtColor(image, cv2.COLOR_BGR2HSV)], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        hist_bgr = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        
        cv2.normalize(hist_lab, hist_lab)
        cv2.normalize(hist_hsv, hist_hsv)
        cv2.normalize(hist_bgr, hist_bgr)
        
        return np.hstack([hist_lab.flatten(), hist_hsv.flatten(), hist_bgr.flatten()])
    

    @staticmethod
    #Hàm trích xuất các đặc trưng về contour từ ảnh - Các tham số có thể điều chỉnh: None
    def extract_contour_features(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return np.zeros(3, dtype=np.float32), image  # Trả về ảnh gốc nếu không có contour
        
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]  # Giữ lại tối đa 5 contour lớn nhất
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, contours, -1, 255, thickness=cv2.FILLED)
        segmented_image = cv2.bitwise_and(image, image, mask=mask)
        
        areas = [cv2.contourArea(c) for c in contours]
        perimeters = [cv2.arcLength(c, True) for c in contours]
        
        return np.array([sum(areas), sum(perimeters), len(contours)], dtype=np.float32), segmented_image
    

    @staticmethod
    #Hàm trích xuất các đặc trưng về hu_moments từ ảnh - Các tham số có thể điều chỉnh: None
    def extract_hu_moments(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        moments = cv2.moments(gray)
        hu_moments = cv2.HuMoments(moments).flatten()
        return -np.sign(hu_moments) * np.log10(np.abs(hu_moments) + 1e-10)
    
    @staticmethod
    def extract_feature(method,image, **kwargs):
        
        methods={
            'color_histogram':Feature_Extractor_Factory.extract_color_histogram,
            'contour_features':Feature_Extractor_Factory.extract_contour_features,
            'hu_moments':Feature_Extractor_Factory.extract_hu_moments
        }
        if method not in methods:
            raise ValueError(f"Invalid method: {method}")
        return methods[method](image, **kwargs)
