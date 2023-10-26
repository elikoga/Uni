import numpy as np
import pandas as pd
import sklearn.metrics as metrics
# import numpy.ma as ma

# Confusion Matrix C:
# C[i] # for true Class i: Predictions
# C[i][j] # for true Class i: How many of them were predicted by a model to be in Class j

def matrix_minor(arr, i, j):
    return np.delete(np.delete(arr,i,axis=0), j, axis=1)

class ConfusionMatrix:
    def __init__(self, matrix: np.ndarray, classes=None):
        self.matrix = matrix
        if classes is None:
            classes = [str(i) for i in range(len(matrix))]
        self.classes = classes
    
    @classmethod
    def from_predictions(cls, predictions, labels, classes=None):
        if classes is None:
            classes = np.unique(labels)
        matrix = np.zeros((len(classes), len(classes)), dtype=np.uint)
        for pred, label in zip(predictions, labels):
            matrix[label][pred] += 1
        return cls(matrix, classes)

    def accuracy(self):
        # true_positives = np.sum(np.diag(self.matrix))
        true_positives = self.matrix.trace()
        # total = np.sum(self.matrix)
        total = self.matrix.sum()
        return true_positives / total
    
    def precision(self):
        # true_positives = np.diag(self.matrix)
        true_positives = self.matrix.diagonal()
        # false_positives = np.sum(self.matrix, axis=0) - true_positives
        # true_positives_plus_false_positives = true_positives + false_positives
        # true_positives_plus_false_positives = np.sum(self.matrix, axis=0)
        true_positives_plus_false_positives = self.matrix.sum(axis=0)
        return np.divide(true_positives, true_positives_plus_false_positives, where=true_positives_plus_false_positives != 0)
    
    def recall(self):
        # true_positives = np.diag(self.matrix)
        true_positives = self.matrix.diagonal()
        # false_negatives = np.sum(self.matrix, axis=1) - true_positives
        # true_positives_plus_false_negatives = true_positives + false_negatives
        # true_positives_plus_false_negatives = np.sum(self.matrix, axis=1)
        true_positives_plus_false_negatives = self.matrix.sum(axis=1)
        return np.divide(true_positives, true_positives_plus_false_negatives, where=true_positives_plus_false_negatives != 0)
    
    def f1(self):
        prec = self.precision()
        rec = self.recall()
        prec_plus_rec = prec + rec
        return np.divide(2 * prec * rec, prec_plus_rec, where=prec_plus_rec != 0)
    
    def macro_f1_score_mean_outer(self):
        # return np.mean(self.f1())
        return self.f1().mean()
    
    def macro_f1_score_mean_inner(self):
        # prec = np.mean(self.precision())
        prec = self.precision().mean()
        # rec = np.mean(self.recall())
        rec = self.recall().mean()
        if prec + rec == 0:
            return 0
        return 2 * prec * rec / (prec + rec)
    
    def __str__(self):
        # use pandas to print a nice table
        df = pd.DataFrame(self.matrix, columns=self.classes, index=self.classes)
        return f"Confusion Matrix: Rows are true labels, columns are predicted labels\n{df}"

CLASSES = ["cat", "dog", "bird", "red", "blue"]
def generate_classification_experiment(classes=CLASSES, n=1000000):
    def noisy_classifier(true_label):
        # 70% chance of correct classification
        if np.random.rand() < 0.7:
            return true_label
        # 30% chance of random classification
        return np.random.randint(len(classes))
    true_labels = np.random.randint(len(classes), size=n)
    predicted_labels = np.array([noisy_classifier(i) for i in true_labels])
    print(f"True labels: {true_labels}")
    print(f"Predicted labels: {predicted_labels}")
    return true_labels, predicted_labels

if __name__ == "__main__":
    # arr = np.array([[25, 5, 1], [2, 15, 12], [1, 6, 0]])
    # cm = ConfusionMatrix(arr)

    
    print(f"Creating random classification experiment...")
    true_labels, predicted_labels = generate_classification_experiment()
    print(f"Creating confusion matrix...")
    cm = ConfusionMatrix.from_predictions(predicted_labels, true_labels, CLASSES)
    print(f"Confusion matrix:")
    print(cm)

    print(f"Accuracy: {cm.accuracy()}")
    print(f"Precision: {cm.precision()}")
    print(f"Recall: {cm.recall()}")
    print(f"F1: {cm.f1()}")
    print(f"Macro F1 (mean outer): {cm.macro_f1_score_mean_outer()}")
    print(f"Macro F1 (mean inner): {cm.macro_f1_score_mean_inner()}")

    # make sure that scikit-learn agrees with us
    print(f"Scikit-learn accuracy: {metrics.accuracy_score(true_labels, predicted_labels)}")
    assert np.allclose(cm.accuracy(), metrics.accuracy_score(true_labels, predicted_labels))
    print(f"Scikit-learn precision: {metrics.precision_score(true_labels, predicted_labels, average=None)}")
    assert np.allclose(cm.precision(), metrics.precision_score(true_labels, predicted_labels, average=None))
    print(f"Scikit-learn recall: {metrics.recall_score(true_labels, predicted_labels, average=None)}")
    assert np.allclose(cm.recall(), metrics.recall_score(true_labels, predicted_labels, average=None))
    print(f"Scikit-learn F1: {metrics.f1_score(true_labels, predicted_labels, average=None)}")
    assert np.allclose(cm.f1(), metrics.f1_score(true_labels, predicted_labels, average=None))
    print(f"Scikit-learn macro F1 (mean outer): {metrics.f1_score(true_labels, predicted_labels, average='macro')}")
    assert np.allclose(cm.macro_f1_score_mean_outer(), metrics.f1_score(true_labels, predicted_labels, average='macro'))

    # Pretend you have a highly imbalanced test data of 990 classA
    # examples and only 10 classB examples. You have two systems: Model-One
    # classifies everything as classA and Model-Two throws a coin for each exam-
    # ple and with 50% probability classify the example as classA (and as classB
    # otherwise). Compute all metrics for both systems.

    # model_one_matrix = np.array([[990, 0], [10, 0]])
    # modle_two_matrix = np.array([[495, 495], [5, 5]])
    # model_one = ConfusionMatrix(model_one_matrix)
    # model_two = ConfusionMatrix(modle_two_matrix)
    # print(model_one)
    # print(model_two)
    # print(f"Stats for model one:")
    # print(f"Accuracy: {model_one.accuracy()}")
    # print(f"Precision: {model_one.precision()}")
    # print(f"Recall: {model_one.recall()}")
    # print(f"F1: {model_one.f1()}")
    # print(f"Macro F1 (mean outer correct): {model_one.macro_f1_score_mean_outer()}")
    # print(f"Macro F1 (mean inner): {model_one.macro_f1_score_mean_inner()}")
    # print(f"Stats for model two:")
    # print(f"Accuracy: {model_two.accuracy()}")
    # print(f"Precision: {model_two.precision()}")
    # print(f"Recall: {model_two.recall()}")
    # print(f"F1: {model_two.f1()}")
    # print(f"Macro F1 (mean outer correct): {model_two.macro_f1_score_mean_outer()}")
    # print(f"Macro F1 (mean inner): {model_two.macro_f1_score_mean_inner()}")
