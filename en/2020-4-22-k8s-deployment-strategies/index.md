# K8S Deployment Strategies


### 1. Background

We always deploy the final version applications to the production env. There are several ways to ensure the release production stably and safety. Below sections are k8s deployment strategies.

### 2. The Strategies

There are 4 ways to do the production release. 1) Rolling-update. 2) Recreate. 3) Blue/Green. 4) Canary. Below is the details.

- **Recreate Update**

  This is very clumsy way to update. Destory V1 application  then create V2 application. Will hit service down issue in a period time. 

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p8fwyufj31ga0e8wiv.jpg" style="zoom:200%;" />

- **Rolling update.**

  This is the most commonly used. 

  - **Performing an automatic rolling update with a RC**

    >```yaml
    >apiVersion: v1
    >kind: ReplicationController
    >metadata:
    >  name: kubia-v1
    >spec:
    >  replicas: 3
    >  template:
    >    metadata:
    >      name: kubia
    >      labels:
    >        app: kubia
    >    spec:
    >      containers:
    >      - image: luksa/kubia:v1
    >        name: nodejs
    >---
    >apiVersion: v1
    >kind: Service
    >metadata:
    >  name: kubia
    >spec:
    >  type: NodePort
    >  selector:
    >    app: kubia
    >  ports:
    >  - port: 80
    >    targetPort: 8080
    >    nodePort: 30007
    >```

    To run this app, will create a ReplicationController and NodePort service to enable to access the app externally. Then open another terminal to monitor the service.

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n0jmlvwj31dq09yq59.jpg" style="zoom:200%;" />

    Then performing a rolling update with kubectl, will create version 2 of the app. Execute below command:

    >```shell
    >kubectl rolling-update kubia-v1 kubia-v2 --image=luksa/kubia:v2
    >```

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mlnx3v7j31dq07eq53.jpg" style="zoom:200%;" />

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mmck3x8j31dk06y75x.jpg" style="zoom:200%;" />

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mnx7txzj31160j20vd.jpg" style="zoom:200%;" />

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2mq854t1j31ce0tqgz2.jpg" style="zoom:200%;" />

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n3378duj31eu0dqdix.jpg" style="zoom:200%;" />

  - **Using Deployment  for updating apps declaratively**

    A deployment is a high-level resource meant for deploying applications and updating them declaratively, instead of doing it through a RC or RS, which are both considered lower-level concepts.

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2n83ztwtj30mq050t8z.jpg" style="zoom:200%;" />

    >```yaml
    >apiVersion: apps/v1
    >kind: Deployment
    >metadata:
    >  name: kubia-v1
    >spec:
    >  replicas: 3
    >  selector:
    >    matchLabels:
    >      app: kubia
    >  template:
    >    metadata:
    >      name: kubia
    >      labels:
    >        app: kubia
    >    spec:
    >      containers:
    >      - image: luksa/kubia:v1
    >        name: nodejs
    >---
    >apiVersion: v1
    >kind: Service
    >metadata:
    >  name: kubia
    >spec:
    >  type: NodePort
    >  selector:
    >    app: kubia
    >  ports:
    >  - port: 80
    >```

    Also to run this application, after completed, change the v1 deployment container to v2, then deploy with the new version.

    >```shell
    >kubectl apply -f kubia-deploy-v2.yaml
    >```

    After that, you can notice that there will reserve the V1 RS. So it's very easy to rollback the version from V2 to V1.

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2oder9xjj316203qab6.jpg" style="zoom:200%;" />

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2oeo5z3zj30u00ud47r.jpg" style="zoom:200%;" />

    Use this command to roll back the deployment.

    >```shell
    >kubectl rollout undo deployment kubia
    >```
    >
    >```shell
    >kubectl rollout history deployment kubia
    >```
    >
    >```shell
    >kubectl rollout undo deployment kubia --to-revision=1
    >```

    <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2ol1uaivj313c0b0gmr.jpg" style="zoom:200%;" />

- **Blue / Green** 

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2omtr0qij313i0iidl9.jpg" style="zoom:200%;" />

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2ouuod2xj31go0e8436.jpg" style="zoom:200%;" />

  Actually this deployment needs V1 and V2 applications are existing. The client connect the Deployment through the labels. 

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2otd304pj312u0iedn4.jpg" style="zoom:200%;" />

-  **Canary Deployment**

  <img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p1g1r2sj312g0iqjwu.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p1vzi0nj312i0i679j.jpg" style="zoom:200%;" />

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/007S8ZIlgy1ge2p2ln3wcj31h00e6dkh.jpg" style="zoom:200%;" />


