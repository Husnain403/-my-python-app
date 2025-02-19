<<<<<<< HEAD
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DevOps!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

>>>>>>> 23038f3 (Deployment)
