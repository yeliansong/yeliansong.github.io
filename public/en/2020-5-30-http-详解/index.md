# Detailed explanation of HTTP


This summary may not cover all HTTP knowledge points, but it is just based on my own understanding, and then combined with online information to summarize.

### 1. What is HTTP

HTTP (hypertext transport protocol), is the hypertext transfer protocol, text can be understood as characters, text, audio and video, etc. Hypertext is not a simple text file, but a more complex mixture of various files.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf8j1170vxj30p80k0gr4.jpg" style="zoom: 67%;" />

In fact, it is very easy to understand. HTTP is actually an application layer protocol. Well, let’s review the seven-layer model of the network. Application layer, presentation layer, session layer, transport layer, network layer, link layer, physical layer.

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/gggg.jpeg)

This figure is still very comprehensive, outlining the scope of the functions of each layer of the entire seven-layer model. HTTP is an application layer protocol.

### 2. Different versions of HTTP

This was still asked during the interview, so let’s talk about it too. Currently, the http version has undergone four changes:

HTTP 0.9 --> HTTP 1.0 --> HTTP 1.1 --> HTTP 1.2

- HTTP 0.9

   The first version, this version only supports GET requests, and can only respond to HTML strings.

- HTTP 1.0

   Added post, delete, put. And the concept of request header and response header is added, and the version number, status code, encoding and other content of the HTTP protocol are specified, and it also supports the transmission of pictures, audio and video, binary and other content.

- HTTP 1.1

   Added long links, added pipeline processing, cache processing and breakpoint transmission. Pipelining means that multiple HTTP requests can be sent at the same time without waiting for responses one by one. For resuming uploads from breakpoints, the client will record the current download progress, and then notify the server of the content fragments that need to be downloaded this time when resuming the upload is required. The long link will be explained in detail below.

#### 2.1 The difference between long links and short links

In fact, it is very easy to understand. The long connection means that after the client and the server establish a connection, they will keep the connection state, and there is no need to disconnect after the end of a request; the short connection is the opposite, and the connection will be disconnected after each request. So their advantages and disadvantages are very obvious.

The long connection saves connection and closing time and reduces waste. But there will also be a problem, that is, as the number of connections increases, the connection between the client and the server will always be maintained, which will bring some problems, and the server will definitely be overwhelmed. For this situation, there are also solutions. When After the number of connections reaches a certain number, the server can actively close some event connections that have not been read or written for a long time. Relatively speaking, the problem of short connections will be more serious, because each request needs to establish a connection, and then disconnect it. If it is a service that is frequently requested, it will take up a lot of resources. Therefore, whether it is a long connection or a short connection, it is determined according to specific needs.

### 3. Some elements of HTTP

#### 3.1 HTTP message

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jeo1er9j311w0m843k.jpg" style="zoom:150%;" />

This is the format of the HTTP message. The upper one is the request body, and the lower one is the returned thing. The details are as follows:

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jfvk74fj311i0jg47x.jpg" style="zoom:200%;" />

#### 3.2 URIs

What is the difference between URI and URL, and what is URI used for?

URI is Uniform Resource Identifier. It is used to define the address of the server to be accessed.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/ffff.jpeg" style="zoom:50%;" />

URI is composed of URL and URN.

#### 3.3 Cookies

Because HTTP is stateless, what does it mean, that is, the protocol has no memory ability for transaction processing, and the server side does not know the specific situation of the client side. The introduction of cookies is to solve this problem. The browser is responsible for storing cookies, not the operating system. If you change a server, you will not know.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jwstm0uj30z20hqk0j.jpg" style="zoom:150%;" />

#### 3.4 session

Session is used to track clients, that is, to distinguish specific clients, but its implementation is implemented through cookies. What does it mean? When the client sends a request, there will be a cookie. If the server wants to track the client's information, it will record a session id in the cookie. The next time the client requests again, it will use this session id, and when the server returns information, it will also find the client based on this session id. It can be said that they complement each other.

### 4. HTTPS

Everyone knows that HTTPS is a more secure communication protocol than HTTP. HTTP message content is plain text, while HTTPS encrypts the message for transmission, so the security will be better.

The difference between HTTPS and HTTP is shown in the figure below.

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9k7voqxcj310u0mste2.jpg)

HTTPS = HTTP + TLS/SSL.

HTTPS has a handshake process before establishing communication, that is, before the client and server establish a connection, they must be encrypted by symmetric and asymmetric encryption algorithms. Only after the client and server are both verified, can the connection be established and transmitted message. The specific process can be seen in the figure below.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9kkvbqegj30ms0nwn02.jpg" />



The specific process can be as follows:

The browser first sends the encryption rules it supports to the website, and the website will select a set of encryption algorithms and HASH algorithms, and send back its identity information to the browser in the form of a certificate, which contains the website address, public key, and information about the issuing authority of the certificate.

After the browser receives the certificate, it will generate a string of random numbers, encrypt the random numbers with the public key, calculate the handshake information with the agreed HASH algorithm, encrypt it with the random numbers, and then send it to the client.

After receiving it, the client first decrypts it with the private key, takes out the random number password, and then decrypts the handshake information with the random number password to verify whether the HASH algorithm is consistent with the one sent in for the first time, and then encrypts a piece of handshake information with the password. sent to the browser.

The browser decrypts and calculates the HASH of the handshake information. If it is consistent with the server, the whole process ends, and all subsequent communication data will be encrypted based on the encryption algorithm.

### 5. The difference between HTTPS and HTTP

HTTPS requires an SSL certificate for encryption and verification of handshake information

HTTP is Hypertext Transfer Protocol, information is transmitted in plain text, HTTPS is secure SSL encrypted transmission

The ports used are different, HTTPS is port 443, and HTTP is port 80

The http connection is very simple, but https establishes a connection to transmit data and requires SSL certification.

### 6. TCP and UDP

This is also a common test point for interviews, and the difference between the two is also obvious.

TCP is connection-oriented, UDP is connectionless, TCP transmission is more reliable, and there is an ordered sequence to ensure data integrity. The reliability of UDP is not so strong, there may be data loss.

The speed of TCP is relatively slow, because a lot of extra work needs to be done to establish a connection and ensure the reliability and order of messages; UDP is more suitable for applications that are more sensitive to speed.
