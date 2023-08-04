# HTTP详解


这份总结可能不是覆盖所有的HTTP知识点，只是按照我自己理解的，然后结合网上资料，进行总结。

### 1. 什么是HTTP

HTTP(hypertext transport protocol), 就是超文本传输协议，文本可以理解为字符，文字，也可以是音视频等等。超文本就不是单纯的文本文件了，而是更加复杂的多种文件的混合。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf8j1170vxj30p80k0gr4.jpg" style="zoom: 67%;" />

其实也是非常好理解了，HTTP实际上还是一种应用层的协议，好了，来复习下网络的七层模型吧。应用层，表示层，会话层，传输层，网络层，链路层，物理层。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/gggg.jpeg)

这个图还是很全面的，概述了整个七层模型的每一层功能已经范围。而HTTP是属于应用层的协议。

### 2. 不同版本的HTTP

这个在面试的时候还是有问到，所以也说说这个吧。目前，http的版本共经历了四次的变化：

HTTP 0.9 --> HTTP 1.0 --> HTTP 1.1 --> HTTP 1.2

- HTTP 0.9

  第一个版本，这个版本只支持GET请求，且只能相应HTML字符串能力。

- HTTP 1.0

  新增了post， delete， put。 且新增了请求头和响应头的概念，并且指定了HTTP协议的版本号，状态码，编码等内容，同时还支持传输图片，音视频，二进制等内容。

- HTTP 1.1

  新增了长链接，新增管道化处理，缓存处理和断点传输。管道化，就是可以同时发送多个HTTP请求，而不用一个一个等待响应。断点续传，客户端会记录当前的下载进度，在需要续传时，再通知服务器本次需要下载的内容片段。长链接下面再详细说下。

#### 2.1 长链接和短链接的区别

其实也非常好理解了，长链接就是客户端和服务端建立连接后，就保持这个连接状态，不用一次请求结束后断开连接；短连接就相反，每次请求结束后就断开连接。所以他们的优缺点就非常明显。

长连接更好的节省了连接和关闭的时间，减少浪费。但是也会存在一个问题，就是随着连接数的增多，而客户端和服务端的连接一直在保持，会带来一些问题，服务端肯定会吃不消，对于这种情况呢，也有解决的方法，当连接数到达一定数后，服务端可以主动关闭一些长时间没有读写的事件连接。相对于来说，短连接的问题会更加严重，因为每次请求都要建立连接，然后在断开连接，如果对于那种频繁请求的服务，就会极大的占用资源。所以不管是长连接还是短连接，都是根据具体的需求来定。

### 3. HTTP的一些元素

#### 3.1 HTTP 报文

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jeo1er9j311w0m843k.jpg" style="zoom:150%;" />

这个就是HTTP报文的格式，上面一个是请求体，下面是返回的东西，具体的如下所示：

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jfvk74fj311i0jg47x.jpg" style="zoom:200%;" />

#### 3.2 URI

URI和URL啥区别，URI是用来干啥的。

URI是统一资源标识符。它是用来定义要访问的服务器的地址。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/ffff.jpeg" style="zoom:50%;" />

URI是包含URL和URN的。

#### 3.3 Cookie

因为HTTP是无状态的，啥意思呢，就是协议对于事务处理是没有记忆能力的，服务器端也不知道客户端的具体情况。Cookie的引入就是为了解决这个问题，cookie是有浏览器来负责存储的，而不是操作系统负责，换一个服务器，就不知道了。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9jwstm0uj30z20hqk0j.jpg" style="zoom:150%;" />

#### 3.4  session

Session是用来跟踪客户端的，就是用来区分特定的客户端，但是它的实现是通过cookie来实现的。什么意思呢，就是客户端发送请求是，会有一个cookie，然后服务端如果想要跟踪这个客户端的信息，就会在cookie里记录一个session id，下次这个客户再请求时，会用上这个session id，而服务端返还信息时，也会根据这个session id来找到客户端。可以说是相辅相成吧。

### 4. HTTPS

所有人都知道，HTTPS相较于HTTP是更加安全的通信协议，HTTP的报文内容是明文，而HTTPS会对报文进行加密传输，所以安全性会更好。

HTTPS相较于HTTP的区别在下图。

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9k7voqxcj310u0mste2.jpg)

HTTPS = HTTP + TLS/SSL.

HTTPS在建立通信之前是有一个握手的过程，就是客户端和服务端建立连接前，要通过对称和非对称加密算法进行加密，只有当客户端和服务端都验证通过后，才能建立连接，传输报文。 具体的过程可以看下图。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf9kkvbqegj30ms0nwn02.jpg"  />



具体流程可以如下：

浏览器先是将自己支持的加密规则发给网站，网站会选出一套加密算法和HASH算法，并将自己的身份信息以证书的形式发回给浏览器，证书里包含网站地址，公钥，以及证书的颁发机构等信息。

浏览器收到证书后，会生生成一串随机数，用公钥对随机数进行加密，用约定好的HASH算法计算握手信息，并用随机数进行加密，然后发给客户端。

客户端收到后先用私钥进行解密，取出随机数密码，然后在用随机数密码进行握手信息的解密，验证HASH算法是否和第一次发进来的一致，再使用密码加密一段握手信息，发给浏览器。

浏览器解密计算握手信息的HASH，如果和服务端一致整个过程结束，之后所有的通信数据都将基于加密算法进行加密。

### 5. HTTPS 和HTTP的区别

HTTPS需要SSL证书，用于加密和验证握手信息

HTTP是超文本传输协议，信息都是明文传输，HTTPS则是具有安全性的SSL加密传输

使用的端口不同，HTTPS是443端口，HTTP是80端口

http的连接很简单，但是https建立连接传输数据需要SSL认证。

### 6. TCP 和 UDP

这个也是面试常考的考点，两者的区别也很明显。

TCP是面向连接的，UDP是无连接的，TCP的传输更加可靠，有有序序列来保证数据的完整。UDP的可靠性没有这么强，可能会有数据的丢失。

TCP的速度比较慢，因为要创建连接，保证消息的可靠性和有序性，需要做额外的很多工作；UDP更适合对速度比较敏感的应用。






