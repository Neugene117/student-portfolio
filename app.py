import streamlit as st
import json
from pathlib import Path
import base64
import datetime
from PIL import Image
import io
import shutil
import os
import pickle

# Configure page settings
st.set_page_config(page_title="My Portfolio", layout="wide", page_icon="👨‍🎓")

# Add constants for data storage
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
PROFILE_DATA_FILE = DATA_DIR / "profile_data.pkl"

# Update session state initialization
if 'profile' not in st.session_state:
    # Try to load existing profile data
    if PROFILE_DATA_FILE.exists():
        try:
            with open(PROFILE_DATA_FILE, 'rb') as f:
                st.session_state.profile = pickle.load(f)
        except Exception:
            # Use default profile if loading fails
            st.session_state.profile = {
                "name": "NDAYISHIMIYE EUGENE",
                "title": "Software Engineer & Technology Enthusiast",
                "location": "Rubavu District, Western Province",
                "university": "INES Ruhengeli",
                "field": "Software Engineering",
                "bio": """Software engineering student passionate about technology and innovation. 
                I believe in creating inclusive technology solutions and stand against inequality in tech. 
                Currently focusing on developing automated systems and AI applications.""",
                "skills": {
                    "Python": 85,
                    "JavaScript": 80,
                    "PHP": 75,
                    "C#": 70,
                    "C++": 65,
                    "SQL": 80,
                    "HTML/CSS": 85,
                    "Machine Learning": 70
                },
                "projects": [
                    {
                        "title": "Face Recognition Attendance System",
                        "year": "Year 1",
                        "type": "Individual",
                        "description": "Automated attendance system using facial recognition, eliminating manual roll calls.",
                        "technologies": ["JavaScript", "PHP", "Face Recognition API"],
                        "github": "https://github.com/Neugene117/face-recognition-attendance"
                    },
                    {
                        "title": "Online Ticket Booking System",
                        "year": "Year 2",
                        "type": "Individual",
                        "description": "Digital platform for booking and managing tickets with real-time availability.",
                        "technologies": ["PHP", "MySQL", "JavaScript"],
                        "github": "https://github.com/Neugene117/ticket-booking"
                    },
                    {
                        "title": "Automatic Timetable Generator",
                        "year": "Year 3",
                        "type": "Current Project",
                        "description": "AI-powered system for generating optimal class schedules and reports.",
                        "technologies": ["Python", "Machine Learning", "SQL"],
                        "github": "https://github.com/Neugene117/auto-timetable"
                    }
                ],
                "social_links": {
                    "linkedin": "https://www.linkedin.com/feed/?legoTrackingToken=c34ZpnFFkTBxr71PqmgCc2UMfmlOrSdjtOoZsC5gr6litOoZp6Zdr6litOoVejAVejRApnhPpnlNpl9JtmUCjAZ9l4BjjR0Zuk9OpmhOjThBpShFtOpQrClQrCBvsClHpmlPnS9LqBYOtChxs6xzrDlxr3RAinhBpShFtOoMfmVLqnhFsSZgt6lDp6BT9z0Kc3RBsCZzkT9D9zROol1Ipl9OpOoZp6Zdr6lisCsCc3RKrSBQqndLk71RrT9D9zAVejAVfmhBt7dBtn5BkCRRjD1RrT9D9DhItm5CpmgZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DhKpnhKqjRAinhLr7cCt6NRompBp3RAinhRrTBxr2oOtChxs6xzrDlxr3RBrm5epmtxs2pEt7tLsCsZp4BMs64Cdj0VdjwOfmh9rCZFsT9BtyoRdPgTdPgPdz0Nfmh9tipBejoRcmdzoClydmkJozwToyQUe3oQbmkUcCoJpztzpjAUcPgZp4BQu6lQrCZz",
                    "github": "https://github.com/Neugene117/"
                },
                "education": {
                    "degree": "A2 Certificate",
                    "status": "Completed"
                },
                "timeline": [
                    {
                        "year": "2021",
                        "event": "First Year Project",
                        "description": "Developed Face Recognition Attendance System",
                        "icon": "✅"
                    },
                    {
                        "year": "2022",
                        "event": "Second Year Project",
                        "description": "Created Online Ticket Booking System",
                        "icon": "🎯"
                    },
                    {
                        "year": "2023",
                        "event": "Current Project",
                        "description": "Developing Automatic Timetable Generator",
                        "icon": "💻"
                    }
                ],
                "testimonials": [
                    {
                        "text": "Eugene demonstrates exceptional problem-solving skills in software development.",
                        "author": "Dr. Jean Paul",
                        "role": "Project Supervisor"
                    },
                    {
                        "text": "Great team player with strong technical capabilities.",
                        "author": "Marie Claire",
                        "role": "Course Instructor"
                    }
                ],
                "image": None  # Add image field to profile
            }
    else:
        st.session_state.profile = {
            "name": "NDAYISHIMIYE EUGENE",
            "title": "Software Engineer & Technology Enthusiast",
            "location": "Rubavu District, Western Province",
            "university": "INES Ruhengeli",
            "field": "Software Engineering",
            "bio": """Software engineering student passionate about technology and innovation. 
            I believe in creating inclusive technology solutions and stand against inequality in tech. 
            Currently focusing on developing automated systems and AI applications.""",
            "skills": {
                "Python": 85,
                "JavaScript": 80,
                "PHP": 75,
                "C#": 70,
                "C++": 65,
                "SQL": 80,
                "HTML/CSS": 85,
                "Machine Learning": 70
            },
            "projects": [
                {
                    "title": "Face Recognition Attendance System",
                    "year": "Year 1",
                    "type": "Individual",
                    "description": "Automated attendance system using facial recognition, eliminating manual roll calls.",
                    "technologies": ["JavaScript", "PHP", "Face Recognition API"],
                    "github": "https://github.com/Neugene117/face-recognition-attendance"
                },
                {
                    "title": "Online Ticket Booking System",
                    "year": "Year 2",
                    "type": "Individual",
                    "description": "Digital platform for booking and managing tickets with real-time availability.",
                    "technologies": ["PHP", "MySQL", "JavaScript"],
                    "github": "https://github.com/Neugene117/ticket-booking"
                },
                {
                    "title": "Automatic Timetable Generator",
                    "year": "Year 3",
                    "type": "Current Project",
                    "description": "AI-powered system for generating optimal class schedules and reports.",
                    "technologies": ["Python", "Machine Learning", "SQL"],
                    "github": "https://github.com/Neugene117/auto-timetable"
                }
            ],
            "social_links": {
                "linkedin": "https://www.linkedin.com/feed/?legoTrackingToken=c34ZpnFFkTBxr71PqmgCc2UMfmlOrSdjtOoZsC5gr6litOoZp6Zdr6litOoVejAVejRApnhPpnlNpl9JtmUCjAZ9l4BjjR0Zuk9OpmhOjThBpShFtOpQrClQrCBvsClHpmlPnS9LqBYOtChxs6xzrDlxr3RAinhBpShFtOoMfmVLqnhFsSZgt6lDp6BT9z0Kc3RBsCZzkT9D9zROol1Ipl9OpOoZp6Zdr6lisCsCc3RKrSBQqndLk71RrT9D9zAVejAVfmhBt7dBtn5BkCRRjD1RrT9D9DhItm5CpmgZp4BMtmZOpOpejQBkildfk3RVgD9Bp79L9DhItm5CpmgZp4BQrClJpSlP9DhKpnhKqjRAinhLr7cCt6NRompBp3RAinhRrTBxr2oOtChxs6xzrDlxr3RBrm5epmtxs2pEt7tLsCsZp4BMs64Cdj0VdjwOfmh9rCZFsT9BtyoRdPgTdPgPdz0Nfmh9tipBejoRcmdzoClydmkJozwToyQUe3oQbmkUcCoJpztzpjAUcPgZp4BQu6lQrCZz",
                "github": "https://github.com/Neugene117/"
            },
            "education": {
                "degree": "A2 Certificate",
                "status": "Completed"
            },
            "timeline": [
                {
                    "year": "2021",
                    "event": "First Year Project",
                    "description": "Developed Face Recognition Attendance System",
                    "icon": "✅"
                },
                {
                    "year": "2022",
                    "event": "Second Year Project",
                    "description": "Created Online Ticket Booking System",
                    "icon": "🎯"
                },
                {
                    "year": "2023",
                    "event": "Current Project",
                    "description": "Developing Automatic Timetable Generator",
                    "icon": "💻"
                }
            ],
            "testimonials": [
                {
                    "text": "Eugene demonstrates exceptional problem-solving skills in software development.",
                    "author": "Dr. Jean Paul",
                    "role": "Project Supervisor"
                },
                {
                    "text": "Great team player with strong technical capabilities.",
                    "author": "Marie Claire",
                    "role": "Course Instructor"
                }
            ],
            "image": None  # Add image field to profile
        }

UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_profile_data():
    """Save profile data to disk"""
    try:
        with open(PROFILE_DATA_FILE, 'wb') as f:
            pickle.dump(st.session_state.profile, f)
    except Exception as e:
        st.error(f"Error saving profile data: {str(e)}")

def save_uploaded_image(uploaded_file):
    """Save uploaded image and return the saved path"""
    try:
        # Create unique filename using timestamp
        file_ext = Path(uploaded_file.name).suffix.lower()
        filename = f"profile_pic_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}{file_ext}"
        save_path = UPLOAD_DIR / filename
        
        # Save the file
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Remove old profile picture if exists
        if "image_path" in st.session_state.profile and Path(st.session_state.profile["image_path"]).exists():
            try:
                os.remove(st.session_state.profile["image_path"])
            except Exception:
                pass
        
        return str(save_path)
    except Exception as e:
        st.error(f"Error saving image: {str(e)}")
        return None

def load_css():
    css = """
        <style>
            /* Main theme colors */
            :root {
                --primary-color: #4CAF50;
                --secondary-color: #2196F3;
                --background-color: #f8f9fa;
                --text-color: #212529;
            }
            
            .main-header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 2rem;
                border-radius: 10px;
                color: white;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            .card {
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                margin-bottom: 1rem;
                transition: transform 0.2s;
            }
            
            .card:hover {
                transform: translateY(-5px);
            }
            
            .skill-bar {
                height: 10px;
                background: #e9ecef;
                border-radius: 5px;
                margin-bottom: 1rem;
            }
            
            .profile-image {
                border-radius: 50%;
                border: 4px solid white;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            
            .button-primary {
                background-color: var(--primary-color);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                transition: background-color 0.2s;
            }
            
            .button-primary:hover {
                background-color: #388E3C;
            }
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Go to",
        ["Home", "Projects", "Skills & Achievements", "Customize Profile", "Contact"]
    )

    if page == "Home":
        display_home()
    elif page == "Projects":
        display_projects()
    elif page == "Skills & Achievements":
        display_skills()
    elif page == "Customize Profile":
        customize_profile()
    else:
        display_contact()

def display_home():
    # Hero section
    st.markdown("""
        <div class="main-header">
            <h1 style="font-size: 3.5rem; font-weight: 700; margin-bottom: 1rem;">
                Hello, I'm Eugene 👋
            </h1>
            <p style="font-size: 1.5rem; opacity: 0.9;">
                Turning Ideas into Reality through Code
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Profile section
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="card profile-card">', unsafe_allow_html=True)
        # Simplified image display logic
        try:
            if "image_path" in st.session_state.profile and Path(st.session_state.profile["image_path"]).exists():
                # Open and display image using PIL
                image = Image.open(st.session_state.profile["image_path"])
                st.image(image, use_container_width=True)
            else:
                st.markdown("""
                    <div class="default-avatar">
                        👤
                    </div>
                """, unsafe_allow_html=True)
            
            # Quick Info
            st.markdown("""
                <div style="text-align: center; margin-top: 1rem;">
                    <h3>Quick Info</h3>
                    <p>📍 Based in Kigali, Rwanda</p>
                    <p>💻 Software Developer</p>
                    <p>🎓 Computer Science Student</p>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error displaying profile: {str(e)}")
            st.markdown("""
                <div class="default-avatar">
                    👤
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # About Me
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
            <h2 style="color: var(--primary-color); margin-bottom: 1rem;">About Me</h2>
        """, unsafe_allow_html=True)
        st.write(st.session_state.profile["bio"])
        
        # Education
        st.markdown("""
            <h3 style="color: var(--secondary-color); margin-top: 1.5rem;">Education</h3>
        """, unsafe_allow_html=True)
        st.write(f"🎓 {st.session_state.profile['university']}")
        st.write(f"📚 {st.session_state.profile['field']}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Timeline Section
    st.markdown('<div class="section-header"><h2>My Journey</h2></div>', unsafe_allow_html=True)
    for item in st.session_state.profile["timeline"]:
        st.markdown(f"""
            <div class="timeline-item fade-in">
                <div class="timeline-icon">{item['icon']}</div>
                <div class="timeline-content">
                    <h3>{item['year']} - {item['event']}</h3>
                    <p>{item['description']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Testimonials Section
    st.markdown('<div class="section-header"><h2>What Others Say</h2></div>', unsafe_allow_html=True)
    cols = st.columns(len(st.session_state.profile["testimonials"]))
    for col, testimonial in zip(cols, st.session_state.profile["testimonials"]):
        with col:
            st.markdown(f"""
                <div class="testimonial-card fade-in">
                    <p class="quote">"{testimonial['text']}"</p>
                    <p class="author">- {testimonial['author']}</p>
                    <p class="role">{testimonial['role']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # Resume Section
    st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
    resume_path = Path("resume.pdf")
    if resume_path.exists():
        try:
            with open(resume_path, "rb") as file:
                st.markdown("""
                    <h3 style="color: var(--primary-color);">Want to know more?</h3>
                    <p style="margin-bottom: 1rem;">Download my resume to see my full qualifications</p>
                """, unsafe_allow_html=True)
                btn = st.download_button(
                    label="📄 Download Resume",
                    data=file,
                    file_name="Eugene_NDAYISHIMIYE_Resume.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error("Error loading resume file")
    st.markdown('</div>', unsafe_allow_html=True)

def display_projects():
    st.markdown("""
        <div class="main-header project-header">
            <h1>My Projects</h1>
            <p>A showcase of my technical journey and innovations</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Updated project filtering
    filter_cols = st.columns([2, 1, 1])
    with filter_cols[0]:
        project_type = st.multiselect(
            "Filter by Type",
            ["Individual", "Group", "Current Project"]
        )
    with filter_cols[1]:
        project_year = st.selectbox(
            "Academic Year",
            ["All Years", "Year 1", "Year 2", "Year 3"]
        )
    
    # Display projects with enhanced cards
    for project in st.session_state.profile["projects"]:
        if (not project_type or project["type"] in project_type) and \
           (project_year == "All Years" or project_year == project["year"]):
            st.markdown(f"""
                <div class="project-card fade-in">
                    <div class="project-header">
                        <h3>{project['title']}</h3>
                        <span class="project-year">{project['year']}</span>
                    </div>
                    <div class="project-type-badge">{project['type']}</div>
                    <p class="project-description">{project['description']}</p>
                    <div class="tech-stack">
                        {' '.join([f'<span class="tech-tag">{tech}</span>' for tech in project['technologies']])}
                    </div>
                    <a href="{project['github']}" target="_blank" class="github-link">
                        <i class="fab fa-github"></i> View Project
                    </a>
                </div>
            """, unsafe_allow_html=True)

def display_skills():
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("Skills & Achievements")
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Technical Skills")
        for skill, level in st.session_state.profile["skills"].items():
            st.write(f"{skill}")
            st.progress(level/100)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Certifications")
        st.write("• AWS Certified Cloud Practitioner")
        st.write("• Google Data Analytics Professional Certificate")
        st.markdown('</div>', unsafe_allow_html=True)

def customize_profile():
    st.title("Customize Profile")
    
    # Image upload section with preview
    st.subheader("Profile Picture")
    uploaded_file = st.file_uploader("Choose a profile picture", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        try:
            # Display preview
            image = Image.open(uploaded_file)
            preview_col, button_col = st.columns([2, 1])
            with preview_col:
                st.image(image, caption="Preview", use_container_width=True)
            with button_col:
                if st.button("✅ Confirm & Save", use_container_width=True):
                    saved_path = save_uploaded_image(uploaded_file)
                    if saved_path:
                        st.session_state.profile["image_path"] = saved_path
                        save_profile_data()  # Save profile data after updating
                        st.success("Profile picture updated!")
                        st.rerun()
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
    
    # Show current profile picture if exists
    elif "image_path" in st.session_state.profile and Path(st.session_state.profile["image_path"]).exists():
        st.image(st.session_state.profile["image_path"], caption="Current Profile Picture", use_container_width=True)
        if st.button("🗑️ Remove Picture", use_container_width=True):
            try:
                os.remove(st.session_state.profile["image_path"])
                del st.session_state.profile["image_path"]
                st.success("Profile picture removed!")
                st.rerun()  # Updated from experimental_rerun()
            except Exception as e:
                st.error(f"Error removing image: {str(e)}")

    new_name = st.text_input("Name", st.session_state.profile["name"])
    new_location = st.text_input("Location", st.session_state.profile["location"])
    new_university = st.text_input("University", st.session_state.profile["university"])
    new_field = st.text_input("Field of Study", st.session_state.profile["field"])
    new_bio = st.text_area("Bio", st.session_state.profile["bio"])
    
    if st.button("Save Changes"):
        st.session_state.profile.update({
            "name": new_name,
            "location": new_location,
            "university": new_university,
            "field": new_field,
            "bio": new_bio
        })
        save_profile_data()  # Save profile data after updating
        st.success("Profile updated successfully!")

def display_contact():
    # Header section
    st.markdown("""
        <div class="main-header contact-header">
            <h1>Let's Connect!</h1>
            <p>Feel free to reach out for collaborations or just a friendly chat</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact section with two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card contact-form-card">', unsafe_allow_html=True)
        st.markdown("""
            <h3 class="form-title">Send Me a Message</h3>
            <form action="https://formsubmit.co/eugene.ndayishimiye@gmail.com" method="POST">
                <div class="modern-input-group">
                    <div class="input-icon">👤</div>
                    <input type="text" name="name" placeholder="Enter your full name" required 
                           class="modern-input" autocomplete="name">
                </div>
                <div class="modern-input-group">
                    <div class="input-icon">✉️</div>
                    <input type="email" name="email" placeholder="Your email address" required 
                           class="modern-input" autocomplete="email">
                </div>
                <div class="modern-input-group">
                    <div class="input-icon">📝</div>
                    <input type="text" name="subject" placeholder="What's this about?" 
                           class="modern-input">
                </div>
                <div class="modern-input-group">
                    <div class="input-icon">💭</div>
                    <textarea name="message" placeholder="Your message here..." rows="5" required 
                              class="modern-textarea"></textarea>
                </div>
                <button type="submit" class="modern-submit-btn">
                    <span class="btn-text">Send Message</span>
                    <span class="btn-icon">➤</span>
                </button>
            </form>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card social-links-card">', unsafe_allow_html=True)
        st.markdown("""
            <h3>Connect With Me</h3>
            <div class="social-links">
                <a href="https://linkedin.com/in/yourusername" class="social-link linkedin">
                    <i class="fab fa-linkedin"></i> LinkedIn
                </a>
                <a href="https://github.com/yourusername" class="social-link github">
                    <i class="fab fa-github"></i> GitHub
                </a>
                <a href="https://twitter.com/yourusername" class="social-link twitter">
                    <i class="fab fa-twitter"></i> Twitter
                </a>
                <a href="mailto:your@email.com" class="social-link email">
                    <i class="fas fa-envelope"></i> Email
                </a>
            </div>
            
            <div class="location-info">
                <h4>Location</h4>
                <p>📍 Kigali, Rwanda</p>
                <p>🌐 Available for Remote Work</p>
            </div>
            
            <div class="availability-status">
                <h4>Current Status</h4>
                <p class="status-badge">🟢 Available for Opportunities</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
