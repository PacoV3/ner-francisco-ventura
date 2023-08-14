import dotenv
import os

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)


def get_env_path():
    '''This function gets the .env paths on the project.
	return: A dictionary that includes the path of the project dir and the .env file
    '''
    return {'project_dir': project_dir, 'dotenv_path': dotenv_path}

def get_env_variable(env_variable_name: str):
    '''This function gets a specific environment variable from the name. You can expect different outputs if the function is run by tests, or if it's run by a notebook or direct piece of code. 
	param env_variable_name: String
		Key of the environment variable that you want to get
	return: String containing the value of the environment variable and a "None" object in case if was not found
    '''
    return os.environ.get(env_variable_name)
