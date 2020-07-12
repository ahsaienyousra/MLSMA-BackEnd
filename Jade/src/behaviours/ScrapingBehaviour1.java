package behaviours;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

import io.github.alekseysotnikov.cmd.core.Cmd;
import io.github.alekseysotnikov.cmd.listeners.WorkDir;
import jade.core.behaviours.Behaviour;


/**
 * @author HP
 *
 */
public class ScrapingBehaviour1 extends Behaviour {
	private static final long serialVersionUID = 1L;
	private Process process;

    @Override
	public void action() {
	  try { String s = null; 
	  //chemin script scraping_collection1
	  process = Runtime.getRuntime().exec("python C:\\Users\\HP\\Desktop\\Corona-virus\\corona-virus.py");
	  BufferedReader in = new BufferedReader(new
	  InputStreamReader(process.getInputStream()));
	  while ((s = in.readLine()) != null) {
		  System.out.println(s); }
	  }
	 catch (IOException e) { e.printStackTrace(); } }
	@Override
	public boolean done() {
		return !(process != null && process.isAlive());
	}
	@Override
	public int onEnd() {
		return super.onEnd();
	}
	public void stop() {
		if (process != null)
			process.destroyForcibly();
		myAgent.doDelete();
	}

}
