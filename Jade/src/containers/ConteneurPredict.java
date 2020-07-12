package containers;

import jade.core.ProfileImpl;
import jade.core.Runtime;
import jade.wrapper.AgentContainer;
import jade.wrapper.AgentController;

public class ConteneurPredict {
	public static void main(String[] args) {
        try {
        	//Contr�ler le syst�me d'ex�cution JADE � partir d'une application externe.
            Runtime runtime = Runtime.instance();
            /*Permet � JADE de r�cup�rer des classes d�pendantes de la configuration
            et des param�tres de d�marrage.*/
            ProfileImpl profileImpl = new ProfileImpl(false);
            //D�finir les param�tres
            profileImpl.setParameter(ProfileImpl.MAIN_HOST, "localhost");
            //Classe Proxy, permettant l'acc�s � un conteneur d'agent JADE
            AgentContainer agentContainer = runtime.createAgentContainer(profileImpl);
            // Cr�er un nouveau agent sans donn�es
            AgentController agentController = agentContainer.createNewAgent("predict",
                    "agents.AgentPredict", new Object[]{});
          //D�marrer le conteneur d'agent
            agentController.start();
            
        } catch (Exception e) {
        	//Ecrire la trace de l'exception
            e.printStackTrace();
        }
    }
}
