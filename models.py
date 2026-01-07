from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Core Fields
    company = db.Column(db.String(150), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150))
    date_applied = db.Column(db.Date, default=datetime.utcnow)
    source = db.Column(db.String(100)) # LinkedIn, Indeed, etc.
    job_link = db.Column(db.String(500))
    
    # Tracking
    resume_version = db.Column(db.String(100))
    current_status = db.Column(db.String(50), default='Applied') # Applied, OA, Interview, Offer, Rejected
    last_contacted_date = db.Column(db.Date)
    
    # Details
    recruiter_info = db.Column(db.Text)
    salary_range = db.Column(db.String(100))
    referral_contact = db.Column(db.String(150))
    notes = db.Column(db.Text) # Interview/OA notes
    priority = db.Column(db.Integer, default=5) # 1-10
    
    # New Fields
    next_follow_up_date = db.Column(db.Date)
    timezone = db.Column(db.String(50), default='EST') # e.g., 'EST', 'PST'

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'job_title': self.job_title,
            'location': self.location,
            'date_applied': self.date_applied.strftime('%Y-%m-%d') if self.date_applied else None,
            'source': self.source,
            'job_link': self.job_link,
            'resume_version': self.resume_version,
            'current_status': self.current_status,
            'last_contacted_date': self.last_contacted_date.strftime('%Y-%m-%d') if self.last_contacted_date else None,
            'recruiter_info': self.recruiter_info,
            'salary_range': self.salary_range,
            'referral_contact': self.referral_contact,
            'notes': self.notes,
            'priority': self.priority,
            'next_follow_up_date': self.next_follow_up_date.strftime('%Y-%m-%d') if self.next_follow_up_date else None,
            'timezone': self.timezone
        }
