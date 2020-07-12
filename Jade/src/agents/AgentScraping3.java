package agents;

import behaviours.ScrapingBehaviour3;
import jade.core.Agent;

public class AgentScraping3 extends Agent {
	
	private static final long serialVersionUID = 1L;

	private ScrapingBehaviour3 b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new ScrapingBehaviour3();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	@Override
	protected void takeDown() {
		b.stop();
		System.out.println("arret");
	}

}
