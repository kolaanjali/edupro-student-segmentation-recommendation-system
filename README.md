# 🎓 EduPro Student Segmentation & Personalized Course Recommendation System

## 📌 Project Overview

This project focuses on building a student-centric personalization engine for EduPro using Machine Learning and Data Analytics techniques.

The system analyzes learner behavior, segments students into meaningful groups, and generates personalized course recommendations to improve learner engagement, retention, and learning experience.

---

# 🚀 Features

✅ Learner Segmentation using K-Means Clustering
✅ Personalized Course Recommendation Engine
✅ Interactive Streamlit Dashboard
✅ Learner Profile Explorer
✅ Cluster Visualization & Insights
✅ Segment Comparison Analytics
✅ Recommendation Intelligence

---

# 📊 Dataset Information

The project uses the **EduPro Online Platform Dataset** containing:

### Users Sheet

* UserID
* Age
* Gender

### Courses Sheet

* CourseID
* CourseName
* CourseCategory
* CourseType
* CourseLevel
* CourseRating

### Transactions Sheet

* UserID
* CourseID
* TransactionDate
* Amount

---

# 🧠 Machine Learning Workflow

## 1. Data Preprocessing

* Data Cleaning
* Missing Value Handling
* Dataset Merging
* Feature Engineering

## 2. Feature Engineering

Generated learner-level behavioral features:

* Total Courses Enrolled
* Average Spending
* Average Course Rating
* Diversity Score
* Enrollment Patterns

## 3. Learner Segmentation

Applied:

* K-Means Clustering
* StandardScaler
* Silhouette Score Evaluation

## 4. Recommendation System

Cluster-aware recommendations using:

* Course popularity
* Rating-based relevance
* Similar learner behavior

---

# 📈 Dashboard Features

### 🎯 Learner Profile Explorer

* View learner metrics
* Assigned cluster
* Spending patterns

### 📊 Cluster Analytics

* Learner segment distribution
* Cluster visualization
* Behavioral insights

### 📚 Recommendation Engine

* Personalized course recommendations
* Cluster-based suggestions

### 📌 Platform Statistics

* Total learners
* Total courses
* Transaction insights

---

# 🛠️ Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Development          |
| Pandas       | Data Processing           |
| Scikit-learn | Machine Learning          |
| Plotly       | Interactive Visualization |
| Streamlit    | Web Application           |
| OpenPyXL     | Excel File Handling       |

---

# 📂 Project Structure

```plaintext
EduPro_Final_Project/
│
├── data/
│   └── EduPro Online Platform.xlsx
│
├── reports/
│   └── executive_summary.md
│
├── app.py
├── requirements.txt
├── README.md
```

---

# ▶️ Run Locally

## Step 1 — Install Requirements

```bash
pip install -r requirements.txt
```

## Step 2 — Run Streamlit App

```bash
streamlit run app.py
```

---

# ☁️ Deployment

This project can be deployed easily using:

* Streamlit Cloud
* GitHub

---

# 📌 Key Outcomes

✔ Learner behavior analysis
✔ Personalized learning intelligence
✔ Cluster-based student segmentation
✔ Adaptive recommendation system
✔ Interactive analytics dashboard

---

# 👩‍💻 Author

Anjali Kola
B.Tech CSE Student | Data Analytics Enthusiast
