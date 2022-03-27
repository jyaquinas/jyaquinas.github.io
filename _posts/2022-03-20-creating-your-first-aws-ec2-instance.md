---
layout: post
title: Creating Your First AWS EC2 Instance
subtitle: Set up your server using the free tier
date: 2022-03-20 21:17:00 +0900
background: '/img/bg-post.jpg'
category: "Server"
tags: [aws, server, ec2]
---

## AWS EC2
To run our applications continuously, we have a few options:
* Run the application on our PCs and keep it live for 24hrs
* Use a hosting service
* Use a cloud service

If we experience a lot of traffic at specific hours of the day, or we expect to scale our application, it is better to go for a cloud service, where we can easily expand the server specs as we need. 

Types of cloud services:
* Infrastructure as a Service (Iaas)
    * computing resources along with other services, such as storage, networking capabilities, etc
    * AWS EC2, S3, google compute engine, Microsoft azure
* Platform as a Service (PaaS)
    * complete development and deployment environment offered to customers
    * beanstalk, heroku, google app engine, windows azure
* Software as a Service (Saas)
    * service in the form of applications offered directly to customers
    * Google drive, dropbox, DocuSign

### What is AWS EC2
EC2 stands for Elastic Compute Cloud. It is a general-purpose computing resource with optimized computing performance, memory, storage, and networking. This can be automatically scaled up and down based on your application needs. Multiple operating systems are provided, but only the linux and windows instances (t2 or t3.micro) are available for the free tier.

