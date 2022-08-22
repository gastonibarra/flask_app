pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "ibarragaston/flask_api"
    }
    stages {
        
        stage('Build and Push Docker Image...') {
          steps {
                script {
                  // DOCKER HUB
                  
                  /* Build the container image */
                  def dockerImage = docker.build(DOCKER_IMAGE_NAME)

                  /* Push the container to the docker Hub */
                  docker.withRegistry('https://registry.hub.docker.com', 'docker_hub') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}