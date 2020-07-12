package containers;


import jade.core.Profile;
import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.util.ExtendedProperties;
import jade.util.leap.Properties;
import jade.wrapper.AgentContainer;

public class MainContainer {

    public static void main(String[] args) {
        try {
        	//Contrôler le système d'exécution JADE à partir d'une application externe.
            Runtime runtime = Runtime.instance();
            //Construire une collection de propriétés vides
            Properties properties = new ExtendedProperties();
            //Définir l'interface graphique et la valeur à stocker
            properties.setProperty(Profile.GUI, "true");
            /*Permet à JADE de récupérer des classes dépendantes de la 
            configuration et des paramètres de démarrage.*/
            ProfileImpl profileImpl = new ProfileImpl(properties);
            //Classe Proxy, permettant l'accès à un conteneur d'agent JADE
            AgentContainer mainContainer = runtime.createMainContainer(profileImpl);
            //Démarrer le conteneur d'agent
            mainContainer.start();
            
        } catch (Exception e) {
        	//Ecrire la trace de l'exception
            e.printStackTrace(); 
        }
    }
}
