package agents;

import jade.core.Agent;
import behaviours.ScrapingBehaviour1;

public class AgentScraping1 extends Agent {

	private static final long serialVersionUID = 1L;

	private ScrapingBehaviour1 b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new ScrapingBehaviour1();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	@Override
	protected void takeDown() {
		b.stop();
		System.out.println("arret");
	}
}
