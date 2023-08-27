# Nginx


### 1. What is Nginx?

From Google result, Nginx is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. Nginx is known for its high performance, stability, rich feature set, simple configuration, and low resource consumption. Nginx supports up to 50000 concurrent applications.

### 2. Forward And Reverse Proxy

The forward proxy is a proxy server between the client and the target server.  In order to obtain content from the original server, the client sends a request to the proxy server, and specifies the target server, after which the proxy transfers to the target server and returns the obtained content to the client. 

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf4iaf9a6xj317s0i6dlj.jpg" style="zoom:200%;" />

Like this, you can't reach the www.google.com if you have direct access. But you can use the forward proxy. In the forward proxy, the real client is invisible to the server. The final result is that you can access the www.google.com site via the proxy server. This is the forward proxy.

Okay, now we can compare the reverse proxy. It's just the opposite. To the client, the reverse proxy is like the target server.The client doesn't need to make any settings. The client sends a request to the reverse proxy, and then the reverse proxy determines where the request is going, and forwards the request to the client. 

![](https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf4j1ik578j31qa0i4tdk.jpg)

Like above, the reverse proxy is to proxy the server, it's very common. For example, you everyday visit the www.google.com, it's actually a reverse proxy, you don't know the real server address. Just show the proxy address.

### 3. Load Balancing

Load Balancing, which means that the load is balanced and distributed to multiple operation units to run in order to complete the work task collaboratively. Load balancing is built on the original network structure, which provides a transparent and inexpensive and effective method to expand the bandwidth of servers and network devices, strengthen network data processing capabilities, increasing throughput, and increase network availability and flexibility.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1gf4kh82548j30vd0u047l.jpg" style="zoom: 50%;" />

The above architecture is very common. It can balance the internet requests through the load balance. It was used in the high concurrency. 

### 4. Hot Standby

![img](https://user-gold-cdn.xitu.io/2018/7/4/16463cd149a85d6d?imageslim) 

In this picture, we can see one of the load balancing applications.  It's high available. There are 2 load balancer servers including primary and secondary server. The primary and secondary communicate through the health check. If the primary server is down, then secondary server can't contact with the primary, then will know it's wrong. The flow will forward to secondary server instead of the primary. In this way, can guarantee the normal operation of the system.

### 5. Dynamic And Static Separation

Dynamic and static separation is to make the dynamic webpage in the dynamic website distinguish the invariable resources from the constantly changing resources according to certain rules. 

Nginx can separate the resources via the config file. It can boost the performance in this way.

### 6. Best Practice

Can refer to the website.









 

