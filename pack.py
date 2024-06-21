import datetime
import os
import zipfile


def pack():

    dt = datetime.datetime.now().strftime('%H-%M_%d.%m.%y')

    with zipfile.ZipFile(f'submission-{dt}.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                file_path = os.path.join(root, file)
                archive_path = os.path.relpath(file_path, '.')
                current_dir = os.path.basename(root)

                # Skip files in the venv directory
                if 'venv' in root.split(os.path.sep):
                    continue

                if file in ['requirements.txt', 'manage.py', 'caller.py'] or current_dir in ['main_app', 'orm_skeleton',
                                                                                             'migrations']:
                    zipf.write(file_path, archive_path)

    print('Submission created!')


if __name__ == '__main__':
    pack()
