import streamlit as st
from datetime import datetime, timedelta
import random

# ------------------ Streamlit Configuration ------------------
st.set_page_config(page_title="📊 Gamification Dashboard", layout="wide")
st.title("📊 Gamification Dashboard")

# ------------------ Fake Data ------------------
# Simulating the number of minutes studied and user's interests.
fake_user_data = {
    "username": "Chere Praneetha",
    "email": "cheriepraneetha265@gmail.com",
    "interests": ["AI", "ML", "Data Science", "Deep Learning", "Reinforcement Learning"],
    "login_dates": [datetime.now() - timedelta(days=i) for i in range(7)]  # Last 7 days of logins
}

# Simulated study time in minutes (for each of the last 7 days)
study_time_data = [random.randint(30, 90) for _ in range(7)]  # Minutes of learning

# ------------------ Gamification Functions ------------------

def calculate_points(minutes_logged, interests_count):
    return (minutes_logged * 2) + (interests_count * 10)

def determine_level(points):
    levels = {
        0: "Beginner",
        100: "Intermediate",
        250: "Advanced",
        500: "Master"
    }
    for threshold, level in sorted(levels.items(), reverse=True):
        if points >= threshold:
            return level
    return "Beginner"

def get_badges(minutes, interests):
    badges = []
    if minutes >= 100:
        badges.append("🔥 100+ Mins")
    if len(interests) >= 5:
        badges.append("🏆 Curiosity Champ")
    if len(interests) >= 7:
        badges.append("🚀 Knowledge Seeker")
    return badges

def calculate_streak(login_dates):
    login_dates = sorted(set(login_dates), reverse=True)
    today = datetime.now().date()
    streak = 0
    for i in range(len(login_dates)):
        if login_dates[i].date() == today - timedelta(days=streak):
            streak += 1
        else:
            break
    return streak

# ------------------ Gamification Summary ------------------

def gamification_summary():
    total_time = sum(study_time_data)
    points = calculate_points(total_time, len(fake_user_data["interests"]))
    level = determine_level(points)
    badges = get_badges(total_time, fake_user_data["interests"])
    streak = calculate_streak(fake_user_data["login_dates"])

    summary = {
        "username": fake_user_data["username"],
        "points": points,
        "level": level,
        "badges": badges,
        "streak": streak,
        "total_time": total_time
    }

    return summary

# ------------------ Fetch Gamification Data ------------------
results = gamification_summary()

# ------------------ Display Results ------------------
if results:
    st.subheader(f"🎓 Welcome, {results['username']}!")
    st.metric("🏅 Total Points Earned", results['points'])
    st.metric("🎓 Learning Level", results['level'])

    # Display Badges Earned
    if results['badges']:
        st.write("🏅 Badges Earned:")
        for badge in results['badges']:
            st.success(badge)
    else:
        st.write("🏅 No badges earned yet! Keep going!")

    # Display Learning Streak
    st.metric("🎯 Learning Streak", f"{results['streak']} days in a row")

    # Display Total Study Time
    st.metric("🕒 Total Study Time", f"{results['total_time']} minutes")

    # ------------------ Visualize Progress ------------------
    # Create a bar chart for daily study time over the last 7 days
    study_days = [f"Day {i+1}" for i in range(7)]
    study_times = study_time_data

    st.subheader("📈 Daily Study Time")
    st.bar_chart(dict(zip(study_days, study_times)))

    # ------------------ Streak Progress Visualization ------------------
    st.subheader("🔥 Learning Streak Progress")
    st.progress(results['streak'] / 7)  # Show progress bar for the streak out of 7 days
else:
    st.error("🚫 No data available. Please check the backend.")
