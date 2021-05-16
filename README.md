# students-api

## How to run locally?
```shell
source venv/bin/activate
pip install -r requirements.txt
cd src
python manage.py collectstatic
python manage.py createsuperuser
```

Make sure to create a config.ini in config directory with acceptable values for all the options
```shell
python manage.py runserver
```

Visit ```localhost:8000/admin``` in your browser, login with the credentials you've created in the ```createsuperuser``` step.

Now Navigate to the Student model on the left side pane and start by importing the ```sample_data.xlsx``` provided in the project's root directory.

Similarly, data can be exported with the export button in the Student Admin View.

Now to list the students in an api format, visit ```localhost:8000/api/students/``` using ```GET``` method. Alternatively open the url in your browser to view it in DRF's Browsable API.