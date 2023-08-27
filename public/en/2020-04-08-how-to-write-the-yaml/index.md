# How to write YAML


### 1. How to write the YAML

>```yaml
>apiVersion: apps/v1
>kind: Deployment
>metadata: 
>  name: nginx-deploymnet
>spec: 
>  replicas: 3
>  selector:
>    matchLabels:
>      app: web_server
>  template: 
>    metadata: 
>      labels: 
>        app: web_server
>    spec: 
>      containers:
>      - name: nginx
>        image: nginx:1.7.9
>```

Okay, Let us analysis this YAML sample. 
It used the indentation to represent the layer. Every layer was dependent and called each other.The meaning of every key.

apiVersion: this is the current configure version.

Kind: the resource created type. 

Metadata: the resource metadata. 

spec：the deployment's specification. 

Selector: use to select which template. 

Template: define the pod information. 

So, from this, I think I can describe with mind map.We can refer to below.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images00831rSTgy1gdjavs7f3cj316b0u043t.jpg" style="zoom:200%;" />

###  2. How to write the job configure file

At first, we need to determine the aim of job. The containers can divide into two types, one is for the persistence running for the server, another one is for just one job, one time running. This is the job. How to define Job configure file.

>```yaml
>apiVersion: batch/v1
>kind: Job
>metadata:
>  name: myjob
>spec:
>  parallelism: 3
>  template:
>    metadata:
>      name: myJob 
>    spec: 
>      containers:
>      - name: hello 
>        image: busybox
>        command: ["echo", "hello k8s job" ]
>      restartPolicy: OnFailure
>```

Actually there are many kinds of job configures, including regular job, parallelism job and timing job. Also need to flexible use the restartPolicy parameter. OnFailure means, when failed, will restart the pod. You can set "never" as well means will restart the pod until it 's successful.

### 3. Summary of YAML
In the end, I think YAML is not difficult if you master the rules. It's comprised with layers. So if you understand every layer, you can design your deployment, job or services.

