import java.io.*;
import java.net.*;
public class ServerChat {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			ServerSocket ss = new ServerSocket(8080);
			System.out.println("server ready for chatting");
			Socket sock = ss.accept();
			
			//reading from keyboard (keyread object)
			BufferedReader keyRead = new BufferedReader(new InputStreamReader(System.in));
			
			//sending to client (pwrite object)
			OutputStream ostream = sock.getOutputStream();
			PrintWriter pwrite = new PrintWriter(ostream,true);
			
			//receiving from server (receiveRead object)
			InputStream istream = sock.getInputStream();
			BufferedReader  receiveRead = new BufferedReader(new InputStreamReader(istream));
			
			String receiveMessage, sendMessage;
			while(true)
			{
				if((receiveMessage =  receiveRead.readLine() )!= null)
				{
					System.out.println(receiveMessage);
				}
				sendMessage = keyRead.readLine();
				pwrite.println(sendMessage);
				pwrite.flush();
			}
		}catch(Exception ex)
		{
			}
		}

}
