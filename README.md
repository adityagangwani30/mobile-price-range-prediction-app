# Mobile Price Prediction App 📱

A web application built with Flask that predicts the price range of a mobile phone based on its specifications. This project uses a Random Forest model trained on the Mobile Price Classification dataset from Kaggle.

## ✨ Live Demo

You can view and interact with the live application here:

* **[Live Demo](https://mobile-price-range-prediction-app.onrender.com)**

---

## 🛠️ Technologies Used

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Deployment:** Render

---

## ⚙️ How to Run This Project Locally

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/adityagangwani30/mobile-price-range-prediction-app.git](https://github.com/adityagangwani30/mobile-price-range-prediction-app.git)
    ```
2.  **Navigate to the project directory**
    ```sh
    cd mobile-price-range-prediction-app
    ```
3.  **Install the required packages**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the Flask application**
    ```sh
    python app.py
    ```
5.  Open your web browser and go to `http://127.0.0.1:5000/`

---

## 📂 Project Structure
| File / Folder | Description |
|---|---|
| `app.py` | The main Flask application script. |
| `model.joblib` | The pre-trained machine learning model. |
| `model.ipynb` | Jupyter Notebook for model training and evaluation. |
| `requirements.txt` | List of required Python packages for deployment. |
| `train.csv` | The training dataset. |
| `test.csv` | The test dataset for final predictions. |
| `.gitignore` | Specifies which files and folders for Git to ignore. |
| `README.md` | The project's documentation file. |
| `templates/` | Folder containing all HTML templates. |
| `└── index.html` | The HTML template for the main user interface. |

## 📊 Dataset

This project uses the "Mobile Price Classification" dataset, which contains various mobile phone specifications and their associated price range. The price range is categorized into four classes:

* **0:** Low Cost
* **1:** Medium Cost
* **2:** High Cost
* **3:** Very High Cost

* **Link to Dataset:** [https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)
