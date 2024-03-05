import os
import subprocess
import shutil
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        python_version = request.form.get('python_version')
        drive = request.form.get('drive')
        environment = request.form.get('environment')
        dockize = 'Yes' if 'dockize' in request.form else 'No'

        try:
            install_script(python_version, drive, environment, dockize)
            success_message = f'Python {python_version} installed successfully in {drive}:\\ScriptInstaller'
            return render_template('success.html', success_message=success_message)
        except Exception as e:
            return render_template('error.html', error_message=str(e))

    # Get available drives on the system
    drives = get_available_drives()

    return render_template('index.html', drives=drives)

def get_available_drives():
    # Get a list of available drives on the system
    drives = [f"{chr(drive)} Drive" for drive in range(65, 91) if os.path.exists(f'{chr(drive)}:\\')]
    return drives

def install_script(python_version, drive, environment, dockize):
    # Create a new folder on the selected drive
    folder_path = os.path.join(drive, 'ScriptInstaller')
    os.makedirs(folder_path, exist_ok=True)

    # Install Python in a virtual environment
    venv_path = os.path.join(folder_path, 'venv')
    python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')

    subprocess.run(['python', '-m', 'venv', venv_path], check=True)

    # Activate the virtual environment and install the specified Python version
    activate_venv_cmd = os.path.join(venv_path, 'Scripts', 'activate')
    pip_install_cmd = f'"{activate_venv_cmd}" && py -m venv --upgrade-deps --clear {venv_path} && "{python_exe}" -m pip install --upgrade pip'

    subprocess.run(pip_install_cmd, check=True, shell=True)
    print(f'Python {python_version} installed in {venv_path}')

    # Install Docker (optional)
    if dockize == 'Yes':
        try:
            dockerfile_content = f'''
FROM python:{python_version}-slim
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip
'''
            dockerfile_path = os.path.join(folder_path, 'Dockerfile')
            with open(dockerfile_path, 'w') as f:
                f.write(dockerfile_content)
        except Exception as e:
            print(f'Docker installation error: {e}')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
