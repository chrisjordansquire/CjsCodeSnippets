import java.io.InputStream;
import java.net.URLConnection;
import java.net.URL;
import java.util.Scanner;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

/**
 * Created by cjordan1 on 7/31/15.
 * A comparison of a few different ways to do an HTTP get request in Java
 */
public class HttpGetExample {

    public static void main(String[] args) {
        standardLibraryHttpGetExample();
        System.out.println("\n\n");
        httpClientHttpGetExample();
    }

    public static void standardLibraryHttpGetExample(){
        //See http://stackoverflow.com/questions/2793150
        //and http://stackoverflow.com/questions/10116961/
        String url = "http://www.google.com";
        String charset = "UTF-8";

        URLConnection connection;
        InputStream response;
        try {
            connection = new URL(url).openConnection();
        }catch(Exception e){
            System.out.println("Connection creation failed");
            return;
        }

        connection.setRequestProperty("Accept-Charset", charset);
        try {
            response = connection.getInputStream();
        }catch(Exception e){
            System.out.println("Connection request failed");
            return;
        }

        System.out.println(convertStreamToString(response));
    }

    static String convertStreamToString(InputStream inputStream){
        //See http://stackoverflow.com/questions/309424/read-convert-an-inputstream-to-a-string
        Scanner scanner = new Scanner(inputStream).useDelimiter("\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }

    public static void httpClientHttpGetExample(){
        HttpGet httpGet = new HttpGet("http://www.google.com");
        CloseableHttpClient httpClient = HttpClients.createDefault();
        CloseableHttpResponse response;

        try {
            response = httpClient.execute(httpGet);
        }catch(Exception e){
            System.out.println("httpClient execute failed");
            return;
        }

        HttpEntity entity = response.getEntity();
        String content;
        try {
            content = convertStreamToString(entity.getContent());
            System.out.println(content);
        }catch(Exception e){
            System.out.println("Get Content failed");
        }
    }

    public static void joupExample(){
        try {
            Document document = Jsoup.connect("http://www.google.com").get();
        }catch(Exception e){
            System.out.println("Jsoup get failed");
        }
    }
}
