package behaviours;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import jade.core.behaviours.Behaviour;

public class ScrapingBehaviour3 extends Behaviour {

	private static final long serialVersionUID = 1L;
	private Process process;

    @Override
	public void action() {
	  try { String s = null; 
	  //chemin script scraping_deaths
	  process = Runtime.getRuntime().exec("python C:\\Users\\HP\\Desktop\\Corona-virus\\scraping_deaths.py");
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
