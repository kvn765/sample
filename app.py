from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Simple admin credentials (in production, use a database)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD_HASH = generate_password_hash('admin123')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_carousel_images():
    """Get list of uploaded images for carousel"""
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        return []
    
    images = []
    for filename in os.listdir(upload_folder):
        if allowed_file(filename):
            images.append(filename)
    return sorted(images)

@app.route('/')
def home():
    images = get_carousel_images()
    return render_template('index.html', images=images)

@app.route('/admin')
def admin():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    
    images = get_carousel_images()
    return render_template('admin.html', images=images)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/admin/upload', methods=['POST'])
def upload_image():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    
    if 'file' not in request.files:
        flash('No file selected!', 'error')
        return redirect(url_for('admin'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected!', 'error')
        return redirect(url_for('admin'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image uploaded successfully!', 'success')
    else:
        flash('Invalid file type! Please upload PNG, JPG, JPEG, GIF, or WebP files.', 'error')
    
    return redirect(url_for('admin'))

@app.route('/admin/delete/<filename>')
def delete_image(filename):
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
    
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(file_path):
            os.remove(file_path)
            flash('Image deleted successfully!', 'success')
        else:
            flash('Image not found!', 'error')
    except Exception as e:
        flash('Error deleting image!', 'error')
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)