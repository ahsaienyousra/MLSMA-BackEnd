package behaviours;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

import jade.core.behaviours.Behaviour;

public class PredictBehaviour extends Behaviour {
	private static final long serialVersionUID = 1L;

	//private String tag;
	private Process process;

	public void action() {
		try { String s = null; 
		//Backend_algos\Predict
		process = Runtime.getRuntime().exec("flask run",null, new File ("C:\\Users\\HP\\Desktop\\Predict"));
		  BufferedReader in = new BufferedReader(new
		  InputStreamReader(process.getInputStream()));
		  while ((s = in.readLine()) != null) {
			  System.out.println(s); }
		  }
		 catch (IOException e) { e.printStackTrace(); }
}
	
	public boolean done() {
		return !(process != null && process.isAlive());
	}

	public int onEnd() {
		// stop();
		return super.onEnd();
	}

	public void stop() {
		if (process != null)
			process.destroyForcibly();
		myAgent.doDelete();
	}

}
