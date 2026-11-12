import streamlit as st
from datetime import datetime

# 1. Web Page Settings (Title aur Icon)
st.set_page_config(page_title="NED Campus Companion", page_icon="🏫", layout="wide")

# App Main Heading
st.title("🏫 NED University Campus Companion")
st.subheader("Your Real-Time Academic & Events Dashboard")
st.markdown("---")

# date process
today = datetime.now()  # Year: 2026, Month: 11, Date: 10
st.sidebar.info(f"📅 Today's Date: {today.strftime('%d %B, %Y')}")

# 2. Academic Dates Data
academic_calendar = {
    "Mid-Term Examination (Fall)": "2026-10-05",
    "End of Teaching (Fall)": "2026-11-27",
    "Commencement of Examinations (Fall)": "2026-11-30",
    "Semester Break": "2026-12-21",
    "Commencement of Classes (Spring)": "2027-01-04"
}

# 3. DSA Extra-Curricular Events Data (From PDF)
dsa_events = [
    {"name": "Rang O Adab", "date": "2026-11-15", "location": "Syed Mehmood Alam Auditorium", "organizer": "TNF"},
    {"name": "Baad e Naubahar Literature Festival", "date": "2026-11-20", "location": "Syed Mehmood Alam Auditorium", "organizer": "LPS"},
    {"name": "MUN (Model United Nation)", "date": "2026-12-10", "location": "NED Premises", "organizer": "NDS"},
    {"name": "TNF FEST", "date": "2027-01-15", "location": "Syed Mehmood Alam Auditorium", "organizer": "TNF"},
    {"name": "Olympiad 6.0", "date": "2027-01-25", "location": "Sports Section & Auditorium", "organizer": "NSA"},
    {"name": "PROXION 2026", "date": "2027-03-10", "location": "Syed Mehmood Alam Auditorium", "organizer": "SENTEC"}
]

# Web page division in two equal Columns 
col1, col2 = st.columns(2)

# --- LEFT COLUMN: Academic Countdowns ---
with col1:
    st.header("📚 Academic Deadlines")
    for event, date_str in academic_calendar.items():
        event_date = datetime.strptime(date_str, "%Y-%m-%d")
        days_left = (event_date - today).days
        
        if days_left >= 0:
            # countdown box 
            st.metric(label=event, value=f"{days_left} Days Left", delta=f"Target: {date_str}")
        else:
            st.error(f"❌ Passed: {event}")

# --- RIGHT COLUMN: Student Society Events ---
with col2:
    st.header("🎪 Upcoming Campus Events")
    for event in dsa_events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        days_left = (event_date - today).days
        
        # Date ko hide kar ke sirf Month aur Year nikalna (e.g., "November 2026")
        event_month_str = event_date.strftime("%B %Y")
        
        if days_left >= 0:
            # Output show official Month 
            st.success(f"**{event['name']}** (Scheduled: {event_month_str})")
            st.caption(f"📍 Location: {event['location']} | 👤 Organized by: {event['organizer']}")
            st.markdown("---")


# ==============================================================================
# --- DO NOT CHANGE ANYTHING ABOVE THIS LINE (Timetable Extension Code) ---
# ================s==============================================================

st.markdown("---")
st.header("📝 Fall Semester Final Exam Tracker (Telecommunications Engg.)")
st.info("⏱️ All exams are scheduled from **09:30 to 12:30 hours** at the **Department of Telecommunications Engg.**")

# finals timetable accurately dictionary mein map kiya 
exam_timetable = {
    "First Year (Batch: 2026)": [
        {"code": "ES-105 / ES-107", "title": "Pakistan Studies / Pakistan Studies (For Foreigners)", "date": "2026-12-02"},
        {"code": "EE-125", "title": "Basic Electrical Engineering", "date": "2026-12-04"},
        {"code": "ES-206 / ES-209", "title": "Islamic Studies / Ethical Behavior", "date": "2026-12-07"},
        {"code": "MT-116", "title": "Calculus & Analytic Geometry", "date": "2026-12-09"},
        {"code": "EF-101", "title": "IT Fundamentals and Application", "date": "2026-12-11"},
        {"code": "EA-128", "title": "Functional English", "date": "2026-12-14"},
        {"code": "CY-100", "title": "Fundamentals of Chemistry", "date": "2026-12-16"}
    ],
    "Second Year (Batch: 2025)": [
        {"code": "TC-205", "title": "Digital Logic Design", "date": "2026-12-03"},
        {"code": "CS-216", "title": "Data Structure & Algorithms", "date": "2026-12-05"},
        {"code": "EL-201", "title": "Electronic Devices & Circuits", "date": "2026-12-08"},
        {"code": "TC-206", "title": "Signals and Systems", "date": "2026-12-10"},
        {"code": "EE-127", "title": "Circuit Analysis", "date": "2026-12-12"}
    ],
    "Third Year (Batch: 2024)": [
        {"code": "EA-304", "title": "Business Communication & Ethics", "date": "2026-12-02"},
        {"code": "EE-374", "title": "Feedback Control Systems", "date": "2026-12-04"},
        {"code": "TC-313", "title": "Antenna & Microwave Engineering", "date": "2026-12-07"},
        {"code": "TC-317", "title": "Artificial Intelligence and Machine Learning", "date": "2026-12-09"},
        {"code": "TC-307", "title": "Communication Systems", "date": "2026-12-11"}
    ],
    "Final Year (Batch: 2023)": [
        {"code": "MT-442", "title": "Numerical Method", "date": "2026-12-03"},
        {"code": "MG-482", "title": "Organizational Behaviour", "date": "2026-12-05"},
        {"code": "CS-430", "title": "Microprocessor Programming and Interfacing", "date": "2026-12-08"},
        {"code": "TC-421", "title": "Telecommunications Network", "date": "2026-12-10"},
        {"code": "TC-422 / TC-428", "title": "Satellite Communications / Communication Security", "date": "2026-12-12"}
    ]
}

# Batch select karne ke liye i add dropdown button 
selected_batch = st.selectbox("Select Your Batch / Year to view Date Sheet:", list(exam_timetable.keys()))

if selected_batch:
    st.subheader(f"📅 Schedule for {selected_batch}")
    
    # 3-column grid 
    exam_cols = st.columns(3)
    
    for idx, exam in enumerate(exam_timetable[selected_batch]):
        exam_date = datetime.strptime(exam["date"], "%Y-%m-%d")
        days_left = (exam_date - today).days
        
        with exam_cols[idx % 3]:
            if days_left >= 0:
                st.success(f"**{exam['code']}**: {exam['title']}\n\n📅 **Date:** {exam['date']} ({days_left} Days Left)")
            else:
                st.error(f"❌ Passed: **{exam['code']}** - {exam['title']}")
