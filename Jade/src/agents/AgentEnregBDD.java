package agents;

import behaviours.EnregBehaviour;
import jade.core.Agent;

public class AgentEnregBDD extends Agent {

	private static final long serialVersionUID = 1L;

	private EnregBehaviour b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new EnregBehaviour();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	 @Override
	 protected void takeDown() {
	 b.stop();
	 System.out.println("arret");
	 }

}