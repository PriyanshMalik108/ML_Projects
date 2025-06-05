# ML_Projects


🔐**Credit Card Fraud Detection using Machine Learning ( ML P1 )** 

🚀 Project Overview
Built a machine learning model to detect fraudulent credit card transactions using real-world transaction data. The project tackles the challenge of class imbalance and aims to improve fraud detection accuracy using both undersampling and SMOTE-based oversampling techniques.


🔧 Tools & Technologies Used

* 🐍 Python (Google Colab)
* 📊 pandas, NumPy – Data handling & preprocessing
* 🔍 scikit-learn – Model building (Logistic Regression), scaling, evaluation
* ⚖️ imbalanced-learn (SMOTE) – Class balancing
* 📈 Matplotlib / Seaborn (optional for EDA & visualization)

📊 Key Techniques Implemented

* 🧹 Data cleaning (duplicates, unnecessary columns)
* ⚖️ Class balancing using:

  * 🟢 Undersampling (random downsampling of majority class)
  * 🔵 SMOTE (Synthetic Minority Oversampling Technique)
* ⚙️ Feature scaling with StandardScaler
* 🤖 Model training using Logistic Regression
* ✅ Evaluation using accuracy score and class distributions

🌍 Real-World Problem Solved

Credit card fraud causes billions in global losses annually. This project addresses the class imbalance challenge — where fraud cases are rare — and builds a foundation for systems that can proactively detect fraud.

💡 Insights & Impact

* Demonstrated that handling imbalance is crucial to improve model fairness.
* Showed how simple models like Logistic Regression can still provide high interpretability and quick baseline performance.
* The solution is lightweight, fast, and can be integrated into early-stage fraud detection pipelines.


📌 Takeaway
This project blends practical machine learning with real-world applicability, making it a solid base for deploying fraud detection models in financial systems.









**🏦 Loan Approval Prediction System | Machine Learning + Web App (ML P2 )**

🚀 Project Overview
Developed a predictive ML model and deployed it as a simple web app to automate and assist in loan approval decisions. The system uses applicant data to predict loan approval status with high accuracy.

 🛠 Tools & Technologies Used

* 🐍 Python (Google Colab)
* 📊 pandas, NumPy – Data processing & feature engineering
* ⚙️ scikit-learn – Model building, scaling, evaluation
* 🧠 Logistic Regression – Classification algorithm
* 🧼 StandardScaler – Feature normalization
* 💾 Pickle – Model serialization
* 🌐 Basic Web App – UI built using Python with input sliders, buttons, and alerts

📌 What I Did

* 🔄 Cleaned and preprocessed real-world loan application data
* 🏗 Created a new financial feature by aggregating various asset values
* 🧹 Encoded categorical variables (education, self_employed, loan_status) into numerical format
* 📐 Scaled features for improved model performance
* 🤖 Trained a Logistic Regression model on applicant data
* 📈 Predicted loan approval outcomes based on income, CIBIL score, assets, and more
* 💻 Built and deployed a basic interactive UI for real-time prediction

🌍 Real-World Problem Solved

* Automates the manual, subjective loan approval process
* Provides data-driven, consistent decision support for financial institutions
* Reduces processing time, human bias, and inconsistency in approvals

💡 Why It’s Useful

* ✅ Ideal for banks or NBFCs handling large volumes of loan applications
* 🔍 Offers an explainable, rule-based model for better transparency
* 📊 Allows non-technical users to interact with the model easily through the web app

 📈 Outcome

* Built an end-to-end ML pipeline
* Demonstrated full workflow from data cleaning → modeling → deployment
* Created a working prototype ready for further scaling or integration into financial systems



