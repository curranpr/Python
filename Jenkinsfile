pipeline {
    agent any
    tools {
        jdk 'JDK 1.7'
    } 
    stages {
        stage('build') {
            steps {
                sh 'python3 python2.py'
            }
        }
    }
}