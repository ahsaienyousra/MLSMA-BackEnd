package agents;


import behaviours.VisualisationBehaviour;
import jade.core.Agent;

public class AgentVisualisation extends Agent {
	
	private static final long serialVersionUID = 1L;

	private VisualisationBehaviour b;

	@Override
	protected void setup() {

		Object[] args = getArguments();
		b = new VisualisationBehaviour();
		addBehaviour(b);

	}

	// Avant la fermeture de l'agent
	@Override
	protected void takeDown() {
		b.stop();
		System.out.println("arret");
	}

}
