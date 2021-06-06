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

## Deploy with AWS Copilot (using AWS ECS and AWS Fargate)

### Installing the AWS CLI

This will install the cli `aws`. It will necessary to authenticate into AWS.

For macOS run: `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg" && sudo installer -pkg AWSCLIV2.pkg -target /`

For Linux x68 run: `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install`

For windows use the MSI installer found here: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html#cliv2-windows-install

For more information see: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

### Installing Copilot CLI

This will install the cli `copilot`. You'll use it to deply the application.

For mac or Linux, install with: `brew install aws/tap/copilot-cli`

For windows install with `PS C:\> New-Item -Path 'C:\copilot' -ItemType directory; Invoke-WebRequest -OutFile 'C:\copilot\copilot.exe' https://github.com/aws/copilot-cli/releases/latest/download/copilot-windows.exe`

For more information see: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html#copilot-install

### Authenticate into AWS
Authenticate into AWS by running: `aws configure`.  

This will prompt you for your credentials and configure `aws` as well as `copilot`.

It will prompt you for you `AWS Access Key ID` and `AWS Secret Access Key` -- use the values for the IAM role you created earlier.

It will also prompt you for `Default region name` -- add a region such as `us-east-2`.

It will also prompt for `Default output format` -- you can leave these blank by hitting the enter key.

### Deploy with Copilot

Make sure that Docker is running locally, since you'll be building from a `Dockerfile`.

You'll be prompted for `Application name`, `Workload type`, `Service name` and `Dockerfile`. Set them as follows:

Application name: <any name>  
Workload type: <"Request-Driven Web Service" or "Load Balanced Web Service">  
Service name: <any name>  
Dockerfile: ./Dockerfile.copilot  

Selecting `Request-Driven Web Service` will deploy with AWS App Runner, while "Load Balanced Web Service" will deploy with AWS Fargate behind a load balancer. The first option is idea for intermittently or infrequently accessed endpoints while the second is better for applications that receive consistent traffic with or without spikes. These are the two options for a publically exposed endpoint; there are other options for private services. See: https://aws.github.io/copilot-cli/docs/concepts/services/

`copilot` infers the port from the `EXPOSE` statement in the `Dockerfile`. If your `Dockerfile` doesn't specify `EXPOSE`, you'll be prompted for the port as well. Its import to make sure that your `Dockerfile` uses the same port internally as you want to use externally; there is no port mapping on Copilot.

You'll be asked if you'd like to deploy, select `y` and hit enter. Copilot will provision all of the required architecture -- this may take a while.

### Clean Up

If you'd like to take this service down, run `copilot app delete` and press `y` to confirm.

## Note on Model
The model in the notebooks folder is not automaticallly moved to the app folder. This is intentional. If you want to change your model, you must move the file manually.
