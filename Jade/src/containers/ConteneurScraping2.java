package containers;

import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;

public class ConteneurScraping2 {
	
	public static void main(String[] args) {
        try {
        	//Contrôler le système d'exécution JADE à partir d'une application externe.
            Runtime runtime = Runtime.instance();
            /*Permet à JADE de récupérer des classes dépendantes de la configuration
            et des paramètres de démarrage.*/
            ProfileImpl profileImpl = new ProfileImpl(false);
            //Définir les paramètres
            profileImpl.setParameter(ProfileImpl.MAIN_HOST, "localhost");
            //Classe Proxy, permettant l'accès à un conteneur d'agent JADE
            AgentContainer agentContainer = runtime.createAgentContainer(profileImpl);
            // Créer un nouveau agent sans données
            AgentController agentController = agentContainer.createNewAgent("Scraping2",
                    "agents.AgentScraping2", new Object[]{});
          //Démarrer le conteneur d'agent
            agentController.start();
            
        } catch (Exception e) {
        	//Ecrire la trace de l'exception
            e.printStackTrace();
        }
    }

}
