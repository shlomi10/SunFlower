# Playwright Python Example

## Articles written about this project

## Project Setup

* Install pytest-html-reporter by running the following command:

```
pip install pytest-html-reporter
```

* Install Playwright by running the following command:

```
playwright install
```

* Install requirements (dependencies) by running the following command:

```
pip install -r requirements.txt 
```

* Clone the project
* Navigate to the project directory

## Running Tests with report

```
python -m pytest tests/ --html-report=./reports
```

## Running Tests with report and see the API requests and responses on the console
```
python -m pytest -s tests/ --html-report=./reports
```

## Running Tests in parallel with report and see the API requests and responses on the console
```
python -m pytest -s -n auto tests/ --html-report=./reports
```

When no browser was selected then chromium will be used.

* Run tests:

```
pytest
```

## Viewing Test Results

* View reports locally by navigate to the reports folder under the main folder of the project


* View Allure results locally by navigate to the project folder under the main folder of the project run the command:
```
allure serve
```

## View Help And Custom CLI Options

```
pytest --help
```