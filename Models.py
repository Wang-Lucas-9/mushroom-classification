from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


class ModelFactory:
    """Factory class for creating specific ML models."""

    @staticmethod
    def create_random_forest(n_estimators=100, max_depth=None, random_state=42, **kwargs):
        return RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state, **kwargs)

    @staticmethod
    def create_xgboost(n_estimators=100, learning_rate=0.1, random_state=42, **kwargs):
        return XGBClassifier(n_estimators=n_estimators, learning_rate=learning_rate, random_state=random_state, **kwargs)

    @staticmethod
    def create_lightgbm(n_estimators=100, boosting_type='gbdt', random_state=42, **kwargs):
        return LGBMClassifier(n_estimators=n_estimators, boosting_type=boosting_type, random_state=random_state, **kwargs)

    @staticmethod
    def create_svm(kernel='rbf', C=1.0, **kwargs):
        return SVC(kernel=kernel, C=C, **kwargs)

    @staticmethod
    def create_logistic_regression(max_iter=500, random_state=42, **kwargs):
        return LogisticRegression(max_iter=max_iter, random_state=random_state, **kwargs)

    @staticmethod
    def create_decision_tree(criterion='gini', max_depth=None, random_state=42, **kwargs):
        return DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=random_state, **kwargs)

    @staticmethod
    def create_knn(n_neighbors=5, **kwargs):
        return KNeighborsClassifier(n_neighbors=n_neighbors, **kwargs)
