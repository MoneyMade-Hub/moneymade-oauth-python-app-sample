### MoneyMade Oauth Python Provider Demo

This is a simple python app demo, which implements integration with [moneymade oauth feature](https://docs.moneymade.io/docs/interaction/connect-flow).

It uses [moneymade-connect-oauth-python-sdk](https://pypi.org/project/moneymade-connect-oauth-python-sdk) on a server side and shows frontend part integration sample.

Content:
 - [main.py](https://github.com/moneymadeio/moneymade-oauth-python-app-sample/blob/main/main.py) - backend side integration sample

 - [frontend/index.html](https://github.com/moneymadeio/moneymade-oauth-python-app-sample/blob/main/frontend/index.html) - frontend part integration sample

### Get started with demo

1. Clone this repo:
    ```shell
    git clone git@github.com:moneymadeio/moneymade-oauth-python-app-sample.git
    ```

2. Install dependencies (Using python venv is appreciated):
    ```shell
      pip install -r requirements.txt
    ```

3. Get your environment keys in the [dashboard](https://console.moneymade.io)
<br/>

4. Create .env file and set variables:
    ```
      PUBLIC_KEY=public key here
      PRIVATE_KEY=private key here
    ```

    <b>NOTE: don't use production variables to run demo app!</b>
    <br/>

5. Start an app via flask module:
    ```shell
      FLASK_APP=main python -m flask run
    ```

6. Open the app on your machine [host](http://localhost:5000/moneymade/oauth)


### Fell free to contact us if you have any questions!
