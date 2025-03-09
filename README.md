Down load the code to your folder
On folder run
python -m venv venv
venv\scripts\activate
pip install --upgrade pip
#python.exe -m pip install --upgrade pip
pip install -r requirements.txt

**For Data Check**
python 01DataCheck.py

python 02Predict1.py
**For Streamlit**
streamlit run mainpage.py

**For Django**
python manage.py makemigrations
python manage.py makemigrations transactions
python manage.py makemigrations users
python manage.py migrate

# EnergyAI

Set up 1:
---------

After downloading the application, execute the following steps.

1.From Command Prompt, go to the project folder

2.Create a virtual environment using the following command

python -m venv venv

3. Activate the virtual environment :

venv\Scripts\activate.bat

4. Install dependencies defined in the requirements.txt file

python.exe -m pip install --upgrade pip
python -m pip install -r requirements.txt

5. change the directory to myenergy1 and execute migration command

python manage.py makemigrations 

python manage.py migrate

6. Create user:
   
python manage.py createsuperuser

8. Start the server
python manage.py shell
python manage.py runserver

9. Open the link in browser
http://127.0.0.1:8000
