pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    pkill -f "flask run" || true
                    source $VENV_DIR/bin/activate
                    export FLASK_APP=app.py
                    nohup flask run --host=0.0.0.0 --port=5000 &
                '''
            }
        }
    }

    post {
        success {
            echo ' App deployed successfully!'
        }
        failure {
            echo ' Build failed.'
        }
    }
}