The full list of EC2 instances can be found [here](https://aws.amazon.com/ec2/instance-types/).

#### Free Tier Limitations
* 1 year free trial period
* 750 hours/month of usage (so unlimited if you only use 1 micro instance)
* Linux or Windows operating systems

### Launching an EC2 Instance
1. Select your region on the top right corner (this is the AWS datacenter's physical location).
2. Click on EC2, then launch an instance.
3. Select the Amazon Machine Image (AMI)[^ami]. You can tick the 'Free tier only' checkbox. 
4. Select the instance (only the t2.micro falls under the free tier category).
5. Configure the instance (VPCs[^vpc], subnets, shutdown behavior, etc). If you're just starting, just use the default settings. 
6. Set the storage to 30 GB (the maximum for the free tier).
7. Add tags to your instance. This is to help you manage your resources as you add more resources. Check out the tagging [best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) recommended by Amazon.
8. Configure the security group, which controls your traffic through a set of firewall rules. It is recommended to only allow known IPs for security reasons (do not use the default 0.0.0.0/0). Check out this [security group guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html).
9. Launch.
10. Create and download new key pair (.pem file) for your instance. You will need this to access the server.

### Using Elastic IP
A new IP will be allocated every time the instance is restarted. So to keep using a fixed IP address, we will use the Elastic IP. 

On the left sidebar, click on Network & Security -> Elastic IPs.

Then click on 'Associate Elastic IP Address' and select your instance and private IP. 

***Important**: Unassociated elastic IPs are billable. Make sure to associate it with your free tier instance to avoid getting billed.*

### Connecting To Your EC2 Instance
Since I'm a mac user, I'll explain how you can connect to your instance using the terminal. You can also find instructions on how to connect using ssh in your AWS console.

`ssh -i keyfile.pem ec2-user@[ec2 ip address]`

The default username is `ec2-user`.

If you don't want to keep typing in the IP address, we can easily connect to a server using an alias. First, move your pem file to the following location, `~/.ssh/`.

`cp [current pem file path] ~/.ssh/`

Then let's create a config file. You can use any editor you like, but I'll use nano.

`nano ~/.ssh/config`

Fill in the information.

```shell
# config
Host yourAlias
    HostName yourHostName
    User ec2-user
    IdentityFile ~/.ssh/keyfile.pem
```

Set the name you want to use in the `Host` and input your EC2 instance hostname/IP for the `HostName`. Don't forget to save.

You can now connect with the hostname you set.

`ssh yourAlias`


### Changing Your Instance Hostname
You'll notice that when you connect to your instance, it will show your instance ip.  

`[ec2-user@ip-##-##-##-## ~]$`

But this can be confusing when you have more than one servers. It'll be easier to differentiate between servers if you name them. 

It will depend on your instance type. So you can check [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html) for more info.

For Amazon Linux 2, use the following command.

`sudo hostnamectl set-hostname YourHostName`

Then edit the file `/etc/hosts` using whatever editor you like.

`sudo nano /etc/hosts`

And add the following line:

`127.0.0.1 YourHostName`

Then reboot using `sudo reboot`.

Once you log in again, you'll now see:  

`[ec2-user@YourHostName ~]$`

### Setting Up Your Database
If you're going to set up a relational DB, you can use Amazon's RDS (Relational Database Service). The reason we want to create our DB through this instance is that manually setting it up on our EC2 instance is not only time-consuming, but we won't have the extra functionalities, like monitoring, that are provided by RDS. 

These are the first few things to set up after creating your RDS instance:
* Timezone
* Character set
* Max connection[^maxcon]

We can set this up in the parameter group. On the left sidebar, click on "Parameter groups" and create a new group. Let's edit the parameters we mentioned above.

Look for the `time_zone` parameter and set it to your timezone.

Type in `character_set` and set all the parameters that show up to `utf8mb4`[^utf], which is the charset used if you want to support emojis. 

The current `utf8` is an alias for `utf8mb3`, which encodes Unicode characters using 1-3 bytes per character. `utf8mb4`, on the other hand, uses 1-4 bytes per character. 

> UTF-8 encoding the same as utf8mb3 but which stores supplementary characters in four bytes.

Search for `collation` and set all the parameters to `utf8mb4_general_ci`. What is [collation](https://database.guide/what-is-collation-in-databases/#:~:text=In%20database%20systems%2C%20Collation%20specifies,the%20data%20in%20the%20database.)?

> In database systems, Collation specifies how data is sorted and compared in a database. Collation provides the sorting rules, case, and accent sensitivity properties for the data in the database.

Once we save all the parameters, we need to change the DB settings so that it uses this newly created parameter group. Click on 'Databases' on the left sidebar and click on 'Modify', then update the parameter group accordingly. Reboot the DB. 

### Accessing RDS From Your Local PC
To access the DB from your local PC, you must configure the security group. 
Add the following inbound rules:
* Type: MySQL/Aurora, Source: MyIP
* Type: MySQL/Aurora, Source: Custom -> Select the security group used for your EC2 instance (This will allow access from your EC2 instance)

Then connect to the DB using the 'Endpoint' shown on your RDS console as the hostname. If you don't remember the username, you can find it under the 'Configuration' tab, under 'Master username'.

Once you connect to your DB, you will see that some of the parameters (`character_set_database`, `collation_connection`) set from the parameter group haven't been properly set. You can check by running the following command:

```sql
use YourDBName; /* You can find it under the 'DBName' in your AWS console */
show variables like 'c%';
```

You'll see that the parameters mentioned above will be set to `latin` or something similar. Let's update this to `utf8mb4`. 
```sql
ALTER DATABASE YourDBName
CHARACTER SET = 'utf8mb4'
COLLATE = 'utf8mb4_general_ci';
```

Check and see if the timezone has been properly set.

`select @@time_zone, now();`

### Accessing RDS From EC2
Let's make sure we can access the RDS instance from the EC2 instance.

Connect to your EC2 instance and install MySQL.

`sudo yum install mysql`

Now connect to your DB.

`mysql -u [YourUserName] -p -h [YourDBEndpoint]`

You should be able to connect to it. If you're not able to, double-check your security group and see if your inbound rules have been set properly. 


---
[^ami]: AMIs are image containers that contain all the necessary components to launch the instances.  
[^vpc]: VPCs are virtual private networks, virtual versions of a physical network within the larger network. 
[^maxcon]: This is automatically calculated based on the instance, but we can also manually set it through the `max_connections` parameter. Check [here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.MaxConnections) for more info.
[^utf]: Check out this [stackoverflow post](https://stackoverflow.com/questions/30074492/what-is-the-difference-between-utf8mb4-and-utf8-charsets-in-mysql) for more info.