import java.io.*;
import java.net.*;
public class ClientChat {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			Socket sock = new Socket("localhost",8080);
			BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
			OutputStream ostream = sock.getOutputStream();
			PrintWriter pwrite = new PrintWriter(ostream,true);

			//receiving form server (receiveRead object)
			InputStream istream = sock.getInputStream();
			BufferedReader  receiveRead = new BufferedReader(new InputStreamReader(istream));

			System.out.println("Start the Chitchat , type and press ender key");

			String receiveMessage, sendMessage;
			while(true){
				sendMessage = keyRead.readLine();
				pwrite.println(sendMessage);
				pwrite.flush();
				if((receiveMessage = receiveRead.readLine()) != null){				//receive from server
					System.out.println(receiveMessage); 											//displaying at dos prompt
				}
			}
		}
		catch(Exception ex){
		}

	}
}
