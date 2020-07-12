import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class test {
	
	//private Process process;
	public static void main(String[] args) {
		
		try {
			String s = null;
		Process process = Runtime.getRuntime().exec("python C:\\Users\\HP\\Desktop\\Corona-virus\\corona-virus.py");
		BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
		while((s=in.readLine())!=null) {
			System.out.println(s);
		}
		
	} catch (IOException e) {
		e.printStackTrace();
	}

	}

}
