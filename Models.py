from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

class ModelFactory:
    """Factory class for creating ML models with customizable hyperparameters."""

    MODEL_MAPPING = {
        'random_forest': (RandomForestClassifier, {
            'n_estimators': 100,  # Số cây trong rừng
            'max_depth': None,  # Độ sâu tối đa của cây
            'random_state': 42
        }),
        'xgboost': (XGBClassifier, {
            'n_estimators': 100,  # Số cây
            'learning_rate': 0.1,  # Tốc độ học
            'random_state': 42
        }),
        'lightgbm': (LGBMClassifier, {
            'n_estimators': 100,  # Số vòng lặp boosting
            'boosting_type': 'gbdt',  # Loại boosting (gbdt, dart, goss)
            'random_state': 42
        }),
        'svm': (SVC, {
            'kernel': 'rbf',  # Kernel sử dụng ('linear', 'poly', 'rbf', 'sigmoid')
            'C': 1.0  # Tham số điều chỉnh độ phạt lỗi
        }),
        'logistic_regression': (LogisticRegression, {
            'max_iter': 500,  # Số vòng lặp tối đa
            'random_state': 42
        }),
        'decision_tree': (DecisionTreeClassifier, {
            'criterion': 'gini',  # 'gini' hoặc 'entropy'
            'max_depth': None,  # Độ sâu tối đa của cây
            'random_state': 42
        }),
        'knn': (KNeighborsClassifier, {
            'n_neighbors': 5  # Số hàng xóm gần nhất
        })
    }

    @staticmethod
    def create_model(model_name, **kwargs):
        """Khởi tạo model với tham số tùy chỉnh."""
        if model_name not in ModelFactory.MODEL_MAPPING:
            raise ValueError(f"Invalid model name: {model_name}. Available models: {list(ModelFactory.MODEL_MAPPING.keys())}")
        
        model_class, default_params = ModelFactory.MODEL_MAPPING[model_name]
        
        # Kết hợp tham số mặc định và tham số do người dùng cung cấp
        model_params = {**default_params, **kwargs}
        return model_class(**model_params)
