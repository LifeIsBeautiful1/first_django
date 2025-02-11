Product Requirements Document (PRD)
Project Name: Intelligends – Kids’ Activities Marketplace
MVP Version: 1.0
Date: February 9, 2025

1. Overview
Goal:
Create a simple, responsive marketplace website where parents can discover extracurricular activities (piano classes, English courses, etc.) for their children. Academies will gain higher visibility, manage their courses, and receive direct inquiries from parents.

Primary Audience:

Parents: Looking for courses for their kids (no account required).
Academies: Can claim their profiles and manage course listings.
Key Features:

No login required for parents.
Embedded Google Reviews instead of custom review functionality.
Academies imported from an external list with the option to claim profiles.
Tech Stack:

Backend: Python (Django)
Frontend: Django Templates with Bootstrap or Tailwind CSS
Database: PostgreSQL
Hosting: www.intelligends.com

2. Features & Functional Requirements
2.1. Public Website (Parents)
Homepage:

Search bar for courses (by activity type, location, age, price).
Featured courses/academies.
Course Listing Page:

List of courses with filters (location, price range, age group, activity type).
Each course card shows title, academy name, price, and basic details.
Course Details Page:

Full course description: title, details, schedule, price, images.
Academy profile with embedded Google Reviews.
Simple Inquiry/Booking Form: Fields: Name, Email, Phone, Message.
Submit inquiry → Academy receives an email notification.
2.2. Academy Features
Imported Academy Profiles:

Basic info: name, location, contact details, Google Reviews.
"Claim This Profile" Button: Opens a form with fields for verification (business email, phone, message).
Claim Process:

Admin receives the claim request for approval.
Upon approval, the academy gets access to manage their profile and courses.
Academy Dashboard (Post-Claim):

Profile Management: Update academy info (description, logo, contact details).
Course Management: Add, edit, or delete courses (title, description, schedule, price, images).
Inquiry Management: View inquiries from parents.
2.3. Admin Panel (For You)
Dashboard: Overview of total academies, courses, and inquiries.
Manage Academies: Approve/reject claim requests, edit academy details.
Manage Courses: Approve/reject new courses if moderation is needed.
Inquiry List: View all inquiries submitted through the platform.

3. Database Schema (Simplified)
3.1. Tables
Academy:

id (PK)
name
description
address
contact_email
contact_phone
claimed (boolean)
owner_id (FK to User if claimed)
Course:

id (PK)
academy_id (FK)
title
description
schedule
price
image_url
Inquiry:

id (PK)
course_id (FK)
parent_name
parent_email
parent_phone
message
submitted_at
ClaimRequest:

id (PK)
academy_id (FK)
requester_name
requester_email
verification_status (pending, approved, rejected)
submitted_at
4. User Flows
4.1. Parent (No Login Needed):
Homepage → Search/Browse Courses → View Course Details → Submit Inquiry → Confirmation Message

4.2. Academy (Post-Claim):
Visit Academy Profile → Click "Claim This Profile" → Submit Verification → Admin Approval → Access Dashboard → Manage Courses

4.3. Admin (You):
Login to Admin Panel → View Claim Requests → Approve/Reject Claims → Manage Academies, Courses, Inquiries

5. API Endpoints (Optional for Future MVP Enhancements)
GET /courses/: List all courses
GET /courses/{id}/: Get course details
POST /inquiries/: Submit inquiry
POST /academies/claim/: Submit claim request
POST /admin/approve-claim/: Approve or reject academy claim

6. Non-Functional Requirements
Responsive Design: Optimized for desktop, tablet, and mobile.
SEO Optimized: For better search engine visibility.
Security: Basic validation for form submissions to prevent spam.