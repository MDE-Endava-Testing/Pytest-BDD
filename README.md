# Pytest-BDD
Test Automation with Pytest-BDD framework.

### Requirements

- **Python installed.**
- **PipEnv installed locally (root project).**
- **PyTest (package) installed.**
- **PyTest BDD framework (plugin) installed.**
- **Selenium framework installed.**
- **PyCharm or Visual Studio Code.**

## Setup Instructions

``` 
- pip install pipenv
- pipenv install
- pipenv install pytest
- pipenv install pytest-bdd
- pipenv install selenium
```

1. Make sure to download the chrome driver version you need in https://sites.google.com/a/chromium.org/chromedriver/downloads 
2. If you use your local ChromeDriver, make sure to change your chrome driver path in the Driver class located in the utils package. This line: 
```
chrome_driver = webdriver.Chrome(executable_path='path/to/your/chromedriver.exe')
``` 
Else, just keep the configuration by default.
```
chrome_driver = webdriver.Chrome()
``` 
### Instructions to run project

Steps to run project.

1. Open CMD on the project's root.
2. Run project: ```pipenv run python -m pytest```

## Plugins
You can use some of PyCharm plugins to add Cucumber support to the IDE.

In PyCharm go to file/settings/plugins and search for Gherkin in the search bar. 

Install the following plugins:
- Gherkin
