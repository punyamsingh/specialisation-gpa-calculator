import streamlit as st

# Mapping grades to points
grade_points = {
    "A": 10, "A-": 9, "B": 8, "B-": 7, "C": 6, "C-": 5, "D": 4, "F": 0
}

# Streamlit app layout
st.title("Specialization CGPA Calculator 📊")

# Explanation Section
st.markdown("""
### How CGPA is Calculated?
1. Each grade has a point value per credit (e.g., **A = 10**, **A- = 9**, etc.).
2. Multiply grade points by course credits to get **Earned Points**.
3. Assume A (10 points) for each course to get **Maximum Possible Points**.
4. **CGPA Formula**:  
\[
   \text{CGPA} = \left( \frac{\text{Total Earned Points}}{\text{Total Max Points}} \right) \times 10
\]
""")

# Course Input Form
st.subheader("Enter Your Courses")
num_courses = st.number_input("Number of Courses", min_value=1, max_value=10, step=1, value=3)

courses = []
earned_points = 0
max_points = 0

with st.form("cgpa_form"):
    for i in range(num_courses):
        col1, col2, col3 = st.columns(3)
        with col1:
            course_name = st.text_input(f"Course {i+1} Name", f"Course {i+1}")
        with col2:
            credits = st.number_input(f"Credits for {course_name}", min_value=1, max_value=10, step=1, value=3)
        with col3:
            grade = st.selectbox(f"Grade for {course_name}", list(grade_points.keys()))

        # Store details
        courses.append((course_name, credits, grade))
        earned_points += grade_points[grade] * credits
        max_points += 10 * credits  # Assuming A (10 points) is max

    # Submit Button
    submitted = st.form_submit_button("Calculate CGPA")

# Display results
if submitted:
    cgpa = (earned_points / max_points) * 10
    st.subheader("Results 📈")
    st.write(f"**Total Earned Points:** {earned_points}")
    st.write(f"**Total Maximum Points:** {max_points}")
    st.write(f"**Calculated CGPA:** `{cgpa:.2f}`")
