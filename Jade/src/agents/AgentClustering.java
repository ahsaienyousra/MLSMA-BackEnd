package agents;

import behaviours.ClusteringBehaviour;
import jade.core.Agent;

public class AgentClustering extends Agent {

	private static final long serialVersionUID = 1L;

	private ClusteringBehaviour b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new ClusteringBehaviour();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	@Override
	protected void takeDown() {
		b.stop();
		System.out.println("arret");
	}

}
