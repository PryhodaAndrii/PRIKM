import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.*
import jenkins.model.*
import hudson.util.Secret
import org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl


// Функція для отримання змінних середовища
def getEnvVariable(String name) {
    return System.getenv(name)
}

def dockerUserName = getEnvVariable('DOCKERHUB_USERNAME')
def dockerPassword = getEnvVariable('DOCKERHUB_PASSWORD')

def mainBotToken = getEnvVariable('MAIN_BOT_TOKEN')
def apiID = getEnvVariable('API_ID')
def apiHash = getEnvVariable('API_HASH')

def domain = Domain.global()
def store = Jenkins.instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0].getStore()
def creds = new UsernamePasswordCredentialsImpl(CredentialsScope.GLOBAL, "dockerhub_token", "Description", dockerUserName, dockerPassword)


def mainBotTokenCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "main_bot_token", "main bot token", Secret.fromString(mainBotToken))
def apiIDCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "api_id", "tg api id", Secret.fromString(apiID))
def apiHashCreds = new StringCredentialsImpl(CredentialsScope.GLOBAL, "api_hash", "tg api hash", Secret.fromString(apiHash))

store.addCredentials(domain, creds)
store.addCredentials(domain, mainBotTokenCreds)
store.addCredentials(domain, apiIDCreds)
store.addCredentials(domain, apiHashCreds)