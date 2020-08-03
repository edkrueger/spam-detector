# spam-detector

## Dev Instructions for App
Run `pipenv install --dev` to install the env.  
Run `pipenv run pre-commit install` to initialize the git hooks.  
Run `pipenv run pre-commit run --all-files` if there are file that were committed before adding the git hooks.  
Activate the shell with: `pipenv shell`  
Lint with: `pylint app/`  

## Dev Instructions for Notebooks
Go to your favorite Jupyter Notebook platform and run `pip install -r requirements.txt`.  
I use GCP AI Platform Notebooks.  

## Build and Run in Docker Locally
Build: `docker build . -t spam-detector`
Run: `PORT=8000 &&  docker run -p 80:${PORT} -e PORT=${PORT} spam-detector`

## Note on Model
The model in the notebooks folder is not automaticallly moved to the app folder. This is intentional. If you want to change your model, you must move the file manually.
