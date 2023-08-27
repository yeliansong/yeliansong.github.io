# 七、ConfigMap and Secret configuration application


### 1. Configuration of container command line parameters

Docker uses command line parameters by defining Entrypoint and CMD in Dockerfile, but there is a problem, this is packaged into the image. Let’s take a look at the difference between the two first.

Entrypoint: Defines the executable program that is invoked when the container starts.

CMD: Specifies the parameters passed to Entrypoint.

So the usual practice is to define these two. When starting with the command line, you can use the argu of the command line to override the definition of CMD in the file. Of course, there is another way, which is the script method, which can write commands into the script, and then define and call the script in the dockerfile.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqeiovej30lb03ct9m.jpg" style="zoom:200%;" />

Commands defined in the POD can override the container's command line. So arguments can be passed to the container via argu in the POD's YAML file.



### 2. General operation of POD environment variables

Before introducing ConfigMap, let's take a look at the general operation of POD configuration environment variables. In fact, you have to understand that environment variables are for containers, so one way of thinking is this. Define environment variables in the container, and the programs in the container reference the environment variables, and then assign values to the environment variables in the POD configuration file. , which is normal operation.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqf7yhhj30it05rgml.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqgyzg8j30j4052wf2.jpg" style="zoom:200%;" />

Just like this, an environment variable is defined, and then, this variable is assigned in the POD. How about this method, okay? Obviously it is not good. Without decoupling, the environment variables and POD configuration files are strongly related. So is there a good way to achieve decoupling? That is, this configuration file can be used not only here, but also in other places . This uses ConfigMap.



### 3. ConfigMaps

First of all, we must understand the problem it needs to solve. In fact, it is equivalent to an independent configuration file, and then it can be referenced in different environments. So this thing is pretty good. Creating a ConfigMap can be done through commands or YAML files. How to create it is not described in detail.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqhmjtoj30kh095wgt.jpg" style="zoom:200%;" />

This example is to use POD to rewrite the environment variable INTERVAL in the container. The basic process is this:

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqjde66j30io08mwjy.jpg" style="zoom:200%;" />

Don't explain it, it's clear. But there is a question, what if this configuration file does not exist, can this POD still be up, the answer is no. It will wait until the configuration file exists before the container can start. Of course, you can also set parameters so that it can start POD without a configuration file.

Of course, if your config file contains a lot of key-values, it is troublesome to set them one by one, but it can be done in one step.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images006y8mN6gy1g6ycqjvnbyj30ib04nwfr.jpg" style="zoom:200%;" />

prefix is used to set the prefix, and there is another one. The key-value set in the configuration file must be in accordance with the format, otherwise, Kubernetes cannot parse it.



### 4. secert configuration file

Of course, the configuration files cannot be all named texts, and those that need to be encrypted need to be configured in secert mode. The secret is also a key-value method like configMap, but there are still some differences. The secret exists in the memory of the POD, so when the POD is deleted, there is no such configuration.
