# EnergyAI

## Multiple csv
We have kept multiple data files that used during various stage of development for future reference. All personal data has been removed.

## Clone/Download/Install the code

Download the code to your folder.

1. Once you have the code, go to the folder where the file is downloaded and create a virtual environment:

2. Create a virtual environment using the following command::

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```sh
    venv\Scripts\activate.bat
    ```

4. Install dependencies defined in the `requirements.txt` file:le:

    ```sh
    python.exe -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

## For Creating the dummy data

Run the following command

```sh
python 01DataCheck.py
``````

## For Creating the prediction model

Run the following command

```sh
python 02Predict1.py
``````

## Creating Agent

Run the following command:

```sh
python 03AgentBuild2.py
``````

## Deploying Agent

Run the following command:

```sh
python 04deployment.py
``````

## Check the agent access

Run the following command:

```sh
python 05AccessAgent.py
``````

## Running  the streamlit

Run the following command:

```sh
streamlit run 06mainpage.py
``````