package agents;

import behaviours.ScrapingBehaviour2;
import jade.core.Agent;

public class AgentScraping2 extends Agent {
	
	private static final long serialVersionUID = 1L;

	private ScrapingBehaviour2 b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new ScrapingBehaviour2();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	@Override
	protected void takeDown() {
		b.stop();
		System.out.println("arret");
	}

}
