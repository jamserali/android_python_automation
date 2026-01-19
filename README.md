create venv : python -m venv venv
Activate venv : venv\Scripts\activate 

run requirement file: pip install -r requirements.txt

Start hub : java -jar selenium-server-4.39.0.jar hub
Start appium server : appium
Start node: java -jar selenium-server-4.39.0.jar node --config android_node.toml --hub http://localhost:4444

Execute tests :  python -m pytest --alluredir=reports/allure-results

See Allure report:  allure serve reports/allure-results
