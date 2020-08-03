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
