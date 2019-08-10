from flask import Flask

import os

app = Flask(__name__)


@app.route('/helm/push', methods=['GET'])
def helm_package():
    helm_push()


def git_clone():
    os.system('./git-clone.sh')


def helm_push():
    os.system('./helm-push.sh')


if __name__ == '__main__':
    git_clone()
    app.run()
