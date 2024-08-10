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
file5 = pd.read_excel(os.path.join(data_dir, 'ex3.xlsx')).head(10)

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

@app.route('/file5')
def show_file5():
    return render_template('file5.html', file5=file5)

@app.route('/submit/<file_type>', methods=['POST'])
def submit(file_type):
    relevant_data = []
    for index in range(10):
        relevant = request.form.get(f'relevant_{index}')
        relevant_data.append({'index': index, 'relevant': relevant})
    
    df_relevant = pd.DataFrame(relevant_data)
    filename = request.form.get('filename')
    df_relevant.to_csv(os.path.join(results_dir, f'{filename}.csv'), index=False)
    
    if file_type == 'file4':
        return redirect(url_for('show_file4'))
    elif file_type == 'file5':
        return redirect(url_for('show_file5'))
    else:
        return "Invalid file type", 400

if __name__ == '__main__':
    app.run(debug=True)
