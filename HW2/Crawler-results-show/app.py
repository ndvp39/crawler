from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Ensure data directory exists and Excel files are present
data_dir = 'data'
results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

# Read Excel files
file1 = pd.read_excel(os.path.join(data_dir, 'avarage_runtime_per_genre_results.xlsx')).head(10)
file2 = pd.read_excel(os.path.join(data_dir, 'best_boxoffice_per_genre_results.xlsx')).head(10)
file3 = pd.read_excel(os.path.join(data_dir, 'best_directors_results.xlsx')).head(10)
file4 = pd.read_excel(os.path.join(data_dir, 'best_directors_upgrade.xlsx')).head(10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file1')
def show_file1():
    return render_template('file1.html', file1=file1.to_html())

@app.route('/file2')
def show_file2():
    return render_template('file2.html', file2=file2.to_html())

@app.route('/file3')
def show_file3():
    return render_template('file3.html', file3=file3.to_html())

@app.route('/file4')
def show_file4():
    return render_template('file4.html', file4=file4)

@app.route('/submit', methods=['POST'])
def submit():
    relevant_data = []
    for index in range(10):
        relevant = request.form.get(f'relevant_{index}')
        relevant_data.append({'index': index, 'relevant': relevant})
    
    df_relevant = pd.DataFrame(relevant_data)
    filename = request.form.get('filename')
    df_relevant.to_csv(os.path.join(results_dir, f'{filename}.csv'), index=False)
    
    return redirect(url_for('show_file4'))

if __name__ == '__main__':
    app.run(debug=True)
