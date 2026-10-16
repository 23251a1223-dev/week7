
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code fetched from SCM'
            }
        }

        stage('Check Files') {
            steps {
                bat 'dir'
                bat 'if not exist Dockerfile exit /b 1'
                bat 'if not exist app.py exit /b 1'
                bat 'if not exist requirements.txt exit /b 1'
                bat 'if not exist templates\\register.html exit /b 1'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t week7-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                    docker rm -f week7-app-container 2>NUL
                    docker run -d --name week7-app-container -p 5000:5000 week7-app
                '''
            }
        }

        stage('Test Application') {
            steps {
                bat '''
                    powershell -NoProfile -Command "$ok = $false; for ($i=0; $i -lt 15; $i++) { try { $r = Invoke-WebRequest -Uri 'http://localhost:5000/' -UseBasicParsing -TimeoutSec 3; if ($r.StatusCode -eq 200) { $ok = $true; break } } catch {}; Start-Sleep -Seconds 2 }; if (-not $ok) { exit 1 }; Write-Host 'Registration page test passed'"
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Application deployed successfully!'
        }
        failure {
            echo 'FAILED: Check Jenkins Console Output.'
        }
    }
}
