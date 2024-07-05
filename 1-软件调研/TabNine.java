import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
public class Main {
    // read xml file
    public static void main(String[] args) {
        try {
            File file = new File("C:\\Users\\user\\Desktop\\hw1_Software_Research\\src\\hw1_Software_Research\\data.xml");
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(file);
            doc.getDocumentElement().normalize();
            NodeList nodeList = doc.getElementsByTagName("student");
            for (int itr = 0; itr < nodeList.getLength(); itr++) {
                Node node = nodeList.item(itr);
                if (node.getNodeType() == Node.ELEMENT_NODE) {
                    Element eElement = (Element) node;
                    System.out.println("Student id: " + eElement.getElementsByTagName("id").item(0).getTextContent());
                    System.out.println("First Name: " + eElement.getElementsByTagName("firstname").item(0).getTextContent());
                    System.out.println("Last Name: " + eElement.getElementsByTagName("lastname").item(0).getTextContent());
                    System.out.println("Subject: " + eElement.getElementsByTagName("subject").item(0).getTextContent());
                    System.out.println("Marks: " + eElement.getElementsByTagName("marks").item(0).getTextContent());
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}