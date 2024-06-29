import os
import zipfile
import datetime

def pack():

    dt = datetime.datetime.now().strftime('%H-%M_%d.%m.%y')
    archive_name = f'submission-{dt}.zip'

    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                file_path = os.path.join(root, file)
                archive_path = os.path.relpath(file_path, os.getcwd())
                current_dir = os.path.basename(root)
                
                if file in ['requirements.txt', 'manage.py', 'caller.py'] or current_dir in ['main_app', 'orm_skeleton', 'migrations']:
                    zipf.write(file_path, archive_path)

    print(f'Submission created: {archive_name}')

if __name__ == '__main__':
    pack()

