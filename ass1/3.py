hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com"]

while True:
	with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in website_list: 
                if website in content: 
                    pass
                else: 
                    file.write(redirect + " " + website + "\n") 
print("The website is blocked")
                    
                    
