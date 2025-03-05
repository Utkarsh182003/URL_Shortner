from flask import Flask, render_template, request, redirect, url_for, flash
from database import db, URLMapping
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        
        if not original_url:
            flash("Please enter a URL", "error")
            return redirect(url_for('index'))

        # Check if URL is already shortened
        existing_url = URLMapping.query.filter_by(original_url=original_url).first()
        if existing_url:
            return render_template('short_url.html', short_code=existing_url.short_code)

        new_url = URLMapping(original_url)
        db.session.add(new_url)
        db.session.commit()
        
        return render_template('short_url.html', short_code=new_url.short_code)

    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_original(short_code):
    url_entry = URLMapping.query.filter_by(short_code=short_code).first()
    if url_entry:
        return redirect(url_entry.original_url)
    flash("Invalid short URL", "error")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
