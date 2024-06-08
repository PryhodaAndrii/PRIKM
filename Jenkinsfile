pipeline {
    agent any
    environment {
		MAIN_BOT_TOKEN = credentials('main_bot_token')
		API_ID = credentials('api_id')
		API_HASH = credentials('api_hash')
	
		DOCKER_IMAGE = 'pryhodaandrii/downloader'
    }
    stages {
        stage('Start') {
            steps {
                echo 'downloader: nginx/custom'
            }
        }

        stage('Build Weather services') {
            steps {
                sh 'export MAIN_BOT_TOKEN=$MAIN_BOT_TOKEN'
				sh 'export API_ID=$API_ID'
				sh 'export API_HASH=$API_HASH'
                dir("Soc_Downloader")
				{
					sh 'docker-compose build'
				}
				sh 'docker tag downloader:latest $DOCKER_IMAGE:latest'
                sh 'docker tag downloader:latest $DOCKER_IMAGE:$BUILD_NUMBER'
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\n Branch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\n Failure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

        stage('Test downloader services') {
            steps {
                echo 'Pass'
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

		stage('Push to registry') {
            steps {
                withDockerRegistry([ credentialsId: "dockerhub_token", url: "" ])
                {
                    sh "docker push $DOCKER_IMAGE:latest"
                    sh "docker push $DOCKER_IMAGE:$BUILD_NUMBER"

                }
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }

        stage('Deploy downloader services') {
            steps {
				dir("Soc_Downloader"){
					sh "docker-compose down -v"
                	sh "docker container prune --force"
                	sh "docker image prune --force"
                	sh "docker-compose up -d --build"
				}
            }
            post{
                failure {
                    script {
                    // Send Telegram notification on success
                        telegramSend message: "Job Name: ${env.JOB_NAME}\nBranch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}\nFailure stage: '${env.STAGE_NAME}'"
                    }
                }
            }
        }
    }

    post {
        success {
            script {
                // Send Telegram notification on success
                telegramSend message: "Job Name: ${env.JOB_NAME}\n Branch: ${env.GIT_BRANCH}\nBuild #${env.BUILD_NUMBER}: ${currentBuild.currentResult}"
            }
        }
    }
}