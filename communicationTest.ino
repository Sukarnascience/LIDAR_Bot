#include <WiFi.h>

// Set the WiFi network credentials
const char* ssid = "MyServer";
const char* password = "passmein";

// Set the IP address and port number to listen on
//IPAddress ip(192, 168, 1, 100);
IPAddress local_IP(192, 168, 1, 100); // Set your desired IP address
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress dns(8, 8, 8, 8); // Set your desired DNS server
int port = 12345;

// Create a WiFi server object
WiFiServer server(port);

void setup() {
  Serial.begin(115200);

  // Connect to the WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  // Set the static IP address for the ESP32

  WiFi.config(local_IP, gateway, subnet, dns);


  // Start the WiFi server
  server.begin();
  Serial.println("Server started");
}

void loop() {
  // Wait for a client to connect
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected");

    // Read data from the client
    String data = client.readStringUntil('\n');
    Serial.println("Received: " + data);

    // Send a response to the client
    String response = "Hello from ESP32!\n";
    client.print(response);

    // Close the client connection
    client.stop();
    Serial.println("Client disconnected");
  }
}