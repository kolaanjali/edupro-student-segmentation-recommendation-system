
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

st.set_page_config(
    page_title="EduPro Intelligence System",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    path = "EduPro Online Platform.xlsx"

    users = pd.read_excel(path, sheet_name="Users")
    courses = pd.read_excel(path, sheet_name="Courses")
    transactions = pd.read_excel(path, sheet_name="Transactions")

    df = transactions.merge(users, on="UserID")
    df = df.merge(courses, on="CourseID")

    return users, courses, transactions, df

users, courses, transactions, df = load_data()

st.title("🎓 EduPro Student Segmentation & Recommendation System")

st.markdown("### Personalized Learning Intelligence Dashboard")

# Feature Engineering
learner_profiles = df.groupby("UserID").agg({
    "CourseID": "count",
    "Amount": "mean",
    "CourseRating": "mean",
    "CourseCategory": pd.Series.nunique,
    "Age": "first"
}).reset_index()

learner_profiles.columns = [
    "UserID",
    "TotalCourses",
    "AvgSpend",
    "AvgRating",
    "DiversityScore",
    "Age"
]

features = learner_profiles[
    ["TotalCourses", "AvgSpend", "AvgRating", "DiversityScore", "Age"]
]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=42)
learner_profiles["Cluster"] = kmeans.fit_predict(scaled_features)

score = silhouette_score(scaled_features, learner_profiles["Cluster"])

segment_names = {
    0: "Explorers",
    1: "Career Builders",
    2: "Specialists",
    3: "Premium Learners"
}

st.sidebar.header("Navigation")

selected_user = st.sidebar.selectbox(
    "Select Learner",
    learner_profiles["UserID"]
)

profile = learner_profiles[
    learner_profiles["UserID"] == selected_user
].iloc[0]

cluster = int(profile["Cluster"])

st.success(f"Assigned Segment: {segment_names[cluster]}")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Courses Enrolled", int(profile["TotalCourses"]))
col2.metric("Average Spending", f"${round(profile['AvgSpend'],2)}")
col3.metric("Average Rating", round(profile["AvgRating"],2))
col4.metric("Diversity Score", int(profile["DiversityScore"]))

st.subheader("Cluster Quality")
st.info(f"Silhouette Score: {round(score,3)}")

cluster_counts = learner_profiles["Cluster"].value_counts().reset_index()
cluster_counts.columns = ["Cluster", "Count"]

cluster_counts["Segment"] = cluster_counts["Cluster"].map(segment_names)

fig = px.bar(
    cluster_counts,
    x="Segment",
    y="Count",
    title="Learner Segment Distribution",
    text="Count"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Cluster Visualization")

pca_df = learner_profiles.copy()

fig2 = px.scatter(
    pca_df,
    x="TotalCourses",
    y="AvgSpend",
    color=pca_df["Cluster"].astype(str),
    hover_data=["UserID"],
    title="Learner Cluster Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Recommended Courses")

cluster_users = learner_profiles[
    learner_profiles["Cluster"] == cluster
]["UserID"]

cluster_df = df[df["UserID"].isin(cluster_users)]

recommendations = (
    cluster_df.groupby(
        ["CourseName", "CourseCategory"]
    )["CourseRating"]
    .mean()
    .reset_index()
    .sort_values(by="CourseRating", ascending=False)
    .head(5)
)

st.dataframe(recommendations)

st.subheader("Segment Insights")

st.markdown("""
- **Explorers** → Try multiple domains and categories  
- **Career Builders** → Prefer practical and certification-oriented learning  
- **Specialists** → Deeply focused in one subject area  
- **Premium Learners** → Spend more on advanced learning experiences  
""")

st.subheader("Platform Statistics")

c1, c2, c3 = st.columns(3)

c1.metric("Total Learners", users.shape[0])
c2.metric("Total Courses", courses.shape[0])
c3.metric("Total Transactions", transactions.shape[0])
