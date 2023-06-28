## Dr. AI - How to setup and run this project?

## **----- To setup ---**
1. Clone this project to local

2. Open server side app.py in visual studio code and ensure terminal window is naviagate server folder like shown below <br>
    "C:\Users\Desktop\Project3\server"<br>
    <br>
    Run the below commands in the visual studio terminal window - only for the first time<br>
    $ python -m venv env<br>
    $ source env/bin/activate<br>
    (env)$ pip install -r requirements.txt<br>

3. Open client folder in another visual studio code and ensure terminal window is naviagate client folder:<br>
"C:\Users\Desktop\Project3\client"<br>
<br>

Run the below commands in the visual studio terminal window - only for the first time<br>
* $ npm install

If any issues please run the below install seperately. Not needed if above works fine and successfull and install all the below from package.json. Run only incase of issues
* $ npm i @vue/compat
* $ npm install bootstrap 
* $ npm install bootstrap-vue
* $ npm i @vitejs/plugin-vue

## **----- To Execute ---**
1. run mongod in your local machine - API calls needs mongodb connection and this step is essential for API calls to work 
2. Open server side app.py in visual studio code and ensure terminal window is naviagate server folder and run the below command<br>
    * $ source env/bin/activate<br>
    * $ flask run --port=5001 <br> <br>
        Navigate to webbrowser use the below api calls and check you get back response using API calls <br>
        * http://localhost:5001/refresh_data
        * http://localhost:5001/getMedicationByType/Over-the-counter
        * http://localhost:5001/getCountByCategory/Over-the-counter/dosage_form
        * http://localhost:5001/getMoreDetailsFromFDA/FAMOTIDINE<br>

3. Open client folder in another visual studio code and ensure terminal window is naviagate client folder:<br>
    "C:\Users\Desktop\Project3\client"<br>
    * $ npm run dev <br>
<br>s
Navigate to http://localhost:5173/Doctorai and play around in the webpage.

