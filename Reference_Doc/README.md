
## Dr. AI - How to setup and run this project?

**----- To setup ---**
1. Clone this project to local

2. Open server side app.py in visual studio code and ensure terminal window is naviagate server folder <br>
    C:\Users\Desktop\Project3\server<br>
    Run the below commands in the visual studio terminal window - only for the first time<br>
    $ python -m venv env<br>
    $ source env/bin/activate<br>
    (env)$ pip install -r requirements.txt<br>

3. Open client folder in another visual studio code and ensure terminal window is naviagate client folder:<br>
C:\Users\Desktop\Project3\client<br>
<br>

Run the below commands in the visual studio terminal window - only for the first time<br>
* $ npm install
* $ npm i @vue/compat
* $ npm install bootstrap 
* $ npm install bootstrap-vue
* $ npm i @vitejs/plugin-vue

**----- To Execute ---**
Open server side app.py in visual studio code and ensure terminal window is naviagate server folder and un the below command<br>
* $ source env/bin/activate<br>
* $ flask run --port=5001 --debugger <br>
    Navigate to webbrowser use the below api calls and check you get back response using API calls <br>
    * http://localhost:5001/refresh_data
    * http://localhost:5001/getMedicationByType/Over-the-counter
    * http://localhost:5001/getCountByCategory/Over-the-counter/dosage_form
    * http://localhost:5001/getMoreDetailsFromFDA/FAMOTIDINE<br>

Open client folder in another visual studio code and ensure terminal window is naviagate client folder:<br>
C:\Users\Desktop\Project3\client<br>
* $ npm run dev <br>
Navigate to http://localhost:5173/Doctorai and play around in the webpage.

