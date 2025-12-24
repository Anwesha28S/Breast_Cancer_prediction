
# Breast Cancer Prediction Web App

## Overview

This is a **Flask-based web application** for predicting whether a breast tumor is **benign or malignant** using the **Wisconsin Breast Cancer (Diagnostic) dataset**.

---

## Dataset Description

The Wisconsin Breast Cancer (Diagnostic) dataset contains **569 samples** with **30 numerical features** derived from fine needle aspirate (FNA) images of breast masses.

Each sample includes measurements describing **cell nuclei characteristics**, such as radius, area, perimeter, and concavity.
The dataset’s **target variable** indicates whether the tumor is **benign (B)** or **malignant (M)**.

### Key Attributes

| Attribute                | Description                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mean Concave Points**  | Average number of concave portions (inward curves) of the nucleus. Higher values indicate irregular shapes, often associated with malignancy. |
| **Worst Concave Points** | Maximum number of concave points in the most irregular cell. Strong indicator of malignancy.                                                  |
| **Worst Radius**         | Maximum distance from the center to the nucleus boundary. Malignant cells usually have larger and more variable nuclei.                       |
| **Worst Area**           | Largest nucleus area measured. Indicates abnormal cell growth.                                                                                |
| **Worst Perimeter**      | Maximum perimeter length, showing irregularity of cell shape.                                                                                 |



## Trained Models

| Model Name                   |
| ---------------------------- |
| Support Vector Machine (SVM) |
| K-Nearest Neighbors (KNN)    |
| Decision Tree                |
| Logistic Regression          |
| XGBoost                      |
| Random Forest                |

---

## Best-Fitted Model

* **Random Forest**
* **Accuracy:** 96.49% (on test data)
* **Recall Score:** 96%

---

## Live App

[Visit the app here](https://breast-cancer-prediction-2-6lre.onrender.com)


