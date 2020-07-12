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
        	//Contr�ler le syst�me d'ex�cution JADE � partir d'une application externe.
            Runtime runtime = Runtime.instance();
            //Construire une collection de propri�t�s vides
            Properties properties = new ExtendedProperties();
            //D�finir l'interface graphique et la valeur � stocker
            properties.setProperty(Profile.GUI, "true");
            /*Permet � JADE de r�cup�rer des classes d�pendantes de la 
            configuration et des param�tres de d�marrage.*/
            ProfileImpl profileImpl = new ProfileImpl(properties);
            //Classe Proxy, permettant l'acc�s � un conteneur d'agent JADE
            AgentContainer mainContainer = runtime.createMainContainer(profileImpl);
            //D�marrer le conteneur d'agent
            mainContainer.start();
            
        } catch (Exception e) {
        	//Ecrire la trace de l'exception
            e.printStackTrace(); 
        }
    }
}
