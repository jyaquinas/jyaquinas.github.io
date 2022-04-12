---
layout: post
title: Zero Downtime Deployment with Nginx
subtitle: ---
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "CICD"
tags: [nginx, deployment]
---

* zero downtime deployment
    * app is never down or unstable during deployment process 
    * nginx, docker, kubernetes, blue green
    * blue green
        * set up 2 production environments, test code in green environment, then switch router so that all incoming requests go to the green environment (instead of the blue). Any error -> switch back to blue
    * nginx
        * used as load balancer, reverse proxy, caching, web server, media streaming, etc
        * reverse proxy -> gets incoming requests and redirects them to backend server
    * Use nginx  for blue green deployment
        * nginx (80, 443 port), and 2 jar files (8081, 8082 port)
        * nginx redirects to 8081 (blue), test deployment on 8082, after successfully testing, nginx reload -> redirect to 8082 (done in 0.1s)
        * repeat for next deployment, this time using 8081 and green environment (switch back and forth)
    * installing nginx on amazon ec2 instance -> use `sudo amazon-linux-extras install` -> lists available packages that you can install
        * `sudo amazon-linux-extras install nginx1`
        * check nginx status with `systemctl status nginx.service`
        * default nginx port -> 80 (access your website without the :8080 and you should see a nginx page)
    * nginx settings -> `sudo nano /etc/nginx/nginx.conf`
    ```bash
        server {
        listen       80;
            listen       [::]:80;
            server_name  _;
            root         /usr/share/nginx/html;

            # Load configuration files for the default server block.
            include /etc/nginx/default.d/*.conf;

            location / {
                    # nginx redirect to
                    proxy_pass http://localhost:8080;   
                    # pass request data to header
                    proxy_set_header X-Real_IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header Host $http_host;
            }

        error_page 404 /404.html;
            location = /404.html {
            }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
            }
        }
    ```
    * restart `sudo service nginx restart`
    
