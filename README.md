<p align="center">
  <img src="https://github.com/RaviRockyRavindra/TCP-SYN_FLOOD/blob/main/Drawing.png" width="auto" title="TCP_SYN_FLOOD_RAVI_ROCKY_RAVINDRA">
</p>

<p align="center">
  <img src="https://github.com/RaviRockyRavindra/TCP-SYN_FLOOD/blob/main/wireshark_tcp_FLOOD.png" width="auto" title="TCP_SYN_FLOOD_RAVI_ROCKY_RAVINDRA">
</p>

# TCP-SYN_FLOOD

Passive attack which is a form of DENIAL OF SERVICE ATTACK where the attacker establishes the connection and becomes unavailable to finalize it. To describe in a more technical way in order to make data communication over TCP/IP the 3-way-handshake would take place in between client and server also foundation for every connection established using the TCP protocol. Attackers were taking advantage of performing the incomplete connection initiation. This bring the server to busy stage and no longer available to the clients for serving any more.


# Thr33__WAY_HANDSHAKE : When a client attempts to start a TCP connection to a server, the client and server exchange a series of messages.
  ** client requests a connection by sending a SYN (synchronize) message to the server
  ** The server acknowledges this request by sending SYN-ACK back to the client.
  ** client responds with an ACK, and the connection is established.
  
# How long this impact on the server 
  ** as long as we terminate the execution

# Risk of the attack
  since this is the passive attack so could be a downtime for the server as long as we interuppt the execution.

Features:
# Socket creation with target
   before flooding our script would perform the socket creation on specified target where we're checking for both internet connectivity & and to confirm able to connect with target network
   
# input_validation
   our repo script will also us to specify both ipv4 and ipv6 .
