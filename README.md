# Personal Landing Page with Admin Panel

A beautiful, responsive personal landing page built with Flask and Bootstrap, featuring an admin panel for image management.

## Features

- **Beautiful Landing Page**: Modern, responsive design with hero section, about, gallery, and contact sections
- **Image Carousel**: Dynamic image gallery that displays uploaded images
- **Admin Panel**: Secure admin access for image management
- **Image Upload**: Upload images that automatically appear in the homepage carousel
- **Image Management**: View and delete uploaded images
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## Admin Credentials

- **Username**: admin
- **Password**: admin123

## Installation & Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Access the application**:
   - Homepage: http://localhost:5000
   - Admin Login: http://localhost:5000/admin/login

## Usage

### For Visitors
- Visit the homepage to see your personal landing page
- Browse the image gallery carousel
- View your skills, about information, and contact details

### For Admin
1. Go to `/admin/login` or click the "Admin" link in the navigation
2. Login with credentials: `admin` / `admin123`
3. Upload new images using the upload form
4. Manage existing images (view and delete)
5. Uploaded images automatically appear in the homepage carousel

## File Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── admin_login.html  # Admin login page
│   └── admin.html        # Admin panel
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── images/           # Static images
│   └── uploads/          # Uploaded images (created automatically)
└── README.md             # This file
```

## Customization

### Personal Information
Edit the following in `templates/index.html`:
- Name in the hero section and navbar
- About section content
- Skills and services
- Contact information
- Social media links

### Styling
Modify `static/css/style.css` to change:
- Colors and theme
- Layout and spacing
- Animations and effects
- Responsive breakpoints

### Profile Image
Replace `static/images/profile.jpg` with your actual profile photo.

## Security Notes

- Change the `app.secret_key` in `app.py` for production
- Consider using environment variables for sensitive configuration
- For production, use a proper database instead of hardcoded credentials
- Implement proper file validation and security measures

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **File Upload**: Werkzeug

## License

This project is open source and available under the MIT License.